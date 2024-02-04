#Carlo Sosa 0901-22-1106
print("Ingrese el primer numero")
numero1 = float(input())

print("Ingrese el segundo numero")
numero2= float(input())

def es_par(dato1, dato2): #Esto Calcula la suma de ambos y utiliza el operador módulo % para verificar si el resultado es divisible por 2 
    suma = dato1+dato2
    return suma % 2 == 0

resultado = es_par(numero1, numero2) #Aqui verifica si es par o no

print(f"La Suma de {numero1} y {numero2} es par? {resultado}") #La f sirve para poner varios valores en cadena