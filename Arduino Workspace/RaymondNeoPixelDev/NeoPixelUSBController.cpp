#include "NeoPixelUSBController.h"
NeoPixelUSBController::NeoPixelUSBController (uint32_t pin, float loopSeconds, uint8_t brightness, uint32_t stripLength) {
  strip = new NeoPixelController (pin, loopSeconds, brightness, stripLength);
  Serial.begin(19200);
  serialIn = "";
}

void NeoPixelUSBController::NeoPixelSerialProcess () {
  while (Serial.available() > 0) {
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

inline bool equal(String s1, String s2) {
  return s1.equals(s2);
}

void NeoPixelUSBController::Translator (String input) {
  input.trim();
  Serial.println("--------------------------------------------------------------------");
  Serial.print("Input  : '");
  Serial.print(input);
  Serial.println(";'");
  input.toUpperCase();
  if (equal(input, "RED")) {
    strip->SetColorMode(NeoPixelController::kRed);
    Serial.println("     Color  : Red");
  } else if (equal(input, "PURPLE")) {
    strip->SetColorMode(NeoPixelController::kPurple);
    Serial.println("     Color  : Purple");
  } else if (equal(input, "HELP")) {
    PrintHelpInfo();
  } else if (equal(input, "GREEN")) {
    strip->SetColorMode(NeoPixelController::kGreen);
    Serial.println("     Color  : Green");
  } else if (equal(input, "BLUE")) {
    strip->SetColorMode(NeoPixelController::kBlue);
    Serial.println("     Color  : Blue");
  } else if (equal(input, "WHITE")) {
    strip->SetColorMode(NeoPixelController::kWhite);
    Serial.println("     Color  : White");
  } else if (equal(input, "RAINBOW")) {
    strip->SetColorMode(NeoPixelController::kRainbow);
    Serial.println("     Color  : Rainbow");
  } else if (equal(input, "OLDCYCLE")) {
    strip->SetColorMode(NeoPixelController::kOldCycle);
    Serial.println("     Color  : Old Cycle");
  } else if (equal(input, "YELLOW")) {
    strip->SetColorMode(NeoPixelController::kYellow);
    Serial.println("     Color  : Yellow");
  } else if (equal(input, "QUASICS")) {
    strip->SetColorMode(NeoPixelController::kQuasics);
    Serial.println("     Color  : Quasics");
  } else if (equal(input, "BROWN")) {
    strip->SetColorMode(NeoPixelController::kBrown);
    Serial.println("     Color  : Brown");
  } else if (equal(input, "ON")) {
    strip->SetBrightnessMode(NeoPixelController::kOn);
    Serial.println("     Dynamic: On");
  } else if (equal(input, "BREATHING")) {
    strip->SetBrightnessMode(NeoPixelController::kBreathing);
    Serial.println("     Dynamic: Breathing");
  } else if (equal(input, "BLINKING")) {
    strip->SetBrightnessMode(NeoPixelController::kBlinking);
    Serial.println("     Dynamic: Blinking");
  } else if (equal(input, "DASHED")) {
    strip->SetBrightnessMode(NeoPixelController::kDashed);
    Serial.println("     Dynamic: Dashed");
  } else if (equal(input, "ROLLIN")) {
    strip->SetBrightnessMode(NeoPixelController::kRollIn);
    Serial.println("     Dynamic: Roll In");
  } else if (equal(input, "ROLLOUT")) {
    strip->SetBrightnessMode(NeoPixelController::kRollOut);
    Serial.println("     Dynamic: Roll Out");
  } else if (equal(input, "ROLLING")) {
    strip->SetBrightnessMode(NeoPixelController::kRolling);
    Serial.println("     Dynamic: Rolling");
  } else if (equal(input, "OFF")) {
    strip->SetBrightnessMode(NeoPixelController::kOff);
    strip->SetColorMode(NeoPixelController::kNone);
    Serial.println("     Notice : Colors and dynamics reset");
  } else if (equal(input, "SPEEDUP")) {
    Serial.print("     Notice :Set loop time from ");
    Serial.print(strip->LoopTime());
    strip->SetLoopTime(strip->LoopTime() / 2);
    Serial.print(" seconds to ");
    Serial.print(strip->LoopTime());
    Serial.println(" seconds");
  } else if (equal(input, "SPEEDDOWN")) {
    Serial.print("     Notice :Set loop time from ");
    Serial.print(strip->LoopTime());
    strip->SetLoopTime(strip->LoopTime() * 2);
    Serial.print(" seconds to ");
    Serial.print(strip->LoopTime());
    Serial.println(" seconds");
  } else if (equal(input, "MAXUP")) {
    if (strip->GetMaxBrightness() * 2 >= 1) {
      strip->SetMaxBrightness(1);
      Serial.println("     Notice : Brightness At Max");
    } else {
      strip->SetMaxBrightness(strip->GetMaxBrightness() * 2);
      Serial.print("     Notice : Brightness at ");
      Serial.print(strip->GetMaxBrightness() * 100);
      Serial.println("% of absolute max");
    }
  } else if (equal(input, "MAXDOWN")) {
    strip->SetMaxBrightness(strip->GetMaxBrightness() / 2);
    Serial.print("     Notice : Brightness at ");
    Serial.print(strip->GetMaxBrightness() * 100);
    Serial.println("% of absolute max");
  } else if (equal(input, "SEGMENTUP")) {
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
  }  else if (equal(input, "SEGMENTDOWN")) {
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
