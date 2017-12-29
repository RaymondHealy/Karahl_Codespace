#include "SimpleJoystick.h"

PushJoystick* stick;

void setup() {
  stick = new PushJoystick(5, 0, 7);
  stick->Calibrate();

  Serial.begin(115200);
  Serial.println("-------Starting Joystick Serial Terminal-------");
}

void loop() {

  Serial.print("\nX: ");
  Serial.println(stick->GetX());
  Serial.print("Y: ");
  Serial.println(stick->GetY());
  Serial.print("B: ");
  Serial.println(stick->GetSwitch());;

  delay(50);
}
