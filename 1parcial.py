#carlo Sosa 0901-22-1106
def revertir_lista(lista):
    pila = [ ]
    for elemento in lista:
        pila.append(elemento)
    lista_revertida = []
    while pila:
       lista_revertida.append(pila.pop())
    return lista_revertida


lista_original = [ 1,2,3,4,5]
lista_revertida = [1+2+3+4+5]

print(lista_original,"\n")
print(lista_revertida, "es la suma de todas las listas" "\n")