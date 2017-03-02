#include <Adafruit_NeoPixel.h>
#include <RGBConverter.h>
#include "Arduino.h"

//Enums-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enum ColorMode {
  kNone, kRed, kGreen, kBlue, kWhite, kRainbow, kOldCycle
};
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Functions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue) ;
void SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value);
void ColorModeProcess (ColorMode color);
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Variables---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
uint32_t modeIteration;

const float deltaHueForCycle = .5;
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


//Objects-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const uint32_t stripLength = 15;
const uint32_t pin = 6;
const uint32_t lastPixel = stripLength - 1;
Adafruit_NeoPixel* strip;
RGBConverter rgbConverter;
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void setup() {
  strip = new Adafruit_NeoPixel(stripLength, pin, NEO_GRB + NEO_KHZ800);
  modeIteration = 0;

  strip->begin();
  strip->show(); // Initialize all pixels to 'off'

}

void loop() {
  // put your main code here, to run repeatedly:
  ColorModeProcess(kGreen);
  strip->show();
  modeIteration++;
}


//Functions defined
void SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue) {
  for (uint32_t pixel = startPixel; pixel <= endPixel; pixel++) {
    strip->setPixelColor (pixel, red, green, blue);
  }
}

void SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value) {
  hue = hue / 360 - int(hue / 360); //Take hue from 0-360, turn it to 0-1, and remove any extra cycles around the wheel (remove the one place)

  byte rgb[3];
  rgbConverter.hsvToRgb(hue, saturation, value, rgb);
  SetRangeRGB(startPixel, endPixel, rgb[0], rgb[1], rgb[2]);
}

void ColorModeProcess (ColorMode color) {
  switch (color) {
    case kRed: {
        SetRangeRGB(0, lastPixel, 255, 0, 0);
      }
      break;
    case kGreen: {
        SetRangeRGB(0, lastPixel, 0, 255, 0);
      }
      break;
    case kBlue: {
        SetRangeRGB(0, lastPixel, 0, 0, 255);
      }
      break;
    case kWhite: {
        SetRangeRGB(0, lastPixel, 255, 255, 255);
      }
      break;
    case kRainbow: {
        float delta = 360 / strip->numPixels();
        float baseHue = modeIteration * deltaHueForCycle;

        for (uint32_t pixel = 0; pixel <= lastPixel; pixel++) {
          if (baseHue + deltaHueForCycle * pixel <= 360)
            SetRangeHSV(pixel, pixel, baseHue + deltaHueForCycle * pixel, 1, 1);
          else
            SetRangeHSV(pixel, pixel, deltaHueForCycle * pixel, 1, 1);
        }
        modeIteration = modeIteration % int(360 / deltaHueForCycle);
      }
      break;
    case kOldCycle: {
        SetRangeHSV(0, lastPixel, deltaHueForCycle * modeIteration, 1, 1);
        modeIteration = modeIteration % int(360 / deltaHueForCycle);
      }
      break;
    default: {
        SetRangeRGB(0, lastPixel, 0, 0, 0);
      }
      break;
  }
}
