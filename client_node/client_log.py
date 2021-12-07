import random

import grpc

from client_grpc import ReplicatedLog_pb2_grpc, ReplicatedLog_pb2

secondary_servers_ports = [50052, 50053]

master_port = 50051

messages_batch = 1


def generate_messages():
    global messages_batch
    messages = [
        (random.randint(1, 3), "Batch {}".format(messages_batch)),
        (random.randint(1, 3), "First message"),
        (random.randint(1, 3), "Second message"),
        (random.randint(1, 3), "Third message"),
        (random.randint(1, 3), "Fourth message"),
        (random.randint(1, 3), "Fifth message"),
    ]

    messages_batch += 1

    return messages


def post():
    with grpc.insecure_channel(f'172.17.0.1:{master_port}') as channel:
        client = ReplicatedLog_pb2_grpc.PostRequestServiceStub(channel)
        messages = [(1, "5 message")]
        for msg in messages:
            request = ReplicatedLog_pb2.POST(w=msg[0], msg=msg[1])
            response = client.PostRequest(request)
            print(response)


def get_master():
    with grpc.insecure_channel(f'172.17.0.1:{master_port}') as channel:
        client = ReplicatedLog_pb2_grpc.GetRequestServiceStub(channel)
        request = ReplicatedLog_pb2.GET(msg='1')
        response = client.GetRequest(request)
        print(response.data)


def get_slaves(port):
    with grpc.insecure_channel(f'172.17.0.1:{port}') as channel:
        client = ReplicatedLog_pb2_grpc.GetRequestServiceStub(channel)
        request = ReplicatedLog_pb2.GET(msg='1')
        try:
            response = client.GetRequest(request)
        except:
            return f'node {port} not responding.'
        return response.data


def get_heartbeats():
    with grpc.insecure_channel(f'172.17.0.1:50051') as channel:
        client = ReplicatedLog_pb2_grpc.AskHeartBeatsServiceStub(channel)
        request = ReplicatedLog_pb2.AskHeartBeat()
        response = client.HeartBeatRequest(request)
        return list(zip(response.address, response.heartbeats))


def run():
    user_input = input('Enter which request to simulate: POST, GET, Heartbeats or quit\n').lower()
    while user_input != 'quit':
        if user_input == 'post':
            print('Calling POST')
            post()
        elif user_input == 'get':
            ask_node = input('Enter where you want logs from: master - m, secondaries - s,'
                             ' secondary 1 - s1 or secondary 2 - s2\n').lower()
            if ask_node == 'm':
                print('calling GET')
                get_master()
            elif ask_node == 's':
                print('calling GET')
                for i in secondary_servers_ports:
                    print(f'Node {i}', get_slaves(i))
            elif ask_node == 's1':
                print('calling GET')
                print(get_slaves(secondary_servers_ports[0]))
            elif ask_node == 's2':
                print('calling GET')
                print(get_slaves(secondary_servers_ports[1]))

        elif user_input == 'heartbeats':
            print(get_heartbeats())

        else:
            print('Wrong input\n')

        user_input = input('Enter which request to simulate: POST, GET, Heartbeats or quit\n').lower()


if __name__ == '__main__':
    run()


