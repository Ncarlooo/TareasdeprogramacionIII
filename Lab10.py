import serial
import tkinter as tk
import time

arduino = serial.Serial('COM3', 9600)

def send_command(command):
    arduino.write(command.encode())
    time.sleep(0.5)  # Agrega un retraso más largo

def set_speed(value):
    command = f"S{int(value)}\n"
    arduino.write(command.encode())
    time.sleep(0.5)  # Agrega un retraso después de ajustar la velocidad

def set_position(degrees):
    arduino.write('P'.encode())
    arduino.write((str(degrees) + '\n').encode())
    time.sleep(0.5)  # Agrega un retraso después de ajustar la posición

root = tk.Tk()
root.title("Control de Motor Stepper")

btn_on = tk.Button(root, text="Encender", command=lambda: send_command('E'))  # Botón para encender el motor
btn_on.pack()

btn_off = tk.Button(root, text="Apagar", command=lambda: send_command('A'))  # Botón para apagar el motor
btn_off.pack()

btn_right = tk.Button(root, text="Derecha", command=lambda: send_command('R'))
btn_right.pack()

btn_left = tk.Button(root, text="Izquierda", command=lambda: send_command('L'))
btn_left.pack()

scale_speed = tk.Scale(root, from_=0, to=300, orient=tk.HORIZONTAL, label="Velocidad")  # Aumenta el rango a 0-300
scale_speed.pack()
scale_speed.bind("<Motion>", lambda event: set_speed(scale_speed.get()))

btn_90 = tk.Button(root, text="90 grados", command=lambda: set_position(90))
btn_90.pack()

btn_180 = tk.Button(root, text="180 grados", command=lambda: set_position(180))
btn_180.pack()

root.mainloop()




