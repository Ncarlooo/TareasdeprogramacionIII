class Pila:
    def __init__(self):  # Inicializa los atributos de la instancia
        self.items = []   # Esto es para poner los atributos de las clases que queremos agregar

    def estancia_vacia(self):
        return len(self.items) == 0  # Esta devolviendo el numero de elementos

    def push(self, elemento):
        self.items.append(elemento)  # Se agrega un elemento a la lista

    def pop(self):  # Eliminar el elemento de la posición indicada
        if not self.estancia_vacia():
            return self.items.pop()
        else:
            raise IndexError("El espacio está vacío\n")  # Raise se usa cuando el flujo de control se interrumpe

    def peek(self):  # Peek se usa para ver el elemento superior sin quitarlo de la fila
        if not self.estancia_vacia():
            return self.items[-1]
        else:
            raise IndexError("El espacio está vacío\n")

class Cola:
    def __init__(self):
        self.items = []

    def estancia_vacia(self):
        return len(self.items) == 0

    def enqueue(self, elemento):
        self.items.insert(0, elemento)

    def dequeue(self):
        if not self.estancia_vacia():
            return self.items.pop()
        else:
            raise IndexError("La cola está vacía")

    def front(self):
        if not self.estancia_vacia():
            return self.items[-1]
        else:
            raise IndexError("La cola está vacía")

# Se va a usar para invertir la fila y cola
def invertir_pila_cola_lista(lista):
    pila = Pila()
    cola = Cola()

    for elemento in lista:
        pila.push(elemento)  # Push nos permite agregar un número al final de la pila

    while not pila.estancia_vacia():
        cola.enqueue(pila.pop())  # Enqueue nos ayuda a agregar un número al final de la cola

    lista_invertida = []
    while not cola.estancia_vacia():
        lista_invertida.append(cola.dequeue())  # Append nos ayuda a agregar un número al final de la lista

    return lista_invertida

lista_original = [1, 2, 3, 4, 5]
lista_invertida = invertir_pila_cola_lista(lista_original)

print("Lista original\n", lista_original)
print("Lista invertida\n", lista_invertida)

        
    

    