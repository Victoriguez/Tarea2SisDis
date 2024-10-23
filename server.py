from concurrent import futures
import grpc
import order_pb2
import order_pb2_grpc
import uuid
import kafka_producer  # Publica eventos en Kafka

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        # Crear un ID único para el pedido
        order_id = str(uuid.uuid4())
        status = "Procesando"

        # Publicar el evento del pedido en Kafka
        kafka_producer.publish_order_event(order_id, request)

        # Retornar la respuesta
        return order_pb2.OrderResponse(order_id=order_id, status=status)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor de pedidos iniciado en el puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
