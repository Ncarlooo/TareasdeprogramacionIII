#include <AccelStepper.h>

#define IN1 8
#define IN2 9
#define IN3 10
#define IN4 11

AccelStepper stepper(AccelStepper::FULL4WIRE, IN1, IN3, IN2, IN4);
bool motorOn = false;

void setup() {
  Serial.begin(9600);
  stepper.setMaxSpeed(3000.0); // Aumenta la velocidad máxima
  stepper.setAcceleration(1500.0); // Aumenta la aceleración
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'E') {
      motorOn = true;
    } else if (command == 'A') {
      motorOn = false;
    } else if (motorOn) {
      if (command == 'R') {
        stepper.move(200);
      } else if (command == 'L') {
        stepper.move(-200);
      } else if (command >= '0' && command <= '9') {
        int speed = (command - '0') * 300; // Aumenta la velocidad
        stepper.setMaxSpeed(speed);
        stepper.setSpeed(speed);
      } else if (command == 'S') {
        while (Serial.available() == 0) {}
        int speed = Serial.parseInt();
        stepper.setMaxSpeed(speed * 30); // Aumenta la velocidad máxima
        stepper.setSpeed(speed * 30); // Aumenta la velocidad
      } else if (command == 'P') {
        while (Serial.available() == 0) {}
        int pos = Serial.parseInt();
        stepper.moveTo(pos * 200 / 360);
      }
    }
  }
  stepper.run();
}





