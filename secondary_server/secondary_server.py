import argparse
import random
import time
from concurrent import futures
from queue import Queue

import grpc

from secondary_grpc import ReplicatedLog_pb2_grpc, ReplicatedLog_pb2

logs = {}
q = Queue()


def save_log(msg_id, msg):
    """
    Save msg into logs and duplicate check
    :param msg_id: message id
    :param msg: message from client
    :return: 0 if it`s duplicate
    """

    if msg_id in logs:
        return 0
    else:
        logs[msg_id] = msg


class PostServerRequest(ReplicatedLog_pb2_grpc.PostRequestServiceServicer):
    """
    Log message, simulated internal server error and latency
    """

    def PostRequest(self, request, context):
        if random.uniform(0, 1) < 0.5:
            sleep = random.randint(2, 8)  # realization of random latency
            time.sleep(sleep)
        save_log(request.w, request.msg)
        if random.uniform(0, 1) < 0.4:  # realization of random error
            raise Exception('InternalServerError')
        return ReplicatedLog_pb2.POSTResponse(msg='1')


class GetServerRequest(ReplicatedLog_pb2_grpc.GetRequestServiceServicer):
    """
    Send message API.
    """

    def GetRequest(self, request, context):
        prev = 0
        msgs_list_txt = []
        for k, v in logs.items():
            if k - prev <= 1:
                prev = k
                msgs_list_txt.append(v)
            else:
                break
        return ReplicatedLog_pb2.GETResponse(data=msgs_list_txt)


class SecondaryServerSendHeartBeat(ReplicatedLog_pb2_grpc.AskHeartBeatServiceServicer):
    """
    Send heartbeat API.
    """

    def HeartBeatRequest(self, request, context):
        return ReplicatedLog_pb2.HeartBeat(heartbeat=1)


def serve(args_input):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    ReplicatedLog_pb2_grpc.add_PostRequestServiceServicer_to_server(PostServerRequest(), server)
    ReplicatedLog_pb2_grpc.add_GetRequestServiceServicer_to_server(GetServerRequest(), server)
    ReplicatedLog_pb2_grpc.add_AskHeartBeatServiceServicer_to_server(SecondaryServerSendHeartBeat(), server)
    server.add_insecure_port(f"{args_input.host}:{args_input.port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process secondary server configure host and port.')
    parser.add_argument('--host', type=str,
                        help='host of secondary server')
    parser.add_argument('--port', type=int,
                        help='port of secondary server')

    args = parser.parse_args()

    serve(args)
