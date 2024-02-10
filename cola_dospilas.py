class ColaConDosPilas:
    def __init__(self):
        self.entrada = []
        self.salida = []

    def enqueue(self, elemento):
        self.entrada.append(elemento)

    def dequeue(self):
        if not self.salida:  # Si la pila de salida está vacía, transfiere elementos desde la pila de entrada
            while self.entrada:
                self.salida.append(self.entrada.pop())

        if not self.salida:  # Si ambas pilas están vacías, la cola también está vacía
            raise IndexError("La cola está vacía")

        return self.salida.pop()


cola = ColaConDosPilas()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(cola.dequeue())  # Imprime 1
print(cola.dequeue())  # Imprime 2
print(cola.dequeue())  # Imprime 3
     
