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

def crear_hilos():

    empleado1 = threading.Thread(target=simulador.procesar_pedidos, name= 1)
    empleado2 = threading.Thread(target=simulador.procesar_pedidos, name= 2)
    empleado3 = threading.Thread(target=simulador.procesar_pedidos, name= 3)
    
    empleado1.start()
    empleado2.start()
    empleado3.start()
    
    # Esperar a que todos los empleados completen sus tareas
    empleado1.join()
    empleado2.join()
    empleado3.join()

def enviar_pedidos(simulador):
    
     # Simular llegada de pedidos
    simulador.pedidos.put(1)
    simulador.pedidos.put(2)
    simulador.pedidos.put(3)
    simulador.pedidos.put(4)
    simulador.pedidos.put(5)

def terminar_pedidos(simulador):
    # indicar fin de pedidos para los tres hilos
    simulador.pedidos.put(None)    
    simulador.pedidos.put(None)    
    simulador.pedidos.put(None) 
    

def tiempo_transcurrido(inicio):
    return time.time() - inicio


if __name__ == "__main__":
    inicio = time.time()
    simulador = SimuladorPedidos()
    print("\x1b[33m"+ "\n\tHay 3 empleados y  hay 5 pedidos" + "\x1b[32m")

    enviar_pedidos(simulador)
    
    terminar_pedidos(simulador)
    
    crear_hilos()

    print("\x1b[33m"+"\n\tTodos los pedidos han sido procesados.")
    print("\tTiempo transcurrido:", tiempo_transcurrido(inicio), "segundos"+ "\x1b[37m")

