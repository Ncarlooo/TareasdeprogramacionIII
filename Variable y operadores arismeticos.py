#Carlo Sosa 0901-22-1106

#Aqui solicite que pida los datos, use el float para numeros enteros
print("Hola Bienvenido a la calculadora multiple, por favor escriba su primer numero: ")
dato1 = float(input())
dato2 = float(input("Ingrese el segundo numero :"))

#Aqui se realizan los calculos

suma = dato1+dato2
resta = dato1-dato2
multiplicacion = dato1*dato2
division = dato1/dato2

#se muestra los resultados

print("Sus resultaos son:")
print("Suma: ",suma)
print("resta: ",resta)
print("Multiplicacion: ",multiplicacion)
print(f"Division: {division:.2f}")           #Puse la f, :.2f para indicar que me lo de con dos decimales



