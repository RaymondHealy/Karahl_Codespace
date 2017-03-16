#include "NeoPixelController.h"
NeoPixelController::NeoPixelController(uint32_t pin, float loopSecondsIn, uint8_t brightness, uint32_t stripLength) {
  strip = new Adafruit_NeoPixel(stripLength, pin, NEO_GRB + NEO_KHZ800);

  modeIteration = 0;
  colorInitialized = 0;
  colorMode = kNone;
  brightnessMode = kOff;
  loopSeconds = fabs(loopSecondsIn);

  brightnessData = new float [strip->numPixels()];
  for (uint32_t i = 0; i < strip->numPixels() - 1; i++) {
    brightnessData [i] = 1;
  }

  universalBrightness = float(brightness) / 255;

  strip->setBrightness(255);
  strip->begin();
  strip->show();
}

void NeoPixelController::NeoPixelProcess () {
  switch (brightnessMode) {
    case kDashed: {
        if (pixelsPerSegment < strip->numPixels()) {
          if (!modeInitialized) {
            static int numberOfSegments = strip->numPixels() / pixelsPerSegment;
            for (int i = 0; i < numberOfSegments; i++) {
              if (i * pixelsPerSegment + pixelsPerSegment / 2 - 1 < strip->numPixels()) {
                SetRangeBrightness(i * pixelsPerSegment, i * pixelsPerSegment + pixelsPerSegment / 2 - 1, 1);
              } else {
                SetRangeBrightness(i * pixelsPerSegment, strip->numPixels() - 1, 1);
              }
              if (i * pixelsPerSegment + pixelsPerSegment - 1 < strip->numPixels()) {
                SetRangeBrightness(i * pixelsPerSegment, i * pixelsPerSegment + pixelsPerSegment - 1, 0);
              } else {
                SetRangeBrightness(i * pixelsPerSegment, strip->numPixels() - 1, 0);
              }
              modeInitialized = true;
            }
          } else {
            CycleBrightnessData(1);
          }
        } else {
          SetRangeBrightness (0, strip->numPixels() - 1, 1);
          brightnessMode = kOn;
        }
      }
    case kBlinking: {
        if (millis() % int(loopSeconds * 1000 + .5) < (loopSeconds * 1000 + .5) / 2) {
          SetRangeBrightness(0, strip->numPixels() - 1, 0);
        } else {
          SetRangeBrightness(0, strip->numPixels() - 1, 1);
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
        float timeLoop = float(millis() % int(loopSeconds * 1000)) / 1000;
        float timeHalf = float(millis() % int(loopSeconds / 2 * 1000)) / 1000;

        if (timeLoop <= loopSeconds / 2)
          SetRangeBrightness( 0, strip->numPixels() - 1, (timeHalf * timeHalf) / (loopSeconds / 2 * loopSeconds / 2));
        else
          SetRangeBrightness( 0, strip->numPixels() - 1, ((loopSeconds / 2 * loopSeconds / 2) - (timeHalf * timeHalf)) /
                              (loopSeconds / 2 * loopSeconds / 2));
      }
      break;
    case kOff: {
        SetRangeBrightness (0, strip->numPixels() - 1, 0);
      }
      break;
    case kOn:
    default: {
        SetRangeBrightness (0, strip->numPixels() - 1, 1);
      }
      break;
  }
  switch (colorMode) {
    case kRainbowReverse: {
        float baseHue = float(millis() % int(loopSeconds * 1000)) * -360 / loopSeconds / 1000;

        while (baseHue < 0) {
          baseHue = 360 - fabs(baseHue);
        }


        for (uint32_t pixel = 0; pixel <= strip->numPixels() - 1; pixel++) {
          SetRangeHSV(pixel, pixel, baseHue +  pixel * 360 / strip->numPixels(), 1, 1);
        }
      }
      break;
    case kBrown:
      SetRangeRGB(0, strip->numPixels() - 1, 93, 21, 0);
      break;
    case kQuasics:
      SetRangeHSV(0, strip->numPixels() - 1, 120, 1, .62);
      break;
    case kYellow:
      SetRangeRGB(0, strip->numPixels() - 1, 255, 255, 0);
      break;
    case kRed: {
        SetRangeRGB(0, strip->numPixels() - 1, 255, 0, 0);
      }
      break;
    case kGreen: {
        SetRangeRGB(0, strip->numPixels() - 1, 0, 255, 0);
      }
      break;
    case kBlue: {
        SetRangeRGB(0, strip->numPixels() - 1, 0, 0, 255);
      }
      break;
    case kWhite: {
        SetRangeRGB(0, strip->numPixels() - 1, 255, 255, 255);
      }
      break;
    case kRainbow: {
        float baseHue = float(millis() % int(loopSeconds * 1000)) * 360 / loopSeconds / 1000;

        while (baseHue < 0) {
          baseHue = 360 - fabs(baseHue);
        }


        for (uint32_t pixel = 0; pixel <= strip->numPixels() - 1; pixel++) {
          SetRangeHSV(pixel, pixel, baseHue +  pixel * 360 / strip->numPixels(), 1, 1);
        }
      }
      break;
    case kOldCycle: {
        SetRangeHSV(0, strip->numPixels() - 1, deltaHueForCycle * modeIteration, 1, 1);
        modeIteration = modeIteration % int(360 / deltaHueForCycle);
      }
      break;
    default: {
        SetRangeRGB(0, strip->numPixels() - 1, 0, 0, 0);
      }
      break;
  }

  modeIteration++;
  strip->show();
}

void NeoPixelController::SetColorMode (ColorMode color) {
  colorMode = color;
  colorInitialized = false;
}

void NeoPixelController::SetBrightnessMode (BrightnessMode brightness) {
  brightnessMode = brightness;
  modeInitialized = false;
}

void NeoPixelController::SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue) {
  for (uint32_t pixel = startPixel; pixel <= endPixel; pixel++) {
    strip->setPixelColor (pixel, int(float(red)* brightnessData[pixel] * universalBrightness),
                          int(float(green)* brightnessData[pixel] * universalBrightness),
                          int(float(blue)* brightnessData[pixel] * universalBrightness));
  }
}

