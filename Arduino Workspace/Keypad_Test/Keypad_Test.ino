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
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  
}

String buf = "0";

void loop() {
  // put your main code here, to run repeatedly:
  char key = keypad.getKey();
  if (key != NO_KEY) {
    Serial.print("Got:");
    Serial.println(key);
    if(key != '#' && key != '*'){
      buf += key;
    } else {
      buf = "0";
    }
    Serial.print("String: ");
    Serial.println(buf);
  }
  if(buf.toInt()%2 == 0){
    digitalWrite(13,HIGH);
    digitalWrite(12,LOW);
  } else {
    digitalWrite(12,HIGH);
    digitalWrite(13,LOW);
  }
}
