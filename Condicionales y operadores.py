#carlo Sosa 0901-22-1106
print("Ingrese el numero deseado:")
dato1 = float(input())

def positivo_negativo(dato):  #Aqui estamos creando una funcion
    if dato > 0:
        return "El numero es positivo"
    elif dato < 0:
        return "El numero es negativo"
    else:
        return "El numero es cero"

    
#aqui estamos llamando a la funcion para que la aplique en nuestro dato
    
resultado = positivo_negativo(dato1)
print(resultado)
