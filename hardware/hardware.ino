#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver myServo = Adafruit_PWMServoDriver();

#define DELAYSERVO 100
#define SERVOMIN 150
#define SERVOMAX 300
#define NUMSERVOS 12

int changeSomething = 1;
const int errorLed = 5;
String receivedString = "";

void setup() {
  Serial.begin(9600);
  myServo.begin();
  myServo.setPWMFreq(60);
  pinMode(errorLed, OUTPUT);
  delay(10);
  parseAndMoveServos("000000000000a");
  digitalWrite(errorLed,LOW);
  // Serial.println("listo"); 
}

void loop() {
  while (Serial.available()) {  
    delay(10);  
    char c = Serial.read(); 
    receivedString += c;
  }

  if (receivedString.length()!=0) {
    if (isValidInput(receivedString)) {
      parseAndMoveServos(receivedString);
      changeSomething = 1;
      digitalWrite(errorLed,LOW);
      //imprima(receivedString)
    }
    else{
      parseAndMoveServos("000000000000a");
      digitalWrite(errorLed,HIGH);
    }
    receivedString = "";
  }

  if(changeSomething){
    changeSomething = 0;
    Serial.println("Hi Python!");
  }
}

void parseAndMoveServos(String input) {
  int targetPos;
  for(int i = 0; i < NUMSERVOS; i++) {
    targetPos = (input.charAt(i) == '0') ? SERVOMIN : SERVOMAX;
    myServo.setPWM(i, 0, targetPos); 
    delay(DELAYSERVO);
  }
}

bool isValidInput(String input) {
  if (input.length() != NUMSERVOS + 1) {
    return false;
  }

  for (int i = 0; i < NUMSERVOS; i++) {
    char c = input.charAt(i);
    if (c != '0' && c != '1') {
      return false;
    }
  }

  return true;
}


