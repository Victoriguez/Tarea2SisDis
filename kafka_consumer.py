from confluent_kafka import Consumer, KafkaError
import json
import time
import elastic_manager
import email_service
from order_manager import OrderManager

# Configura el consumidor
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'order-consumer-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['order-events'])

# Instancia de OrderManager para manejar pedidos
order_manager = OrderManager()

def process_order_event(event):
    order_id = event['order_id']
    order = order_manager.create_order(
        product_name=event['product_name'],
        price=event['price'],
        payment_gateway=event['payment_gateway'],
        card_brand=event['card_brand'],
        bank=event['bank'],
        region=event['region'],
        address=event['address'],
        email=event['email']
    )

    for _ in range(len(order_manager.states) - 1):
        order_manager.simulate_processing_time()
        order = order_manager.update_order_status(order)
        elastic_manager.store_performance_metrics(order['order_id'], order['status'])
        subject = f"Actualización de Pedido: {order['product_name']}"
        message = f"Su pedido con ID {order['order_id']} ha sido actualizado al estado: {order['status']}."
        email_service.send_email(order['email'], subject, message)

def run_consumer():
    print("Iniciando consumidor confluent-Kafka...")
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Fin de la partición")
            elif msg.error():
                print("Error del consumidor: {}".format(msg.error()))
                break
        else:
            event = json.loads(msg.value().decode('utf-8'))
            process_order_event(event)

if __name__ == '__main__':
    run_consumer()
