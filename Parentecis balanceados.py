def balance(cadena):
    pila = []  # Sirve para rastrear todos los paréntesis

    # Se corrige el diccionario de mapeo
    mapeo = {')': '(', '}': '{', ']': '['}  # Verifica que los paréntesis estén balanceados

    for caracter in cadena:
        if caracter in mapeo:  # Verifica si es un paréntesis de cierre
            superior = pila.pop() if pila else '#'  # Verifica que el paréntesis coincida con la pila

            if mapeo[caracter] != superior:  # Verifica que coincida con el paréntesis de apertura
                return False
        else:
            pila.append(caracter)  #agrega un parentesis a la apertura

    return not pila  #la función devuelve True si la pila está vacía (todos los paréntesis están balanceados) y False si la pila no está vacía (los paréntesis no están balanceados).

cadena = "{[()]}"
resultado = balance(cadena)

if resultado:
    print("Los resultados están balanceados\n")
else:
    print("Los paréntesis no están balanceados\n")



