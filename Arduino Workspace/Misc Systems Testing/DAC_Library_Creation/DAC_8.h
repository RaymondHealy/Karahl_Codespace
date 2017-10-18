#ifndef DAC_8_H_
#define DAC_8_H_

#include "arduino.h"

class DAC_8 {
  public:
    DAC_8(uint8_t pinOne, uint8_t pinTwo, uint8_t pinThree, uint8_t pinFour, uint8_t pinFive, uint8_t pinSix, uint8_t pinSeven, uint8_t pinEight);

    void dacWrite(uint8_t valueIn);
    uint8_t dacRead();

  private:
    uint8_t value;
  
    uint8_t kPinOne;
    uint8_t kPinTwo;
    uint8_t kPinThree;
    uint8_t kPinFour;
    uint8_t kPinFive;
    uint8_t kPinSix;
    uint8_t kPinSeven;
    uint8_t kPinEight;
};


#endif //DAC_8_H
