#include <Servo.h>

Servo servoLeft;          // Define left servo
Servo servoRight;         // Define right servo

void setup() { 
  servoLeft.attach(12);  // Set left servo to digital pin 10
  servoRight.attach(13);  // Set right servo to digital pin 9
} 

void loop() {            // Loop through motion tests
  turnLeft();             // Example: move forward
  delay(700);           // Wait 2000 milliseconds (2 seconds)
  reverse();
  delay(1000);
  forward();
  delay(200);
  turnRight();
  delay(700);
  turnLeft();
  delay(700);
  turnRight();
  delay(2000);
}

// Motion routines for forward, reverse, turns, and stop
void forward() {
  servoLeft.write(0);
  servoRight.write(180);
}

void reverse() {
  servoLeft.write(180);
  servoRight.write(0);
}

void turnRight() {
  servoLeft.write(180);
  servoRight.write(180);
}
void turnLeft() {
  servoLeft.write(0);
  servoRight.write(0);
}

void stopRobot() {
  servoLeft.write(90);
  servoRight.write(90);
}
