#include <AFMotor.h>
#include <Servo.h> 

AF_DCMotor motor(3);

Servo servo1;

void setup() {
  Serial.begin(9600);           
  servo1.attach(9);
  motor.setSpeed(200);
}

int i;

void loop() {
  motor.run(FORWARD);
  for (i = 0; i <= 180; i += 1) {
    servo1.write(i);
    delay(15);
 }

  delay(1000);

  motor.run(BACKWARD);
  for (i=180; i>=0; i-=1) {
    servo1.write(i);
    delay(15);
 }
 
 delay(1000);
 motor.run(RELEASE);
}
 
