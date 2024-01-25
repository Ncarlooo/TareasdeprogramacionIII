# Se le pide al usuario que ponga la hora con minutos y segundos.
hora = int(input("Ingresa la hora (0-23): "))
minutos = int(input("Ingresa los minutos (0-59): "))
segundos = int(input("Ingresa los segundos (0-59): "))

# formula
segundos_totales = hora * 3600 + minutos * 60 + segundos

# Enseñar resultados
print(f"Han pasado {segundos_totales} segundos desde la medianoche.")
