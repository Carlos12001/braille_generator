# Braille Generator

Braille Generator is a Python script that converts text to braille. It can be used to generate braille for a single character, a word, or a sentence. It can also be used to generate braille for a text file.

## Hardware

The hardware use Arduino Uno, 12 servos, 2 push button and a breadboard. The servos are connected to the Arduino Uno as shown in the figure below.

SCL - Blanco
SDA - MORADO

Adafruit 16-Channel 12-bit PWM/Servo Driver

SCL - MAS EXTERNO PUERTO DIGITAL
SDL - EL SEGUNDO DESPUES DE SCL

https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all 
 
## IDE

The IDE is built with Electron Js, which gives it a modern look. Since the language is still being compiled in Python, it was necessary to stablish a connection using Flask in python and http fetchs from Javascript.

