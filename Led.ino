void setup() {  //Se usa para iniciar configuraciones iniciales
  pinMode(13, OUTPUT); //indica en que pin esta y se usa el output para decir que va a ser una salida
  Serial.begin(9600); // Inicia la comunicación a la velocidad que se van a comunicar 
}

void loop() { //Aqui es donde inicia la accion principal del pograma 
  if (Serial.available() > 0) {  //Indica si hay puertos de salida para leerlos
    char command = Serial.read(); // Lee el comando enviado por Python
    if (command == 'H') {  //si el carácter leído es 'H', entonces se enciende el LED conectado al pin 13
      digitalWrite(13, HIGH); // Enciende el LED
    } else if (command == 'L') { //Si el carácter leído es 'L', entonces se apaga el LED
      digitalWrite(13, LOW);  // Apaga el LED
    }
  }
}

