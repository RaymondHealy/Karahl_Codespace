#include <WiiChuck.h>
#include <Wire.h>

Nunchuck nunchuck(SDA, SCL);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  nunchuck.begin();

  nunchuck.addMap(new Nunchuck::joyX(5, 200, 128, 10));
  nunchuck.addMap(new Nunchuck::joyY(6, 200, 128, 10));
}

void loop() {
  // put your main code here, to run repeatedly:
  nunchuck.readData();
  int x = map(nunchuck.getJoyX() - 128, -100, 100, -50, 50) + .5;
  int y = map(nunchuck.getJoyY() - 128, -100, 100, -50, 50) + .5;

  Serial.print("Coordinates: ( ");
  if (x >= 0) {
    Serial.print('0');
  } else {
    Serial.print('-');
    x = abs(x);
  }
  if (abs(x) < 10) {
    Serial.print('0');
  }
  Serial.print(x);
  Serial.print(" , ");

  if (y >= 0) {
    Serial.print('0');
  } else {
    Serial.print('-');
    y = abs(y);
  }
  
  if (abs(y) < 10) {
    Serial.print('0');
  }
  Serial.print(y);
  Serial.print(" )\n");
  delay(0);
}
