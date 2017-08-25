#include <Servo.h>

Servo servoLeft;      
Servo servoRight;

void setup()                                 // Built-in initialization block
{
  servoLeft.attach(13);
  servoRight.attach(12); 
  tone(4, 3000, 5000);                       // Play tone for 1 second
  delay(1000);                               // Delay to finish tone
  pinMode(7, INPUT);                         // Set right whisker pin to input
  pinMode(5, INPUT);                         // Set left whisker pin to input  

  Serial.begin(9600);                        // Set data rate to 9600 bps
}  
 
void loop()                                  // Main loop auto-repeats
{                                            
  byte wLeft = digitalRead(5);               // Copy left result to wLeft  
  byte wRight = digitalRead(7);              // Copy right result to wRight

  Serial.print(wLeft);                       // Display left whisker state
  Serial.println(wRight);                    // Display right whisker state

  delay(50);
  if (wLeft==0){
    tone(4,100,1000);
    reverse();
    delay(500);
    turnRight();
    delay(400);
  }
  else {
    forward();
    
  }

  if(wRight==0){
    tone(4,100, 1000); 
    reverse();
    delay(500);
    turnLeft();
    delay(400);
 }
   else {
     forward();
   
  }
  
 if (wLeft==0 and wRight==0){ 
   tone(4, 100, 1000); 
   reverse();
   delay(500);
   turnRight();
   delay(400);
 }
  else {
  forward();
 }
}
void forward() {
  servoLeft.write(180);
  servoRight.write(0);

}
void reverse() {
  servoLeft.write(0);
  servoRight.write(180);
}

void turnRight(){
 servoLeft.write(180);
 servoRight.write(180);
}
 void turnLeft() {
  servoLeft.write(0);
  servoRight.write(0);
 
  

