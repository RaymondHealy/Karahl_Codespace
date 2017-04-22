#include "NeoPixelUSBController.h"

NeoPixelUSBController::NeoPixelUSBController (uint32_t pin, float loopSeconds, uint8_t brightness, uint32_t stripLength) {
  strip = new NeoPixelController (pin, loopSeconds, brightness, stripLength);
  Serial.begin(115200);
  serialIn = "";
}

void NeoPixelUSBController::NeoPixelSerialProcess () {
  if (Serial.available() > 0) {
    char c = char(Serial.read());
    if (c == ';') {
      Translator(serialIn.c_str());
      serialIn = "";
    } else {
      serialIn += c;
    }

  }
  strip->NeoPixelProcess();
}

inline bool equal(const char* s1, const char* s2) {
  return strcmp(s1, s2) == 0;
}

void NeoPixelUSBController::Translator (const char * input) {
  Serial.println("--------------------------------------------------------------------");
  Serial.print("Input  : '");
  Serial.print(input);
  Serial.println(";'");
  if (equal(input, "Red")) {
    strip->SetColorMode(NeoPixelController::kRed);
    Serial.println("     Color  : Red");
  } else if (equal(input, "Purple")) {
    strip->SetColorMode(NeoPixelController::kPurple);
    Serial.println("     Color  : Purple");
  } else if (equal(input, "Help")) {
    PrintHelpInfo();
  } else if (equal(input, "Green")) {
    strip->SetColorMode(NeoPixelController::kGreen);
    Serial.println("     Color  : Green");
  } else if (equal(input, "Blue")) {
    strip->SetColorMode(NeoPixelController::kBlue);
    Serial.println("     Color  : Blue");
  } else if (equal(input, "White")) {
    strip->SetColorMode(NeoPixelController::kWhite);
    Serial.println("     Color  : White");
  } else if (equal(input, "Rainbow")) {
    strip->SetColorMode(NeoPixelController::kRainbow);
    Serial.println("     Color  : Rainbow");
  } else if (equal(input, "OldCycle")) {
    strip->SetColorMode(NeoPixelController::kOldCycle);
    Serial.println("     Color  : Old Cycle");
  } else if (equal(input, "Yellow")) {
    strip->SetColorMode(NeoPixelController::kYellow);
    Serial.println("     Color  : Yellow");
  } else if (equal(input, "Quasics")) {
    strip->SetColorMode(NeoPixelController::kQuasics);
    Serial.println("     Color  : Quasics");
  } else if (equal(input, "Brown")) {
    strip->SetColorMode(NeoPixelController::kBrown);
    Serial.println("     Color  : Brown");
  } else if (equal(input, "On")) {
    strip->SetBrightnessMode(NeoPixelController::kOn);
    Serial.println("     Dynamic: On");
  } else if (equal(input, "Breathing")) {
    strip->SetBrightnessMode(NeoPixelController::kBreathing);
    Serial.println("     Dynamic: Breathing");
  } else if (equal(input, "Blinking")) {
    strip->SetBrightnessMode(NeoPixelController::kBlinking);
    Serial.println("     Dynamic: Blinking");
  } else if (equal(input, "Dashed")) {
    strip->SetBrightnessMode(NeoPixelController::kDashed);
    Serial.println("     Dynamic: Dashed");
  } else if (equal(input, "RollIn")) {
    strip->SetBrightnessMode(NeoPixelController::kRollIn);
    Serial.println("     Dynamic: Roll In");
  } else if (equal(input, "RollOut")) {
    strip->SetBrightnessMode(NeoPixelController::kRollOut);
    Serial.println("     Dynamic: Roll Out");
  } else if (equal(input, "Rolling")) {
    strip->SetBrightnessMode(NeoPixelController::kRolling);
    Serial.println("     Dynamic: Rolling");
  } else if (equal(input, "Off")) {
    strip->SetBrightnessMode(NeoPixelController::kOff);
    strip->SetColorMode(NeoPixelController::kNone);
    Serial.println("     Notice : Colors and dynamics reset");
  } else if (equal(input, "SpeedUp")) {
    Serial.print("     Notice :Set loop time from ");
    Serial.print(strip->LoopTime());
    strip->SetLoopTime(strip->LoopTime() / 2);
    Serial.print(" seconds to ");
    Serial.print(strip->LoopTime());
    Serial.println(" seconds");
  } else if (equal(input, "SpeedDown")) {
    Serial.print("     Notice :Set loop time from ");
    Serial.print(strip->LoopTime());
    strip->SetLoopTime(strip->LoopTime() * 2);
    Serial.print(" seconds to ");
    Serial.print(strip->LoopTime());
    Serial.println(" seconds");
  } else if (equal(input, "MaxUp")) {
    if (strip->GetMaxBrightness() * 2 >= 1) {
      strip->SetMaxBrightness(1);
      Serial.println("     Notice : Brightness At Max");
    } else {
      strip->SetMaxBrightness(strip->GetMaxBrightness() * 2);
      Serial.print("     Notice : Brightness at ");
      Serial.print(strip->GetMaxBrightness() * 100);
      Serial.println("% of absolute max");
    }
  } else if (equal(input, "MaxDown")) {
    strip->SetMaxBrightness(strip->GetMaxBrightness() / 2);
    Serial.print("     Notice : Brightness at ");
    Serial.print(strip->GetMaxBrightness() * 100);
    Serial.println("% of absolute max");
  } else if (equal(input, "SegmentUp")) {
    if (strip->GetPixelsPerSegment() < strip->GetStripLength() - 4) {
      strip->SetPixelsPerSegment(strip->GetPixelsPerSegment() + 2);
      Serial.print("     Notice : ");
      Serial.print(strip->GetPixelsPerSegment());
      Serial.println(" pixels per segment");
    } else {
      strip->SetPixelsPerSegment(strip->GetStripLength());
      Serial.println("     Notice : Segment size at max (strip length)");
    }
    strip->SetBrightnessMode(NeoPixelController::kDashed);
  }  else if (equal(input, "SegmentDown")) {
    if (strip->GetPixelsPerSegment() > 5) {
      strip->SetPixelsPerSegment(strip->GetPixelsPerSegment() - 2);
      Serial.print("     Notice : ");
      Serial.print(strip->GetPixelsPerSegment());
      Serial.println(" pixels per segment");
    } else {
      strip->SetPixelsPerSegment(2);
      Serial.println("     Notice : Segment size at min (2)");
    }
    strip->SetBrightnessMode(NeoPixelController::kDashed);
  } else {
    Serial.println("     ***ERROR***");
  }
  Serial.println("--------------------------------------------------------------------\n");
}

void NeoPixelUSBController::PrintHelpInfo() {
  Serial.println("Colors:");
  Serial.println("    Red;");
  Serial.println("    Green;");
  Serial.println("    Blue;");
  Serial.println("    White;");
  Serial.println("    Rainbow;");
  Serial.println("    OldCycle;");
  Serial.println("    Yellow;");
  Serial.println("    Quasics;");
  Serial.println("    Brown;");
  Serial.println("    Purple;");
  Serial.println("Dynamics:");
  Serial.println("    On;");
  Serial.println("    Breathing;");
  Serial.println("    Blinking;");
  Serial.println("    Dashed;");
  Serial.println("    RollIn;");
  Serial.println("    RollOut;");
  Serial.println("    Rolling;");
  Serial.println("    Off;");
  Serial.println("Settings:");
  Serial.println("    SpeedUp;");
  Serial.println("    SpeedDown;");
  Serial.println("    MaxUp;");
  Serial.println("        Increase max brightness");
  Serial.println("    MaxDown;");
  Serial.println("        Decrease max brightness");
  Serial.println("    SegmentUp;");
  Serial.println("        Increase size of dashed segments");
  Serial.println("    SegmentDown;");
  Serial.println("        Decrease size of dashed segments");
}

