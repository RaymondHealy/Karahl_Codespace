#include "Arduino.h"

#ifndef  SIMPLE_JOYSTICK_H_
#define  SIMPLE_JOYSTICK_H_

class Joystick {
  public:
    Joystick(uint32_t xIn, uint32_t yIn);

    void Calibrate();

    float GetX();
    float GetY();

  private:
    uint16_t GetRawX();
    uint16_t GetRawY();

    double fMap(double src, double fromLow, double fromHigh, double toLow, double toHigh);

    uint32_t kXIn;
    uint32_t kYIn;

    uint16_t centerX;
    uint16_t centerY;

    uint16_t kMaxX = 900;
    uint16_t kMinX = 0;
    uint16_t kMaxY = 900;
    uint16_t kMinY = 0;
};

class PushJoystick {
  public:
    PushJoystick(uint32_t xIn, uint32_t yIn, uint32_t btnIn);

    void Calibrate();

    float GetX();
    float GetY();
    bool GetSwitch();

  private:
    Joystick* stick;
    uint32_t kBtnIn;
};

#endif //SIMPLE_JOYSTICK_H_
