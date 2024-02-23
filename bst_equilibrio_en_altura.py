class NodoArbol(object):
    def __init__(self, valor):
        self.val = valor
        self.izquierda = None
        self.derecha = None

def convertir_array_a_bst(nums):
    if not nums:
        return None
    mitad = len(nums) // 2
    nodo = NodoArbol(nums[mitad])
    nodo.izquierda = convertir_array_a_bst(nums[:mitad])
    nodo.derecha = convertir_array_a_bst(nums[mitad+1:])
    return nodo

def recorrido_preorden(nodo):
    if not nodo:
        return
    print(nodo.val)
    recorrido_preorden(nodo.izquierda)
    recorrido_preorden(nodo.derecha)

array_nums = [1, 2, 3, 4, 5, 6, 7]
print("Array original:")
print(array_nums)
resultado = convertir_array_a_bst(array_nums)
print("\nÁrbol balanceado:")
recorrido_preorden(resultado)
