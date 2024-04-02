// Arduino
const int buttonPin1 = 2;
const int buttonPin2 = 3;
const int buttonPin3 = 4;
const int buttonPin4 = 5;

const int ledPin1 = 6;
const int ledPin2 = 7;
const int ledPin3 = 8;
const int ledPin4 = 9;
const int ledPin5 = 10;
const int ledPin6 = 11;
const int ledPin7 = 12;
const int ledPin8 = 13;

bool previousButtonState1 = false;
bool previousButtonState2 = false;
bool previousButtonState3 = false;
bool previousButtonState4 = false;

void setup() {
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(buttonPin2, INPUT_PULLUP);
  pinMode(buttonPin3, INPUT_PULLUP);
  pinMode(buttonPin4, INPUT_PULLUP);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(ledPin5, OUTPUT);
  pinMode(ledPin6, OUTPUT);
  pinMode(ledPin7, OUTPUT);
  pinMode(ledPin8, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  bool buttonState1 = digitalRead(buttonPin1);
  bool buttonState2 = digitalRead(buttonPin2);
  bool buttonState3 = digitalRead(buttonPin3);
  bool buttonState4 = digitalRead(buttonPin4);

  if (buttonState1 != previousButtonState1) {
    if (buttonState1 == LOW) {
      digitalWrite(ledPin1, !digitalRead(ledPin1));
      digitalWrite(ledPin2, !digitalRead(ledPin2));
    }
    previousButtonState1 = buttonState1;
  }

  if (buttonState2 != previousButtonState2) {
    if (buttonState2 == LOW) {
      digitalWrite(ledPin3, !digitalRead(ledPin3));
      digitalWrite(ledPin4, !digitalRead(ledPin4));
    }
    previousButtonState2 = buttonState2;
  }

  if (buttonState3 != previousButtonState3) {
    if (buttonState3 == LOW) {
      digitalWrite(ledPin5, !digitalRead(ledPin5));
      digitalWrite(ledPin6, !digitalRead(ledPin6));
    }
    previousButtonState3 = buttonState3;
  }

  if (buttonState4 != previousButtonState4) {
    if (buttonState4 == LOW) {
      digitalWrite(ledPin7, !digitalRead(ledPin7));
      digitalWrite(ledPin8, !digitalRead(ledPin8));
    }
    previousButtonState4 = buttonState4;
  }

  if (Serial.available() > 0) {
    char ledNum = Serial.read();
    if (ledNum >= '1' && ledNum <= '8') {
      int ledPin = ledNum - '0' + 5;  // Convertir char a int y ajustar al pin correcto
      digitalWrite(ledPin, !digitalRead(ledPin)); // Alternar el estado del LED
    }
  }
}






