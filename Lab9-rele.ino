int rele = 7;

void setup() {
  pinMode(rele, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '1') {
      digitalWrite(rele, HIGH);
    } else if (c == '0') {
      digitalWrite(rele, LOW);
    }
  }
}



























