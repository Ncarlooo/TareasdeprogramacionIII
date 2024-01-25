#carlo Sosa 0901-22-1106

# Se escribe la funcion para convertir de celsius a fahrenheit y se introduce la formula.
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Se escribe la funcion para convertir defahrenheit a celsius y se introduce la formula.
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# esto es para que el usuario ponga que opcion desea 
opcion = input("¿Deseas convertir de Celsius a Fahrenheit (C) o de Fahrenheit a Celsius (F)? ").upper()

if opcion == 'C':
    # Convertir de Celsius a Fahrenheit
    temperatura_celsius = float(input("Ingresa la temperatura en Celsius: "))
    temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
    print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")
    
elif opcion == 'F':
    # Convertir de Fahrenheit a Celsius
    temperatura_fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
    print(f"{temperatura_fahrenheit} grados Fahrenheit son {temperatura_celsius} grados Celsius.")
    
else:      #esto es por si el usuario no escribe ninguna de las dos opciones.
    print("Opción no válida. Por favor, ingresa 'C' o 'F' para seleccionar la conversión.")
