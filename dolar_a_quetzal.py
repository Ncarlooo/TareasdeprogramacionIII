# Solicitar al usuario la cantidad de dólares a convertir
dolares = float(input("Ingresa la cantidad de dólares a convertir: "))

# Definir la tasa de cambio actual
tasa_cambio = 7.8  

# Calcular la cantidad en quetzales
quetzales = dolares * tasa_cambio

# Mostrar el resultado
print(f"{dolares} dólares son equivalentes a {quetzales} quetzales (con un cambio de {tasa_cambio}).")
