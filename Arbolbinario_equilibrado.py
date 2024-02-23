class NodoArbolBinario(object):
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def crear_arbol_binario_desde_array(elementos):
    if not elementos:
        return None
    mitad = len(elementos) // 2
    nodo = NodoArbolBinario(elementos[mitad])
    nodo.izquierda = crear_arbol_binario_desde_array(elementos[:mitad])
    nodo.derecha = crear_arbol_binario_desde_array(elementos[mitad+1:])
    return nodo

def recorrido_preorden(nodo):
    if not nodo:
        return
    print(nodo.valor)
    recorrido_preorden(nodo.izquierda)
    recorrido_preorden(nodo.derecha)

resultado = crear_arbol_binario_desde_array([1,2,3,4,5,6,7])
recorrido_preorden(resultado)
