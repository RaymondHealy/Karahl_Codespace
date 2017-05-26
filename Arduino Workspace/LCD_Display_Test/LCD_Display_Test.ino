#include <LiquidCrystal.h>
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
byte rowPins[ROWS] = {52, 50, 48, 46}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {44, 42, 40}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

LiquidCrystal * screen;

String topLine = "";
String input = "0";
void setup() {
  // put your setup code here, to run once:
  screen = new LiquidCrystal(22, 23, 24, 25, 26, 27, 28);
  screen->begin(16, 2);
  screen->clear();
  screen->print(topLine);
  screen->setCursor(0, 1);
  screen->print(input);
}

void loop() {
  char key = keypad.getKey();
  if (key != NO_KEY) {
    if (key != '*' && key != '#') {
      if (input.toInt() != 0) {
        input += key;
        screen->print(key);

      } else {
        screen->setCursor(0, 1);
        screen->print(key);
        input = key;
      }
    } else if (key = '*') {
      input = "0";
      screen->clear();
      screen->print(topLine);
      screen->setCursor(0, 1);
      screen->print(input);
    } else {
      input = "0";
      screen->clear();
      screen->print(topLine);
      screen->setCursor(0, 1);
      screen->print(input);
    }



  }
  // put your main code here, to run repeatedly:



}
