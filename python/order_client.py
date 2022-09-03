from __future__ import print_function

import logging
import random

import grpc
import order_pb2
import order_pb2_grpc
from uuid import uuid4


#   string id = 1;
#   string name = 2;
#   float price = 3;
#   int32 quantity = 4;
def list_orders(stub):
    result = stub.ListOrder(order_pb2.Empty())
    for item in result:
        print(item)


def delete_order(stub):
    order_id = order_pb2.OrderId(id='3')
    try:
        result = stub.DeleteOrder(order_id)
        print(f'result" {result}')
    except Exception as e:
        print(e)


def place_order(stub):
    order_request = order_pb2.OrderRequest(id='3',
                                           name='StandUp Desk',
                                           price=999.30,
                                           quantity=1)
    result = stub.SendOrder(order_request)
    print(f'result" {result}')
    return


def update_order(stub):
    order_request = order_pb2.OrderRequest(id='2',
                                           name='Paciencia',
                                           price=9999999999.0,
                                           quantity=100)
    result = stub.UpdateOrder(order_request)
    print(f'result" {result}')
    return


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderStub(channel)
        print("-------------- PlaceOrder --------------")
        # place_order(stub)
        delete_order(stub)
        # list_orders(stub)
        # update_order(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
