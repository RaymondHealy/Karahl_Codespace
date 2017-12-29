#include "Arduino.h"
/*  Piezo_When_High.ino
 *  
 *  Raymond Healy
 *  
 *  A simple program to test functionality of a PIR Motion Detector.
 *  
 *  Components: An Active Piezo Buzzer
 *              A PIR Motion Sensor
 *              An Arduino, largely to act as a power supply
 *  
 *  Behaviour: When Motion is detected (PIR output is high), the Piezo 
 *  Buzzer's signaml pin will be set to <HIGH>
 */

const uint32_t motionIn = 7;
const uint32_t piezoOut = 13;

void setup() {
  pinMode(motionIn, INPUT);
  pinMode(piezoOut, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(piezoOut, digitalRead(motionIn));
}
