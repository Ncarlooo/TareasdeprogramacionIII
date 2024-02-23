class NodoArbol(object):
    def __init__(self, valor):
        self.val = valor
        self.izquierda = None
        self.derecha = None

def k_esimo_menor(raiz, k):
    pila = []
    while raiz or pila:
        while raiz:
            pila.append(raiz)
            raiz = raiz.izquierda
        raiz = pila.pop()
        k -= 1
        if k == 0:
            return raiz.val
        raiz = raiz.derecha

raiz = NodoArbol(8)
raiz.izquierda = NodoArbol(5)
raiz.derecha = NodoArbol(14)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(6)
raiz.izquierda.derecha.izquierda = NodoArbol(8)
raiz.izquierda.derecha.derecha = NodoArbol(7)
raiz.derecha.derecha = NodoArbol(24)
raiz.derecha.derecha.izquierda = NodoArbol(22)

print(k_esimo_menor(raiz, 2))
print(k_esimo_menor(raiz, 3))
