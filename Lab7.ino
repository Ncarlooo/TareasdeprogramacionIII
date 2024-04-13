const int ledPin1 = 6;
const int ledPin2 = 7;
const int ledPin3 = 8;
const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int buttonPin3 = 4;
const int potPin = A3;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);

  if (digitalRead(buttonPin1) == LOW) {
    // Preorden: Rojo, Verde, Azul
    digitalWrite(ledPin1, HIGH);
    delay(500);
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, HIGH);
    delay(500);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, HIGH);
    delay(500);
    digitalWrite(ledPin3, LOW);
    Serial.println(1);  // Enviar '1' a Python para indicar preorden
  } else if (digitalRead(buttonPin2) == LOW) {
    // Inorden: Verde, Rojo, Azul
    digitalWrite(ledPin2, HIGH);
    delay(500);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin1, HIGH);
    delay(500);
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin3, HIGH);
    delay(500);
    digitalWrite(ledPin3, LOW);
    Serial.println(2);  // Enviar '2' a Python para indicar inorden
  } else if (digitalRead(buttonPin3) == LOW) {
    // Postorden: Verde, Azul, Rojo
    digitalWrite(ledPin2, HIGH);
    delay(500);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, HIGH);
    delay(500);
    digitalWrite(ledPin3, LOW);
    digitalWrite(ledPin1, HIGH);
    delay(500);
    digitalWrite(ledPin1, LOW);
    Serial.println(3);  // Enviar '3' a Python para indicar postorden
  } else {
    // Apagar todos los LEDs si no se presiona ningún botón
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
  }
}






