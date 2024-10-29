import uuid
import time

class OrderManager:
    def __init__(self):
        # Definir los posibles estados del pedido en un flujo
        self.states = ['Procesando', 'Preparación', 'Enviado', 'Entregado', 'Finalizado']

    def create_order(self, product_name, price, payment_gateway, card_brand, bank, region, address, email):
        """
        Crear un nuevo pedido con un estado inicial.
        """
        order_id = str(uuid.uuid4())  # Genera un ID único para cada pedido
        order = {
            'order_id': order_id,
            'product_name': product_name,
            'price': price,
            'payment_gateway': payment_gateway,
            'card_brand': card_brand,
            'bank': bank,
            'region': region,
            'address': address,
            'email': email,
            'status': self.states[0]  # Estado inicial: 'Procesando'
        }
        print(f"Nuevo pedido creado: {order}")
        return order

    def update_order_status(self, order):
        """
        Actualizar el estado del pedido de acuerdo con el flujo predefinido.
        """
        current_status = order['status']
        try:
            # Obtener el índice actual y actualizar al siguiente estado
            current_index = self.states.index(current_status)
            next_status = self.states[current_index + 1] if current_index < len(self.states) - 1 else current_status
            order['status'] = next_status
            print(f"Pedido {order['order_id']} actualizado a: {next_status}")
            return order
        except ValueError:
            print(f"Error: Estado '{current_status}' no encontrado.")
            return None

    def simulate_processing_time(self, min_time=1, max_time=3):
        """
        Simula el tiempo de procesamiento entre estados.
        """
        processing_time = min_time + (max_time - min_time) * 0.5  # Simulación con un tiempo promedio
        time.sleep(processing_time)  # Pausa para simular el procesamiento
        print(f"Tiempo de procesamiento simulado: {processing_time:.2f} segundos")
