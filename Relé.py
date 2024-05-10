import tkinter as tk
import serial

# Configura el puerto
puerto = 'COM3'  # Cambia esto al puerto donde está conectado tu Arduino

# Crea una instancia de la conexión serie
ser = serial.Serial(puerto, 9600)

# Crea una ventana de tkinter
ventana = tk.Tk()
ventana.title("Control de relé")

# Estado del relé
estado_rele = False

# Función para manejar el botón
def toggle_rele():
    global estado_rele
    estado_rele = not estado_rele
    if estado_rele:
        ser.write(b'1')
    else:
        ser.write(b'0')

# Crea un botón
boton = tk.Button(ventana, text="Encender/Apagar", command=toggle_rele)
boton.pack()

# Inicia el bucle principal de tkinter
ventana.mainloop()






