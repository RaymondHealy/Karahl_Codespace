#include <RTClib.h>

#include <Wire.h>

RTC_DS3231 rtc;

void setup() {
  // put your setup code here, to run once:
  rtc.begin();
  rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
}

void loop() {
  // put your main code here, to run repeatedly:

}
