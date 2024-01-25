import cmath  # Importar el módulo de números complejos para manejar raíces cuadradas de números negativos

# Solicitar al usuario los coeficientes de la ecuación cuadrática
a = float(input("Ingresa el coeficiente 'a': "))
b = float(input("Ingresa el coeficiente 'b': "))
c = float(input("Ingresa el coeficiente 'c': "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Calcular las soluciones
solucion_1 = (-b + cmath.sqrt(discriminante)) / (2*a)
solucion_2 = (-b - cmath.sqrt(discriminante)) / (2*a)

# Mostrar el resultado
print(f"Las soluciones de la ecuación cuadrática son:")
print(f"Solución 1: {solucion_1}")
print(f"Solución 2: {solucion_2}")