void NeoPixelController::SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value) {
  hue = hue / 360 - int(hue / 360); //Take hue from 0-360, turn it to 0-1, and remove any extra cycles around the wheel (remove the one place)

  byte rgb[3];
  rgbConverter.hsvToRgb(hue, saturation, value, rgb);
  SetRangeRGB(startPixel, endPixel, rgb[0], rgb[1], rgb[2]);
}

void NeoPixelController::CycleBrightnessData (uint32_t numberOfSpaces) {
  numberOfSpaces = numberOfSpaces % strip->numPixels();
  if (numberOfSpaces != 0) {
    float buf[numberOfSpaces];
    uint16_t counter = 0;
    for (uint16_t i = 0; i < numberOfSpaces; i++) {
      buf[i] = brightnessData[strip->numPixels() - numberOfSpaces + i];
    }
    counter = 0;
    for (uint16_t i = strip->numPixels() - numberOfSpaces; i < strip->numPixels(); i++) {
      brightnessData[i] = brightnessData[counter];
      counter++;
    }
    for (uint16_t i = 0; i < numberOfSpaces; i++) {
      brightnessData[i] = buf[i];
    }
  }
}

void NeoPixelController::SetRangeBrightness(uint32_t first, uint32_t last, float brightnessLevel) {
  for (uint32_t pixel = first; pixel <= last; pixel++)
    brightnessData[pixel] = brightnessLevel;
}

void NeoPixelController::CycleColorData (uint32_t numberOfSpaces) {
  numberOfSpaces = numberOfSpaces % strip->numPixels();
  if (numberOfSpaces != 0) {
    float buf[numberOfSpaces];
    uint16_t counter = 0;
    for (uint16_t i = 0; i < numberOfSpaces; i++) {
      buf[i] = strip->getPixelColor(strip->numPixels() - numberOfSpaces + i);
    }
    counter = 0;
    for (uint16_t i = strip->numPixels() - numberOfSpaces; i < strip->numPixels(); i++) {
      strip->setPixelColor(i, strip->getPixelColor(counter));
      counter++;
    }
    for (uint16_t i = 0; i < numberOfSpaces; i++) {
      strip->setPixelColor(i, buf[i]);
    }
  }
}

void NeoPixelController::SetLoopTime (float seconds) {
  loopSeconds = fabs(seconds);
}

float NeoPixelController::LoopTime () {
  return loopSeconds;
}

void NeoPixelController::SetMaxBrightness (float brightness){
  universalBrightness = brightness;
}

float NeoPixelController::GetMaxBrightness (){
  return universalBrightness;
}

