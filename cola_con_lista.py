class Cola:
    def __init__(self):
        self.items = []

    def vacia(self):
        return len(self.items) == 0

    def enqueue(self, elemento):  # Añade un elemento al final de la cola
        self.items.append(elemento)

    def dequeue(self):  #elminia y develve al primer elemento de la cola
        if not self.vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía\n")

    def front(self):
        if not self.vacia():
            return self.items[0]
        else:
            raise IndexError("La cola está vacía\n")

# Función para simular la atención en la fila
def atencion_fila():
    fila = Cola()

    fila.enqueue("Cliente 1")
    fila.enqueue("Cliente 2")
    fila.enqueue("Cliente 3")

    print("Fila actual:", fila.items)

    cliente_atendido = fila.dequeue()
    print("Cliente atendido:", cliente_atendido)

    proximo = fila.front()
    print("El próximo cliente es:", proximo)

    print("Fila después de la atención:", fila.items)

# Llamada a la función para simular la atención en la fila
atencion_fila()

        

    


        





