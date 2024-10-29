from elasticsearch import Elasticsearch
from datetime import datetime

# Conexión a Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

def store_performance_metrics(order_id, status):
    doc = {
        'order_id': order_id,
        'status': status,
        'timestamp': datetime.now(),
        'latency': calculate_latency(),
        'throughput': calculate_throughput(),
    }
    es.index(index="performance_metrics", document=doc)
    print(f"Métricas de rendimiento almacenadas para el pedido {order_id}")

def calculate_latency():
    # Simulación del cálculo de latencia (en milisegundos)
    return 200  # Aquí iría el cálculo real basado en eventos del sistema

def calculate_throughput():
    # Simulación del cálculo de throughput (en pedidos por minuto)
    return 5  # Aquí iría el cálculo real de throughput del sistema
