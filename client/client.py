import grpc
import order_pb2
import order_pb2_grpc

def run():
    # Establecer conexión con el servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_pb2_grpc.OrderServiceStub(channel)

        # Crear la solicitud de pedido
        order_request = order_pb2.OrderRequest(
            product_name="Laptop",
            price=1200.00,
            payment_gateway="MercadoPago",
            card_brand="VISA",
            bank="Banco XYZ",
            region="Región Metropolitana",
            address="Calle Falsa 123",
            email="cliente@ejemplo.com"
        )

        # Enviar el pedido y recibir la respuesta
        response = stub.CreateOrder(order_request)
        print(f"Pedido creado con ID: {response.order_id}, Estado: {response.status}")

if __name__ == '__main__':
    run()
