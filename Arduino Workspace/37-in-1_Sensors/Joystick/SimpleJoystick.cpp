#include "SimpleJoystick.h"

Joystick::Joystick(uint32_t xIn, uint32_t yIn) {
  kXIn = xIn;
  kYIn = yIn;

  centerX = analogRead(kXIn);
  centerY = analogRead(kYIn);
}

void Joystick::Calibrate() {
  centerX = GetRawX();
  centerY = GetRawY();
}

float Joystick::GetX() {
  float toReturn = GetRawX(); //Initial cast of raw to float

  //-----------------------------------<MIN/MAX_CHECK>-----------------------------------//
  if (toReturn > kMaxX) { //If we have found a new max
    kMaxX = toReturn; //Change the recorded max
  }
  if (toReturn < kMinX) { //If we have found a new min
    kMinX = toReturn; //Change the recorded min
  }
  //---------------------------------<END MIN/MAX_CHECK>---------------------------------//

  //-----------------------------------<CAST_TO_RANGE>-----------------------------------//
  if (toReturn < centerX) { //If in the negative sector
    toReturn = fMap(toReturn, kMinX, centerX, -1, 0);
    //Cast the raw data [kMinX, centerX] to the expected range [-1, 0]
  }
  else { //Otherwise (if in the positive sector)
    toReturn = fMap(toReturn, centerX, kMaxX, 0, 1);
    //Map the raw data [centerX, kMaxX] to the expected range [0, 1]
  }
  //---------------------------------<END CAST_TO_RANGE>---------------------------------//

  return toReturn;
}

float Joystick::GetY() {
 float toReturn = GetRawY(); //Initial cast of raw to float

  //-----------------------------------<MIN/MAX_CHECK>-----------------------------------//
  if (toReturn > kMaxY) { //If we have found a new max
    kMaxY = toReturn; //Change the recorded max
  }
  if (toReturn < kMinY) { //If we have found a new min
    kMinY = toReturn; //Change the recorded min
  }
  //---------------------------------<END MIN/MAX_CHECK>---------------------------------//

  //-----------------------------------<CAST_TO_RANGE>-----------------------------------//
  if (toReturn < centerY) { //If in the negative sector
    toReturn = fMap(toReturn, kMinY, centerY, -1, 0);
    //Cast the raw data [kMinY, centerY] to the expected range [-1, 0]
  }
  else { //Otherwise (if in the positive sector)
    toReturn = fMap(toReturn, centerY, kMaxY, 0, 1);
    //Map the raw data [centerY, kMaxY] to the expected range [0, 1]
  }
  //---------------------------------<END CAST_TO_RANGE>---------------------------------//

  return toReturn;
}

PushJoystick::PushJoystick(uint32_t xIn, uint32_t yIn, uint32_t btnIn){
  stick = new Joystick(xIn, yIn);
  kBtnIn = btnIn;
  pinMode(kBtnIn, INPUT_PULLUP);
}

bool PushJoystick::GetSwitch(){
  return !bool(digitalRead(kBtnIn));
}


