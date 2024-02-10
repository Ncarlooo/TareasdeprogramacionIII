class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def esta_vacia(self):
        return len(self.items) == 0

def revertir_mitad_cola(cola):
    pila = []
    tamano_original = len(cola.items)
    mitad_tamano = tamano_original // 2

    # Pasar la primera mitad de la cola a la pila
    for _ in range(mitad_tamano):
        pila.append(cola.desencolar())

    # Pasar la pila de nuevo a la cola
    while pila:
        cola.encolar(pila.pop())

    # Pasar la segunda mitad de la cola a la pila y luego de nuevo a la cola
    for _ in range(tamano_original - mitad_tamano):
        cola.encolar(cola.desencolar())


mi_cola = Cola()

for i in range(1, 11):
    mi_cola.encolar(i)

print("Cola original:", mi_cola.items)

revertir_mitad_cola(mi_cola)

print("Cola con la mitad revertida:", mi_cola.items)
