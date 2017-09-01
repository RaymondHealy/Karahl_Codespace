#ifndef NEO_PIXEL_CONTROLLER_H_
#define NEO_PIXEL_CONTROLLER_H_

#include "Arduino.h"
#include <Adafruit_NeoPixel.h>
#include <RGBConverter.h>

class NeoPixelController {
public:
	NeoPixelController(uint32_t pin, float loopSeconds, 
		uint8_t brightness, uint32_t stripLength);		//Constructor
	
	//--------------------------------------------------------------------Enums--------------------------------------------------------------------
	enum ColorMode {		//Pre-programmed color paterns
		kNone, 
		kBlueNoise,
		kRed, 
		kGreen, 
		kBlue, 
		kWhite, 
		kRainbow, 
		kRainbowReverse, 
		kOldCycle, 
		kYellow, 
		kQuasics, 
		kBrown, 
		kPurple
	};

	enum BrightnessMode {		//Pre-programmed dynamic patterns
		kOff, 
		kOn, 
		kBreathing, 
		kBlinking, 
		kDashed, 
		kRollIn, 
		kRollOut, 
		kRolling, 
		kSnakeIn, 
		kSnakeOut, 
		kSnake, 
		kPSnake
	};

	//-------------------------------------------------------------Patern Setting-------------------------------------------------------------
	void NeoPixelProcess ();		//Carry out the currently set color and dynamic patterns
	void SetColorMode (ColorMode color);		//Change the set color pattern
	void SetBrightnessMode (BrightnessMode brightness);		//Change the set dynamic pattern

	//----------------------------------------------------------Change Pattern Parameters----------------------------------------------------------
	void SetLoopTime (float seconds);		//Change the time of the loop for the color and brightness paterns
	void SetMaxBrightness (float brightness);		//Set the max brightness of the strip as a whole (NeoPixel brightness command is one-use only)
	void SetPixelsPerSegment (uint32_t pixels);		//change the pixels per dash segment

	//----------------------------------------------------Pattern Parameter Information Return-----------------------------------------------------
	uint32_t GetStripLength();		//Return the length of the strip
	float GetMaxBrightness ();		//Get the set max brightness of the strip as a whole
	uint32_t GetPixelsPerSegment ();		//Get pixels per dash segment
	float LoopTime ();		//Returns the loop time

private:
	//------------------------------------------------------------------Functions------------------------------------------------------------------
	void SetRangeRGB (uint32_t startPixel, uint32_t endPixel, uint32_t red, uint32_t green, uint32_t blue);		//Set the color from start to end pixel with RGB
	void SetRangeHSV(uint32_t startPixel, uint32_t endPixel, float hue, float saturation, float value);		//Set the color from start to end pixel with hsv
	void CycleBrightnessData (uint32_t numberOfSpaces);		//Cycle the brightness data (allows for rotation of the individual pixels' brightness)
	void CycleColorData (uint32_t numberOfSpaces);		//Cycle the color data (allows for rotation of the individeal pixels' colors)
	void SetRangeBrightness(uint32_t first, uint32_t last, float brightnessLevel);		//Set the individual brightness data from start to end (used in the brightness patterns)

	//------------------------------------------------------------------Variables------------------------------------------------------------------
	uint32_t pixelsPerSegment;		//Pixels per dash segment
	float loopSeconds;		//Pattern loop time in seconds

	uint32_t modeIteration;		//Dynamic time counter, taking the loop time into account
	bool colorInitialized;		//Has the color pattern been initialized (set to false when color mode changed)
	bool modeInitialized;		//Has the brightness pattern been initialized (set to false when color mode changed)

	float * brightnessData;		//Individual pixel brightness data
	float universalBrightness;		//Brightness of the entire strip

	ColorMode colorMode;		//Currently set color mode
	BrightnessMode brightnessMode;		//Currently set dynamic mode

	//-------------------------------------------------------------------Objects-------------------------------------------------------------------
	Adafruit_NeoPixel* strip;		//The actual NeoPixel strip
	RGBConverter rgbConverter;		//Handles RGB to HSV conversion
};

#endif //NEO_PIXEL_CONTROLLER_H_
