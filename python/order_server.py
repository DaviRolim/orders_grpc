from concurrent import futures
import logging

import grpc
import order_pb2
import order_pb2_grpc

class Order(order_pb2_grpc.OrderServicer):
    def __init__ (self):
        self.db = {}

    def SendOrder(self, request, context):
        self.db[request.id] = request
        print(self.db)
        return order_pb2.OrderReply(status=201, message="Saved item successfully")
        # return super().SendOrder(request, context)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServicer_to_server(
        Order(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()