import threading
import time
import queue

class SimuladorPedidos:
    def __init__(self):
        self.pedidos = queue.Queue()

    def realizar_pedido(self, pedido):
        print(f"\nEmpleado {threading.current_thread().name} recibe pedido: {pedido}")
        time.sleep(3)  # Simula el tiempo que lleva procesar el pedido
        print(f"\nEmpleado {threading.current_thread().name} completa pedido: {pedido}")

    def procesar_pedidos(self):
        while True:
            pedido = self.pedidos.get()
            if pedido is None:
                break
            self.realizar_pedido(pedido)

if __name__ == "__main__":
    inicio = time.time()
    simulador = SimuladorPedidos()
    print("\n\tHay 3 empleados ya hay 5 pedidos")

    # Crear hilos que representan empleados
    empleados = []
    for i in range(3): #
        empleado = threading.Thread(target=simulador.procesar_pedidos, name=i+1)
        empleados.append(empleado)
        empleado.start()

    # Simular llegada de pedidos
    for pedido_num in range(1, 6):
        simulador.pedidos.put(pedido_num)

    # Añadir sentinela para indicar fin de pedidos
    for _ in range(len(empleados)):
        simulador.pedidos.put(None)

    # Esperar a que todos los empleados completen sus tareas
    for empleado in empleados:
        empleado.join()

    print("\n\tTodos los pedidos han sido procesados.")
    tiempo_transcurrido = time.time() - inicio
    print("\tTiempo transcurrido:", tiempo_transcurrido, "segundos")
