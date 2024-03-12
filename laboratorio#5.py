import serial #importa la bilboteca
import time   #importa la bilboteca

# Conecta al puerto serie del Arduino
arduino = serial.Serial('COM3', 9600)  # Crea un objeto de comunicación serial con la velocidad que se comunica

# Espera a que se establezca la conexión
time.sleep(2)


# Deja el LED encendido durante 10 segundos
arduino.write(b'H')      # Enciende el LED
time.sleep(10)           # Espera 10 segundos

# Apaga el LED al finalizar
arduino.write(b'L')      # Apaga el LED

# Cierra la conexión
arduino.close()
