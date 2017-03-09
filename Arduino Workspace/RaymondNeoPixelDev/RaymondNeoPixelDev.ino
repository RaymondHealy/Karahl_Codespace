#include <Adafruit_NeoPixel.h>
#include <RGBConverter.h>
#include "Arduino.h"

//Enums-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enum ColorMode {
  kNone, kRed, kGreen, kBlue, kWhite, kRainbow, kOldCycle, kYellow, kQuasics, kBrown
};

enum BrightnessMode {
  kOff, kOn, kBreathing, kBlinking, kDashed, kRollIn, kRollOut, kRolling
};
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Functions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue) ;
void SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value);
void NeoPixelProcess ();
void SetColorMode (ColorMode color);
void SetBrightnessMode (BrightnessMode brightness);
void CycleBrightnessData (uint32_t numberOfSpaces);
void SetRangeBrightness(uint32_t first, uint32_t last, float brightnessLevel);
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Variables---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
uint32_t modeIteration;
float * brightnessData;

ColorMode colorMode = kRainbow;
BrightnessMode brightnessMode = kOn;

const float deltaHueForCycle = ;
const unsigned char brightness = 128;
const float loopSeconds = fabs(1);
const uint32_t delayMS = 0;

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


//Objects-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const uint32_t stripLength = 24;
const uint32_t pin = 6;
const uint32_t lastPixel = stripLength - 1;
Adafruit_NeoPixel* strip;
RGBConverter rgbConverter;
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

void setup() {
  strip = new Adafruit_NeoPixel(stripLength, pin, NEO_GRB + NEO_KHZ800);

  modeIteration = 0;

  brightnessData = new float [strip->numPixels()];
  for (uint32_t i = 0; i < lastPixel; i++) {
    brightnessData [i] = 1;
  }

  strip->setBrightness(brightness);
  strip->begin();
  strip->show();
}

void loop() {
  NeoPixelProcess();
  delay(delayMS);
}


//Functions defined
void SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue) {
  for (uint32_t pixel = startPixel; pixel <= endPixel; pixel++) {
    strip->setPixelColor (pixel, int(float(red)* brightnessData[pixel]), int(float(green)* brightnessData[pixel]), int(float(blue)* brightnessData[pixel]));
  }
}

void SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value) {
  hue = hue / 360 - int(hue / 360); //Take hue from 0-360, turn it to 0-1, and remove any extra cycles around the wheel (remove the one place)

  byte rgb[3];
  rgbConverter.hsvToRgb(hue, saturation, value, rgb);
  SetRangeRGB(startPixel, endPixel, rgb[0], rgb[1], rgb[2]);
}

void NeoPixelProcess () {
  switch (brightnessMode) {
    //kDashed
    case kBlinking: {
        if (millis() % int(loopSeconds * 1000 + .5) < (loopSeconds * 1000 + .5) / 2) {
          SetRangeBrightness(0, lastPixel, 0);
        } else {
          SetRangeBrightness(0, lastPixel, 1);
        }
      }
      break;
    case kRollIn: {
        static uint32_t pixelsFilled = 1;
        static uint32_t iteration = 0;
        SetRangeBrightness(0, strip->numPixels() - pixelsFilled, 0);
        SetRangeBrightness(iteration, iteration, 1);

        if (iteration >= strip->numPixels() - pixelsFilled) {
          iteration = 0;
          if (pixelsFilled >= strip->numPixels()) {
            brightnessMode = kOn;
            pixelsFilled = 1;
          } else {
            pixelsFilled++;
          }
        } else {
          iteration++;
        }
      }
      break;
    case kRollOut: {
        static uint32_t pixelsFilled = 1;
        static uint32_t iteration = 0;
        SetRangeBrightness(0, strip->numPixels() - pixelsFilled, 1);
        SetRangeBrightness(iteration, iteration, 0);

        if (iteration >= strip->numPixels() - pixelsFilled) {
          iteration = 0;
          if (pixelsFilled >= strip->numPixels()) {
            brightnessMode = kOff;
            pixelsFilled = 1;
          } else {
            pixelsFilled++;
          }
        } else {
          iteration++;
        }
        break;
      }
      break;
    case kRolling: {
        static uint32_t stage = 0;
        if (stage == 0) {
          static uint32_t pixelsFilled = 1;
          static uint32_t iteration = 0;
          SetRangeBrightness(0, strip->numPixels() - pixelsFilled, 0);
          SetRangeBrightness(iteration, iteration, 1);

          if (iteration >= strip->numPixels() - pixelsFilled) {
            iteration = 0;
            if (pixelsFilled >= strip->numPixels()) {
              stage = 1;
              pixelsFilled = 1;
            } else {
              pixelsFilled++;
            }
          } else {
            iteration++;
          }
        } else if (stage == 1) {
          static uint32_t pixelsFilled = 1;
          static uint32_t iteration = 0;
          SetRangeBrightness(0, strip->numPixels() - pixelsFilled, 1);
          SetRangeBrightness(iteration, iteration, 0);

          if (iteration >= strip->numPixels() - pixelsFilled) {
            iteration = 0;
            if (pixelsFilled >= strip->numPixels()) {
              stage = 0;
              pixelsFilled = 1;
            } else {
              pixelsFilled++;
            }
          } else {
            iteration++;
          }
        }
        break;
      }
      break;
    case kBreathing:
      {
        const float loopDurration = loopSeconds;
        const float halfDurration = loopDurration / 2;

        float timeLoop = float(millis() % int(loopDurration * 1000)) / 1000;
        float timeHalf = float(millis() % int(halfDurration * 1000)) / 1000;

        if (timeLoop <= halfDurration)
          SetRangeBrightness( 0, lastPixel, (timeHalf * timeHalf) / (halfDurration * halfDurration));
        else
          SetRangeBrightness( 0, lastPixel, ((halfDurration * halfDurration) - (timeHalf * timeHalf)) /
                        (halfDurration * halfDurration));
      }
      break;
    case kOff: {
        SetRangeBrightness (0, lastPixel, 0);
      }
      break;
    case kOn:
    default: {
        SetRangeBrightness (0, lastPixel, 1);
      }
      break;
  }
  switch (colorMode) {
    case kBrown:
        SetRangeRGB(0, lastPixel, 93, 21, 0);
        break;
    case kQuasics:
        SetRangeHSV(0, lastPixel, 120, 1, .62);
        break;
    case kYellow:
        SetRangeRGB(0, lastPixel, 255, 255, 0);
        break;
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
        float baseHue = modeIteration * deltaHueForCycle;

        while (baseHue < 0){
          baseHue = 360 - fabs(baseHue);
        }

        
        for (uint32_t pixel = 0; pixel <= lastPixel; pixel++) {
          SetRangeHSV(pixel, pixel, baseHue +  pixel * 360 / strip->numPixels(), 1, 1);
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

  modeIteration++;
  strip->show();
}

void SetColorMode (ColorMode color) {
  colorMode = color;
}

void CycleBrightnessData (uint32_t numberOfSpaces){
  
}

void SetBrightnessMode (BrightnessMode brightness) {
  brightnessMode = brightness;
}

void SetRangeBrightness(uint32_t first, uint32_t last, float brightnessLevel) {
  for (uint32_t pixel = first; pixel <= last; pixel++)
    brightnessData[pixel] = brightnessLevel;
}
