#include <LiquidCrystal.h>
#include "Arduino.h"
#include "Keypad.h"
//--------------------------------------Controlls---------------------------------------
const char leftButton = '4';
const char rightButton = '6';
const char upButton = '2';
const char downButton = '8';
//--------------------------------------------------------------------------------------

//-------------------------------------Keypad Setup-------------------------------------
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
Keypad * myKeypad;
//--------------------------------------------------------------------------------------

//--------------------------------------LCD Setup---------------------------------------
LiquidCrystal * screen;
String topLine = "<              >";
String bottomLine = "0";
//--------------------------------------------------------------------------------------

//------------------------------------Menu Variables------------------------------------
const uint8_t numMenus = 3;
const uint8_t maxSubMenuSelections[numMenus] = {10,7,5};

uint8_t menuSelected;
uint8_t subMenuSelections[numMenus];
//--------------------------------------------------------------------------------------

void setup() {
  // put your setup code here, to run once:
  menuSelected = 0;
  for (uint8_t i = 0; i<numMenus; i++){
    subMenuSelections[i] = 0;
  }
  
  myKeypad = new Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );
  screen = new LiquidCrystal(22, 23, 24, 25, 26, 27, 28);
  screen->begin(16, 2);
  screen->clear();
  screen->print(topLine);
  screen->setCursor(0, 1);
  screen->print(bottomLine);
}

void loop() {
  // put your main code here, to run repeatedly:

}
