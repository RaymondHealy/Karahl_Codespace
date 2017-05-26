#include "Arduino.h"
#include "Keypad.h"

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};
byte rowPins[ROWS] = {8, 7, 6, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {4, 3, 2}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  randomSeed(analogRead(0));

  Serial.println("\n\n\n----------------------WELCOME TO THE GAME----------------------");
  Serial.println("\n                    ----Press # To Start----");
  Serial.println("                    ----Press * For Help----\n");
  Serial.println("---------------------------------------------------------------\n\n\n");

  char key = keypad.getKey();
  do {
    key = keypad.getKey();
  } while (key != '#' && key != '*');
  if (key == '*') {
    Serial.println("A simple equation ([1-12] [+,-,/,*] [1-12] = ?) will appear");
    Serial.println("on your screen. Enter your answer on the keypad and then press #");
    Serial.println("to submit your answer. Press * to clear what you've entered");
    Serial.println("Press # to begin");
    do {
      key = keypad.getKey();
    } while (key != '#');
  }
  Serial.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
}

String buf = "0";

void loop() {
  // put your main code here, to run repeatedly:
  //---------------------------------------------------------------Question Creation---------------------------------------------------------------
  //---------------------------------------------------------------Factor Generation---------------------------------------------------------------
  unsigned char operation = random(0, 3); //Pick Operation [(0, Addition), (1, Subtraction), (2, multiplication), (3, division)]
  unsigned char firstNumber = random(1, 12); //Pick First number [1-12]
  unsigned char secondNumber = random(1, 12); //pick the second number [1-12]
  unsigned char operatedNumber = 0;
  switch (operation) {
    case 2:
    case 3:
      operatedNumber = firstNumber*secondNumber;
      break;
    default:
      operatedNumber = firstNumber*secondNumber;
      break;
  }


  char key = keypad.getKey(); //Player Input
  if (key != NO_KEY) {
    if (key != '#' && key != '*') {
      buf += key;
    } else {
      buf = "0";
    }
    Serial.print("String: ");
    Serial.println(buf);
  }
}

