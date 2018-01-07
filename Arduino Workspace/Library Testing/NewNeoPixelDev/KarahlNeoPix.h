#include <Adafruit_NeoPixel.h>
#include "Arduino.h"

#ifndef  KARAHL_NEO_PIX_H_
#define  KARAHL_NEO_PIX_H_
class KarahlNeoPix {
  public:
    KarahlNeoPix(uint32_t stripLength, uint32_t pin, uint8_t brightness = 255,
                 uint32_t comsProtocol = NEO_GRB + NEO_KHZ800);

    void UpdateStrip();

    void SetRangeRGB(uint32_t startIndex, uint32_t endIndex, uint8_t red,
                     uint8_t green, uint8_t blue);
    void SetRangeBrightness(uint32_t startIndex, uint32_t endIndex,
                            float brightness);

    void GetPixelRGB(uint32_t pixelIndex, uint8_t& red, uint8_t& green,
                     uint8_t& blue);

  private:
    void CodeToRGB(uint32_t colorCode, uint8_t& red, uint8_t& green,
                   uint8_t& blue);



    float* brightnessData;
    Adafruit_NeoPixel* strip;
};

#endif //KARAHL_NEO_PIX_H_
