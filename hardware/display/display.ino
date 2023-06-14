#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Dirección I2C y dimensiones del LCD
String message = "000000001110b";
int counter = 0;
void setup() {
  lcd.begin(16, 2);
  lcd.setBacklight(255);  // Establecer el brillo máximo (0-255)
  Serial.begin(9600);
}

void loop() {
  // Ejemplo de uso: Mostrar el carácter que inserte
  if(!counter){
    CaracterI(message);
    counter++;
  }
  else {
    
  }
}



// á
byte a2[8] = {
  B00010,
  B00100,
  B01111,
  B00001,
  B11111,
  B10001,
  B10001,
  B11111
};

// Á
byte aa2[8] = {
  B00010,
  B00100,
  B01110,
  B10001,
  B10001,
  B11111,
  B10001,
  B10001
};

// é
byte e2[8] = {
  B00010,
  B00100,
  B00000,
  B11111,
  B10001,
  B11111,
  B10000,
  B01110
};

// É
byte ee2[8] = {
  B00010,
  B00100,
  B00000,
  B11111,
  B10000,
  B11110,
  B10000,
  B11111
};

// í
byte i2[8] = {
  B00010,
  B00100,
  B00000,
  B01100,
  B00100,
  B00100,
  B00100,
  B01110
};

// Í
byte ii2[8] = {
  B00010,
  B00100,
  B00000,
  B01110,
  B00100,
  B00100,
  B00100,
  B01110
};

// ó
byte o2[8] = {
  B00010,
  B00100,
  B11111,
  B10001,
  B10001,
  B10001,
  B10001,
  B11111
};

// Ó
byte oo2[8] = {
  B00010,
  B00100,
  B11111,
  B10001,
  B10001,
  B10001,
  B10001,
  B11111
};

// ú
byte u2[8] = {
  B00001,
  B00010,
  B00000,
  B10001,
  B10001,
  B10001,
  B10001,
  B01110
};

// Ú
byte uu2[8] = {
  B00001,
  B00010,
  B10001,
  B10001,
  B10001,
  B10001,
  B10001,
  B11111
};


// ñ
byte n2[8] = {
  B01010,
  B00101,
  B10000,
  B11111,
  B10001,
  B10001,
  B10001,
  B10001
};

// Ñ
byte nn2[8] = {
  B01010,
  B00101,
  B00000,
  B10001,
  B11001,
  B10101,
  B10011,
  B10001
};

// u con dieresis
byte pp2[8] = {
  B00000,
  B01010,
  B00000,
  B10001,
  B10001,
  B10001,
  B10001,
  B01110
};


// U con dieresis
byte pe2[8] = {
  B01010,
  B00000,
  B10001,
  B10001,
  B10001,
  B10001,
  B10001,
  B11111
};
// signo de excalmaci[on
byte ll2[8] = {
  B00000,
  B00100,
  B00000,
  B00100,
  B00100,
  B00100,
  B00100,
  B00000
};
// signo de pregunta
byte xx2[8] = {
  B00100,
  B00000,
  B00100,
  B00100,
  B01000,
  B10001,
  B10001,
  B01110
};




void CaracterI(String brailleChar) {
  // Limpiar el display
  
  char ultimoElemento = brailleChar.charAt(brailleChar.length() - 1);
  lcd.setCursor(7, 0);
  if (ultimoElemento == ' ') {
    if (brailleChar.equals("000000011011 ")) {
      // é
      lcd.createChar(1, e2);
      lcd.setCursor(5, 0);
      lcd.write(1);
      
    } else if (brailleChar.equals("000000010010 ")) {
      // í
      lcd.createChar(2, i2);
      lcd.setCursor(5, 0);
      lcd.write(2);
      
    }else if (brailleChar.equals("000000101101 ")) {
      // U con dieresis
      lcd.createChar(2, pp2);
      lcd.setCursor(5, 0);
      lcd.write(2);
    
    } else if (brailleChar.equals("000000010011 ")) {
      // ó
      lcd.createChar(3, o2);
      lcd.setCursor(5, 0);
      lcd.write(3);

    } else if (brailleChar.equals("010001010011 ")) {
      // u co dieresis
      lcd.createChar(3, pe2);
      lcd.setCursor(5, 0);
      lcd.write(3);

     }else if (brailleChar.equals("000000001110 ")) {
      // Signode pregunta 
      lcd.createChar(3, xx2);
      lcd.setCursor(5, 0);
      lcd.write(3);
      
     }else if (brailleChar.equals("000000001001 ")) {
      // Signo de interorgaci[on contrario a !
      lcd.createChar(3, xx2);
      lcd.setCursor(5, 0);
      lcd.write(3);
    } else if (brailleChar.equals("000000111101 ")) {
      // ññ¿
      lcd.createChar(4, n2);
      lcd.setCursor(5, 0);
      lcd.write(4);
    } else if (brailleChar.equals("000000100000 ")) {
      // á
      lcd.createChar(2, a2);
      lcd.setCursor(5, 0);
      lcd.write(2);
    } else if (brailleChar.equals("010001011011 ")) {
      // É
      lcd.createChar(1, ee2);
      lcd.setCursor(5, 0);
      lcd.write(1);
    } else if (brailleChar.equals("010001010010 ")) {
      // Í
      lcd.createChar(2, ii2);
      lcd.setCursor(5, 0);
      lcd.write(2);
    } else if (brailleChar.equals("010001010011 ")) {
      // Ó
      lcd.createChar(3, oo2);
      lcd.setCursor(5, 0);
      lcd.write(3);
    } else if (brailleChar.equals("010001111101 ")) {
      // Ñ
      lcd.createChar(4, nn2);
      lcd.setCursor(5, 0);
      lcd.write(4);
    } else if (brailleChar.equals("010001100000 ")) {
      // Á
      lcd.createChar(2, aa2);
      lcd.setCursor(5, 0);
      lcd.write(2);
    }
    
    else {
      lcd.setCursor(0, 0);
      lcd.print("error de caracter");
    }
  }else{
    lcd.print(ultimoElemento);
   }
   
  
}