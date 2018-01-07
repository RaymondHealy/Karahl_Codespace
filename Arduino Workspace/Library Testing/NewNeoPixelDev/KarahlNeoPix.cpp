#include "KarahlNeoPix.h"

KarahlNeoPix::KarahlNeoPix(uint32_t stripLength, uint32_t pin, uint8_t brightness,
                           uint32_t comsProtocol) {

  strip = new Adafruit_NeoPixel(stripLength, pin, comsProtocol);

  strip->begin();
  strip->setBrightness(255);
  strip->show();

  float fBrightness = float(brightness) / 255;

  brightnessData = new float[stripLength];

  for (int i = 0; i < stripLength; i++) {
    brightnessData[i] = fBrightness;
  }
}

void KarahlNeoPix::UpdateStrip() {
  strip->show();
}

void KarahlNeoPix::SetRangeRGB(uint32_t startIndex, uint32_t endIndex, uint8_t red,
                               uint8_t green, uint8_t blue) {
  for (int i = startIndex; i <= endIndex; i++) {
    strip->setPixelColor(i, red * brightnessData[i], green * brightnessData[i],
                         blue * brightnessData[i]);
  }

  strip->show();
}

void KarahlNeoPix::SetRangeBrightness(uint32_t startIndex, uint32_t endIndex,
                                      float brightness) {
  brightness = max(min(brightness, 1), 0);

  if (startIndex > endIndex) {
    uint32_t temp = endIndex;

    endIndex = startIndex;
    startIndex = temp;
  }

  if (endIndex >= strip->numPixels()) {
    endIndex = strip->numPixels() - 1;
  }

  for (int i = startIndex; i <= endIndex; i++) {
    brightnessData[i] = brightness;
  }

  strip->show();
}

void KarahlNeoPix::CodeToRGB(uint32_t colorCode, uint8_t& red, uint8_t& green,
                             uint8_t& blue) {
  blue = colorCode % int(pow(2, 8));
  colorCode = (colorCode - blue) / int(pow(2, 8));

  green = colorCode % int(pow(2, 8));
  colorCode = (colorCode - green) / int(pow(2, 8));

  red = colorCode % int(pow(2, 8));
  colorCode = (colorCode - red) / int(pow(2, 8));
}

void KarahlNeoPix::GetPixelRGB(uint32_t pixelIndex, uint8_t& red, uint8_t& green,
                               uint8_t& blue) {
  red = 0;
  green = 0;
  blue = 0;

  CodeToRGB(strip->getPixelColor(pixelIndex), red, green, blue);
  float brightness = brightnessData[pixelIndex];

  red = int(float(red) / brightness + .5);
  green  = int(float(green) / brightness + .5);
  blue = int(float(blue) / brightness + .5);

}

