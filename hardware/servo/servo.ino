#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver myServo = Adafruit_PWMServoDriver();

#define DELAYSERVO 100
#define SERVOMIN 150
#define SERVOMAX 300


uint8_t numberOfServos = 12;
uint8_t servonum = 0;

void setup() {
  Serial.begin(9600);
  myServo.begin();
  myServo.setPWMFreq(60);
  delay(10);
}

void loop() {
  raiseServo(servonum);
  lowerServo(servonum);
  
  servonum ++;
  if (servonum > numberOfServos-1) 
    servonum = 0;
}

void raiseServo(uint8_t servoNum){
  myServo.setPWM(servonum, 0, SERVOMAX);  // mover el servo a la posición máxima
  delay(DELAYSERVO);
}

void lowerServo(uint8_t servoNum){
  myServo.setPWM(servonum, 0, SERVOMIN);  // mover el servo a la posición mínima
  delay(DELAYSERVO);
}
