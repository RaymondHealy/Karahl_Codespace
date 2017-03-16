#include <SerialInterface.h>
#include <SPI.h>
#include <Pixy.h>

//#define cameraDistance

const uint32_t numberOfLoops = 50;
const uint32_t targetSignature = 1;
const uint32_t deltaTolerance = 50;
const uint32_t areaTolerance = 100;

#ifdef cameraDistance
const uint32_t targetArea = 250;
#endif

struct targetBlock {
  uint16_t height;
  uint16_t width;
  uint16_t x;
};

// This is the main Pixy object
Pixy pixy;
SerialInterface * serialInterface;

void setup() {
  serialInterface = new SerialInterface ();
  pixy.init(); //initialize the Pixy
}

void loop() {
  static int i = 0; //loop Counter
  int j; //Block Cycler
  uint16_t blocks; //number of detected blocks
  static char buf[14] = "Camera,L,N,G;"; //character buffer (32 characters)
  targetBlock leftBlock = {0, 0, 0};
  targetBlock rightBlock = {0, 0, 0};

  //grab blocks
  blocks = pixy.getBlocks();

  //if there are blocks...
  if (blocks && i % numberOfLoops == 0) {
    uint32_t targetBlocks = 0;
    targetBlock targetAray[2];  //Arbitrary buffer
    for (j = 0; j < blocks; j++) //from j = 0 to j < number of blocks (incrementing j by 1 each time)
    {
      if (pixy.blocks[j].signature == targetSignature && pixy.blocks[j].height > pixy.blocks[j].width) {
        if (targetBlocks <= 2)
          targetAray[j] = {pixy.blocks[j].height, pixy.blocks[j].width, pixy.blocks[j].x};
        targetBlocks++;
      }
    }
    if (targetBlocks > 2) { //If Overflowing, return default
      buf[8] = 'L';
      buf[10] = 'N';
      buf[12] = 'G';
    } else {
      if (targetAray[0].x > targetAray[1].x) {
        leftBlock = targetAray[1];
        rightBlock = targetAray[0];
      } else {
        leftBlock = targetAray[0];
        rightBlock = targetAray[1];
      }

      bool isFarLeft = true;
      bool isGoodDistance = true;
      if (leftBlock.height * leftBlock.width >= rightBlock.height * rightBlock.width){
        buf[8] = 'L';
        isFarLeft = true;
      } else {
        buf[8] = 'R';
        isFarLeft = false;
      }
      #ifdef cameraDistance
        if ((leftBlock.height * leftBlock.width + rightBlock.height * rightBlock.width)/2 <= areaTolerance){
          isGoodDistance = true;
        } else {
          isGoodDistance = false;
        }
      #else
        isGoodDistance = true;
      #endif

      if(abs(leftBlock.height * leftBlock.width - rightBlock.height * rightBlock.width) <= deltaTolerance && isGoodDistance){
        buf[12] = 'G';
      } else {
        buf[12] = 'B';
      }
    }
  }
  if (i % numberOfLoops == 0)
    serialInterface->SerialWrite(buf);
  i++;
}

