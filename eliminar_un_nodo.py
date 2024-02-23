class NodoArbol(object):
    def __init__(self, valor):
        self.val = valor
        self.izquierda = None
        self.derecha = None

def eliminar_nodo(raiz, clave):
    if not raiz:
        return raiz

    # Buscar el nodo en el subárbol izquierdo si la clave es menor que el valor de la raíz
    if raiz.val > clave:
        raiz.izquierda = eliminar_nodo(raiz.izquierda, clave)
    
    # Buscar el nodo en el subárbol derecho si la clave es mayor que el valor de la raíz
    elif raiz.val < clave:
        raiz.derecha = eliminar_nodo(raiz.derecha, clave)
    
    # Borrar el nodo si raiz.val == clave
    else:
        # Si el hijo derecho es nulo, la nueva raíz será el hijo izquierdo
        if not raiz.derecha:
            return raiz.izquierda
        # Si el hijo izquierdo es nulo, la nueva raíz será el hijo derecho
        elif not raiz.izquierda:
            return raiz.derecha
        # Si existen hijos izquierdo y derecho en el nodo,
        # reemplace su valor con el valor mínimo en el subárbol derecho.
        # Ahora elimina ese nodo mínimo en el subárbol derecho
        temp_valor = encontrar_minimo(raiz.derecha)
        raiz.val = temp_valor.val
        raiz.derecha = eliminar_nodo(raiz.derecha, temp_valor.val)

    return raiz

def encontrar_minimo(nodo):
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo

def recorrido_preorden(nodo):
    if not nodo:
        return
    print(nodo.val)
    recorrido_preorden(nodo.izquierda)
    recorrido_preorden(nodo.derecha)

raiz = NodoArbol(5)
raiz.izquierda = NodoArbol(3)
raiz.derecha = NodoArbol(6)
raiz.izquierda.izquierda = NodoArbol(2)
raiz.izquierda.derecha = NodoArbol(4)
raiz.izquierda.derecha.izquierda = NodoArbol(7)

print("Nodo original:")
recorrido_preorden(raiz)

resultado = eliminar_nodo(raiz, 4)
print("Después de borrar el nodo deseado:")
recorrido_preorden(resultado)
