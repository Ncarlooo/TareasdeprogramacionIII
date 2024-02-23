class NodoArbol(object):
    def __init__(self, valor):
        self.val = valor
        self.izquierda = None
        self.derecha = None

def encontrar_valor_mas_cercano(raiz, objetivo):
    if not raiz:
        return float('inf')
    
    a = raiz.val
    hijo = raiz.izquierda if objetivo < a else raiz.derecha
    
    if not hijo:
        return a
    
    b = encontrar_valor_mas_cercano(hijo, objetivo)
    return min((a, b), key=lambda x: abs(objetivo - x))

raiz = NodoArbol(8)
raiz.izquierda = NodoArbol(5)
raiz.derecha = NodoArbol(14)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(6)
raiz.izquierda.derecha.izquierda = NodoArbol(7)
raiz.derecha.derecha = NodoArbol(24)
raiz.derecha.derecha.izquierda = NodoArbol(22)

resultado = encontrar_valor_mas_cercano(raiz, 19)
print(resultado)
