#include <LiquidCrystal.h>

const uint8_t D7 = 13;
const uint8_t D6 = 12;
const uint8_t D5 = 11;
const uint8_t D4 = 10;
const uint8_t E  = 9;
const uint8_t RW = 8;
const uint8_t RS = 7;

const uint8_t width = 16;
const uint8_t height = 2;

LiquidCrystal* lcd;

void setup() {
  // put your setup code here, to run once:
  lcd = new LiquidCrystal(RS, RW, E, D4, D5, D6, D7);
  lcd->begin(width, height);
  lcd->clear();
  lcd->print("Karahl_1");
  lcd->setCursor(0,1);
  lcd->print("Raymond Healy");
}

void loop() {
  // put your main code here, to run repeatedly:

}
