#include <Wire.h>
#include <Adafruit_L3GD20.h>

Adafruit_L3GD20 gyro;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  if (!gyro.begin(gyro.L3DS20_RANGE_2000DPS)) {
    Serial.println("Oops ... unable to initialize the L3GD20. Check your wiring!");
    while (1);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  gyro.read();
  Serial.print("X: "); Serial.print((int)gyro.data.x);   Serial.print(" ");
  Serial.print("Y: "); Serial.print((int)gyro.data.y);   Serial.print(" ");
  Serial.print("Z: "); Serial.println((int)gyro.data.z); Serial.print(" ");
  delay(100);
}
