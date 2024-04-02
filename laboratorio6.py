# Python
import tkinter as tk
import serial
import time

# Configura el puerto serial
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Espera a que se establezca la conexión

def toggle_led(led):
    arduino.write(bytes(str(led), 'utf-8'))

# Función para crear un botón que controla un LED específico
def create_led_button(frame, led):
    button = tk.Button(frame, text=f"LED {led}", command=lambda: toggle_led(led))
    button.grid(row=0, column=led - 1, padx=5, pady=5)

# Crear ventana principal
root = tk.Tk()
root.title("Control de LED")

# Crear un marco para los botones
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Crear botones para cada LED
for led in range(1, 9):
    create_led_button(button_frame, led)

root.mainloop()


