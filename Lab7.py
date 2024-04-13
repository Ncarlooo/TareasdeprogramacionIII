import tkinter as tk
from tkinter import Canvas, Button
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Configurar el puerto serial (ajustar el puerto según tu sistema)
arduino_port = 'COM3'  # Reemplazar 'COM3' con tu puerto serial correcto
ser = serial.Serial(arduino_port, 9600)

# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Árbol")

# Canvas para dibujar el árbol (diagrama de flujo)
canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Coordenadas de los círculos (nodos del árbol)
node_positions = [
    (300, 50),   # Nodo 1 (Raíz)
    (200, 150),  # Nodo 2 (Hijo izquierdo)
    (400, 150)   # Nodo 3 (Hijo derecho)
]

# Lista de círculos (simulación de LEDs) en el árbol
leds = []

# Crear círculos (simulación de LEDs) en forma de diagrama de flujo (árbol)
for (x, y) in node_positions:
    circle = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, outline="black", fill="gray")
    leds.append(circle)

# Crear la figura y el eje para la visualización
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Establecer límites del eje x
ax.set_ylim(0, 0.5)  # Establecer límites del eje y para la barra (más pequeño)

# Barra inicial
bar = Rectangle((0, 0), 0, 0.2, facecolor='blue', alpha=0.7)  # Tamaño inicial más pequeño
ax.add_patch(bar)

# Función para procesar los datos del puerto serial
def process_serial_data():
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Recibido desde Arduino:", data)
        # Actualizar simulación de LEDs en la interfaz gráfica
        if data in ["Preorden", "Inorden", "Posorden"]:
            update_leds(data)
        else:
            try:
                # Actualizar la barra de la visualización
                if data:  # Verificar que la cadena no esté vacía
                    # Solo procesar el primer número en la línea
                    first_number = data.split()[0]
                    if first_number.isdigit():  # Verificar que la cadena pueda ser convertida a un entero
                        update_plot(int(first_number))
            except ValueError:
                print(f"Valor no válido recibido: {data}")

    root.after(100, process_serial_data)  # Reiniciar la escucha del puerto serial

# Función para actualizar simulación de LEDs según el tipo de recorrido
def update_leds(traversal_type):
    # Reiniciar todos los LEDs (círculos)
    for circle in leds:
        canvas.itemconfig(circle, fill="gray")
    
    # Encender LEDs según el tipo de recorrido
    if traversal_type == "Preorden":
        animate_leds([0, 1, 2])  # Índices de círculos en recorrido preorden
    elif traversal_type == "Inorden":
        animate_leds([1, 0, 2])  # Índices de círculos en recorrido inorden
    elif traversal_type == "Posorden":
        animate_leds([1, 2, 0])  # Índices de círculos en recorrido posorden

# Función para encender y apagar un círculo (LED virtual) en la interfaz gráfica
def toggle_led(circle_index, color):
    canvas.itemconfig(leds[circle_index], fill=color)

# Función para animar círculos (LEDs virtuales)
def animate_leds(order):
    if order:
        i = order.pop(0)
        toggle_led(i, "green")
        root.after(1000, toggle_led, i, "gray")  # Apagar el LED después de 1 segundo
        root.after(1500, animate_leds, order)  # Encender el siguiente LED después de medio segundo

# Funciones para simular recorridos de árbol
def simulate_preorden():
    ser.write(b'3')  # Enviar dato al Arduino para activar preorden
    animate_leds([0, 1, 2])  # Animar LEDs virtuales para preorden

def simulate_inorden():
    ser.write(b'2')  # Enviar dato al Arduino para activar inorden
    animate_leds([1, 0, 2])  # Animar LEDs virtuales para inorden

def simulate_posorden():
    ser.write(b'1')  # Enviar dato al Arduino para activar posorden
    animate_leds([1, 2, 0])  # Animar LEDs virtuales para posorden

# Crear botones virtuales para simular recorridos de árbol
btn_preorden = Button(root, text="Preorden", command=simulate_preorden)
btn_preorden.pack(side=tk.LEFT, padx=10)

btn_inorden = Button(root, text="Inorden", command=simulate_inorden)
btn_inorden.pack(side=tk.LEFT, padx=10)

btn_posorden = Button(root, text="Posorden", command=simulate_posorden)
btn_posorden.pack(side=tk.LEFT, padx=10)

# Función para actualizar el tamaño de la barra según el valor del potenciómetro
def update_plot(value):
    try:
        # Escalar el valor del potenciómetro a un tamaño entre 0 y 10
        size = float(value) / 1023 * 10
        # Actualizar el ancho de la barra
        bar.set_width(size)
        fig.canvas.draw()
    except ValueError:
        print(f"Valor no válido recibido: {value}")

# Función principal para recibir datos del puerto serial
def main():
    plt.ion()  # Habilitar modo interactivo para actualizar la gráfica en tiempo real
    
    while True:
        if ser.in_waiting > 0:
            # Leer valor del potenciómetro desde Arduino
            try:
                pot_value = ser.readline().decode().strip()
                if pot_value:  # Verificar que la cadena no esté vacía
                    # Solo procesar el primer número en la línea
                    first_number = pot_value.split()[0]
                    if first_number.isdigit():  # Verificar que la cadena pueda ser convertida a un entero
                        update_plot(int(first_number))
            except UnicodeDecodeError:
                print("Error al decodificar los datos recibidos.")

            # Mostrar la visualización
            plt.pause(0.01)  # Breve pausa para actualizar la gráfica

# Ejecutar la función principal
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ser.close()  # Cerrar puerto serial al salir

plt.ioff()  # Desactivar modo interactivo al finalizar
plt.show()  # Mostrar la visualización final

# Procesar datos del puerto serial en segundo plano (hilo)
root.after(100, process_serial_data)

# Ejecutar la ventana principal
root.mainloop()

