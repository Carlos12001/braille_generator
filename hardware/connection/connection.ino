
const int pinLed11 = 11;
const int pinLed12 = 12;
const int pinLed13 = 13;
int changeSomething = 1;
int option;
String receivedString;

void setup() {
  Serial.begin(9600);
  pinMode(pinLed11, OUTPUT);
  pinMode(pinLed12, OUTPUT);
  pinMode(pinLed13, OUTPUT);
}

void loop() {

  while (Serial.available()) {  
    delay(10);  
    char c = Serial.read(); 
    receivedString += c;
  }

  if (receivedString.length() > 0) {
    Serial.println(receivedString);  
    changeSomething = 1;


    if(receivedString == "BLANCO"){
      digitalWrite(pinLed11,HIGH);
      delay(5000);
      digitalWrite(pinLed11,LOW);
      delay(2000);
    }
    else if(receivedString == "VERDE"){
      digitalWrite(pinLed12,HIGH);
      delay(5000);
      digitalWrite(pinLed12,LOW);
      delay(2000);
    } else {
        digitalWrite(pinLed13,HIGH);
      delay(5000);
      digitalWrite(pinLed13,LOW);
      delay(2000);
    }
    receivedString = "";  
  }

  if(changeSomething){
    changeSomething = 0;
    Serial.println("Hi Python!");
  }
}
