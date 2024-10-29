from confluent_kafka import Producer
import json

# Configura el productor
producer = Producer({
    'bootstrap.servers': 'localhost:9092'  
})

def delivery_report(err, msg):
    if err is not None:
        print(f"Fallo al entregar el mensaje: {err}")
    else:
        print(f"Mensaje entregado a {msg.topic()} [{msg.partition()}]")

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
    producer.produce('order-events', key=str(order_id), value=json.dumps(event_data), callback=delivery_report)
    producer.flush()
