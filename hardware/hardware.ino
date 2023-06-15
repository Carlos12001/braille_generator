#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver myServo = Adafruit_PWMServoDriver();

#define DELAYSERVO 100
#define SERVOMIN 150
#define SERVOMAX 300
#define NUMSERVOS 12

String receivedString = "";
const int errorLed = 5;
const int nextButton = 8;
int buttonOld = 0;  
int buttonNew = 0;


void setup() {
  Serial.begin(9600);
  myServo.begin();
  myServo.setPWMFreq(60);
  pinMode(errorLed,OUTPUT);
  pinMode(nextButton,INPUT);
  delay(10);
  parseAndMoveServos("000000000000a");
  Serial.println("");
  digitalWrite(errorLed,LOW);
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
      digitalWrite(errorLed,LOW);
    }
    else{
      parseAndMoveServos("000000000000a");
      digitalWrite(errorLed,HIGH);
    }
    receivedString = "";
  }

  buttonNew = digitalRead(nextButton);
  if(buttonNew && !buttonOld){
    buttonOld = 1;
    digitalWrite(errorLed,HIGH);
    Serial.println("next");
    delay(1000);
    digitalWrite(errorLed,LOW);
    Serial.println("");
  }
  else if (buttonNew){
    Serial.println("");
    buttonOld = 1;
    delay(1000);
  }
  else{
    buttonOld = 0;
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


