class NodoArbol(object):
    def __init__(self, valor):
        self.val = valor
        self.izquierda = None
        self.derecha = None

def es_arbol_busqueda_binaria(raiz):
    pila = []
    previo = None

    while raiz or pila:
        while raiz:
            pila.append(raiz)
            raiz = raiz.izquierda
        raiz = pila.pop()
        if previo and raiz.val <= previo.val:
            return False
        previo = raiz
        raiz = raiz.derecha

    return True  

arbol1 = NodoArbol(2)
arbol1.izquierda = NodoArbol(1)
arbol1.derecha = NodoArbol(3)

resultado1 = es_arbol_busqueda_binaria(arbol1)
print(resultado1)

arbol2 = NodoArbol(1)
arbol2.izquierda = NodoArbol(2)
arbol2.derecha = NodoArbol(3)

resultado2 = es_arbol_busqueda_binaria(arbol2)
print(resultado2)
