#include "RaymondUnoNeoPixel.h"
NeoPixelController::NeoPixelController(uint32_t pin, float loopSecondsIn, uint8_t brightness, uint32_t stripLength, neoPixelType type) {
  strip = new Adafruit_NeoPixel(stripLength, pin, type);

	modeIteration = 0;
	colorInitialized = 0;
	colorMode = kNone;
	brightnessMode = kOff;
	loopSeconds = fabs(loopSecondsIn);
	pixelsPerSegment = 6;

	brightnessData = new float [strip->numPixels()];
	for (uint32_t i = 0; i < strip->numPixels(); i++) {
		brightnessData [i] = 1;
	}

	universalBrightness = float(brightness) / 255;

	strip->setBrightness(255);
	strip->begin();
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
	red = max(0, min(red, 255));
	green = max(0, min(green, 255));
	blue = max(0, min(blue, 255));

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
		for (uint32_t i = 1; i <= numberOfSpaces; i++) {
			float copy[strip->numPixels()];
			const float firstCell = brightnessData[strip->numPixels() - 1];
			memmove(brightnessData + 1, brightnessData, (strip->numPixels() - 1) * sizeof(float));
			brightnessData[0] = firstCell;
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

void NeoPixelController::SetMaxBrightness (float brightness) {
	universalBrightness = brightness;
}

float NeoPixelController::GetMaxBrightness () {
	return universalBrightness;
}

uint32_t NeoPixelController::GetPixelsPerSegment () {
	return pixelsPerSegment;
}

// Note: this function is trying to make sure that we'we wind up with a value for
// "pixelsPerSegment" that is an integer divisor of the # of pixels in the strip.
// However, since strips can be arbitrary lengths (including primes), that may
// not work out as well as Raymond's original design calls for.  The code has been
// modified so that we *will* wind up with an integer divisor (though that may be
// 0), which addresses a potential infinite loop seen in earlier versions (e.g.,
// with an odd # of pixels in the strip).
void NeoPixelController::SetPixelsPerSegment (uint32_t pixels) {
  if (strip->numPixels() < 2) {
    pixelsPerSegment = 1;
    return;
  }

	if (pixels % 2 != 0) {  //Make the number of pixels a round number
		if (pixels > pixelsPerSegment) { //increase or decrease with translation direction
			pixels++;
		} else {
			pixels--;
		}
	}

  const int maxSegmentLength = max(1, strip->numPixels() - 2);
  const int minSegmentLength = min(2, maxSegmentLength);
 
  bool atLimit = (pixels > - maxSegmentLength || pixels < minSegmentLength); //at min/max?
  pixels = min(maxSegmentLength, max(minSegmentLength, pixels)); //Cap at min/max

	if (!atLimit) { //if not at the limit
		bool isIncreasing = pixels > pixelsPerSegment;  //determine whether or not to increment

        while (strip->numPixels() % pixels != 0) {  //do this until the strip length is a multiple of the number of pixels
			if (isIncreasing) {
			pixels = pixels + 1;
			} else {
				pixels = pixels - 1;
			}
		}
	}
	pixelsPerSegment = pixels;  //Save the result
}

uint32_t NeoPixelController::GetStripLength() {
	return strip->numPixels();  //get the number of pixels in the strip
}
