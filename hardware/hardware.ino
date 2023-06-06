#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver myServo = Adafruit_PWMServoDriver();

#define DELAYSERVO 100
#define SERVOMIN 150
#define SERVOMAX 300
#define NUMSERVOS 12

void setup() {
  Serial.begin(9600);
  myServo.begin();
  myServo.setPWMFreq(60);
  delay(10);
  parseAndMoveServos("000000000000a");
}

void loop() {
  delay(2000);
  parseAndMoveServos("100000000000a");
  delay(2000);
  parseAndMoveServos("010001000000a");
  delay(2000);
  parseAndMoveServos("000000000000a");
  delay(2000);
}

void parseAndMoveServos(String input) {
  int targetPos;
  for(int i = 0; i < NUMSERVOS; i++) {
    targetPos = (input.charAt(i) == '0') ? SERVOMIN : SERVOMAX;
    myServo.setPWM(i, 0, targetPos); 
    delay(DELAYSERVO);
  }

  // Imprimir el último caracter
  Serial.println(input.charAt(input.length()-1));
}

