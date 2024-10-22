from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_order_event(order_id, order_request):
    event_data = {
        'order_id': order_id,
        'product_name': order_request.product_name,
        'price': order_request.price,
        'payment_gateway': order_request.payment_gateway,
        'card_brand': order_request.card_brand,
        'bank': order_request.bank,
        'region': order_request.region,
        'address': order_request.address,
        'email': order_request.email,
        'status': 'Procesando'
    }
    producer.send('order-events', event_data)
    producer.flush()
    print(f"Evento publicado para el pedido {order_id}")

