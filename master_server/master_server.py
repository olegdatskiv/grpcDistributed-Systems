import time
from concurrent import futures
from threading import Thread, Condition

import grpc

from master_grpc import ReplicatedLog_pb2_grpc, ReplicatedLog_pb2

logs = {}
secondary_servers_ports = [50052, 50053]
secondary_servers_hosts = ['node1', 'node2']
message_id = 0

waiting_parameter = 5.0
delays = [0.5, 1, 5, 10, 20]

quorum = 2
quorum_state = False


def post_secondary(host, port, msg, message_id, delay, latch):
    """
    Connect to secondary server, check accessibility, retry if needed, send messages with id
    :param host: host secondary server
    :param port: port of secondary server
    :param msg: message from client
    :param message_id: id of message to be replicated
    :param latch: CountDownLatch object
    :param delay: delay id for iterating delays array
    :return:
    """
    with grpc.insecure_channel(f'{host}:{port}') as channel:
        client = ReplicatedLog_pb2_grpc.PostRequestServiceStub(channel)
        secondary_request = ReplicatedLog_pb2.POST(w=message_id, msg=msg)
        try:
            client.PostRequest(secondary_request)
        except:
            time.sleep(delays[delay])
            if delay == 4:
                heartbeat_delay = 60
                heartbeat = heartbeat_node(host, port)
                while heartbeat == 0:
                    time.sleep(heartbeat_delay)
                    heartbeat = heartbeat_node(host, port)
                delay -= 1
            post_secondary(host, port, msg, message_id, delay + 1, latch)
            return 0
        latch.count_down()
        return 1


class PostServerRequest(ReplicatedLog_pb2_grpc.PostRequestServiceServicer):
    """
    Post Logic Master
    """
    def PostRequest(self, request, context):
        global message_id, quorum_state

        if not quorum_state:
            return ReplicatedLog_pb2.POSTResponse(
                msg='No quorum servers are available. Master server in read-only mode')

        message_id += 1
        logs[message_id] = request.msg
        threads = []
        latch = CountDownLatch(request.w - 1)
        delay = 0

        for i in range(len(secondary_servers_ports)):
            thread = Thread(target=post_secondary, args=(secondary_servers_hosts[i], secondary_servers_ports[i],
                                                         request.msg, message_id, delay, latch))
            thread.start()
            threads.append(thread)

        latch.__await__()
        for thread in threads:
            thread.join(waiting_parameter)

        return ReplicatedLog_pb2.POSTResponse(msg=f'Master and Secondaries servers have '
                                                  f'received msg={request.msg}, w={request.w}')


class GetServerRequest(ReplicatedLog_pb2_grpc.GetRequestServiceServicer):
    """
    Send local messages to Client
    """

    def GetRequest(self, request, context):
        msgs_list_txt = [v for k, v in logs.items()]
        return ReplicatedLog_pb2.GETResponse(data=msgs_list_txt)


def heartbeat_node(secondary_host, secondary_port):
    """
    Check node for accessibility
    :param secondary_host: host
    :param secondary_port: port
    :return: int 1-node is alive, 0-node is dead
    """

    with grpc.insecure_channel(f'{secondary_host}:{secondary_port}') as channel:
        client = ReplicatedLog_pb2_grpc.AskHeartBeatServiceStub(channel)
        request_to_node = ReplicatedLog_pb2.AskHeartBeat()
        try:
            return client.HeartBeatRequest(request_to_node).heartbeat
        except:
            return 0


def check_quorum(n):
    """
    Check for quorum every 0.5sec, if system doesn't have quorum,
    master goes to read-only mode
    :param n: int quorum
    """
    global quorum_state
    while True:
        active_nodes = [heartbeat_node(secondary_servers_hosts[i], secondary_servers_ports[i])
                        for i in range(len(secondary_servers_hosts))]
        quorum_state = sum(active_nodes) >= n
        time.sleep(0.5)


class HeartBeat(ReplicatedLog_pb2_grpc.AskHeartBeatsServiceServicer):
    """
    HeartBeat API
    """

    def HeartBeatRequest(self, request, context):
        """
        Check all slaves accessibility
        :return: array with addresses and array with heartbeats: 1-alive; 0-dead
        """

        heartbeats = []
        address = []
        for i in range(len(secondary_servers_ports)):
            address.append(f'{secondary_servers_hosts[i]}:{secondary_servers_ports[i]}')
            heartbeats.append(heartbeat_node(secondary_servers_hosts[i], secondary_servers_ports[i]))
        return ReplicatedLog_pb2.HeartBeats(address=address, heartbeats=heartbeats)


class CountDownLatch(object):
    def __init__(self, count=1):
        self.count = count
        self.lock = Condition()

    def count_down(self):
        self.lock.acquire()
        self.count -= 1
        if self.count <= 0:
            self.lock.notifyAll()
        self.lock.release()

    def __await__(self):
        self.lock.acquire()
        while self.count > 0:
            self.lock.wait()
        self.lock.release()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ReplicatedLog_pb2_grpc.add_PostRequestServiceServicer_to_server(PostServerRequest(), server)
    ReplicatedLog_pb2_grpc.add_GetRequestServiceServicer_to_server(GetServerRequest(), server)
    ReplicatedLog_pb2_grpc.add_AskHeartBeatsServiceServicer_to_server(HeartBeat(), server)
    server.add_insecure_port("master:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    Thread(target=check_quorum, args=(quorum,)).start()
    serve()
