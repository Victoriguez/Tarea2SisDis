from kafka import KafkaConsumer
import json
import time
import elastic_manager  # Integra Elasticsearch

# Configuramos el consumidor Kafka
consumer = KafkaConsumer(
    'order-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='order-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def process_order_event(event):
    order_id = event['order_id']
    product_name = event['product_name']
    status = event['status']

    # Simular procesamiento del pedido
    print(f"Procesando pedido {order_id} - {product_name}")
    time.sleep(2)  # Simulamos un tiempo de procesamiento
    
    # Actualizar el estado del pedido
    next_status = update_order_status(order_id, status)

    # Registrar métricas en Elasticsearch
    elastic_manager.store_performance_metrics(order_id, next_status)

def update_order_status(order_id, current_status):
    states = ['Procesando', 'Preparación', 'Enviado', 'Entregado', 'Finalizado']
    if current_status in states:
        next_status = states[states.index(current_status) + 1] if states.index(current_status) < len(states) - 1 else current_status
        print(f"Actualizando estado del pedido {order_id} a {next_status}")
        return next_status
    return current_status

def run_consumer():
    print("Iniciando consumidor Kafka...")
    for message in consumer:
        event = json.loads(message.value)
        process_order_event(event)

if __name__ == '__main__':
    run_consumer()
