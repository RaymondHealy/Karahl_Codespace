#define SerialOut
#define LCDOut
//----------------------------<Constants>------------------------------
//-------<Input Constants>---------//***Constants For The Input Pins***
const int kLeftIn = A1;            //Left Jack Input Pin
const int kRightIn = A0;           //Right Jack Input Pin
const int kMaxPot = A3;            //Display Range Potentiometer Input Pin
//---------------------------------

//-------<Serial Constants>--------//***Constants For Serial Communication (Iff Used)***
#ifdef   SerialOut
const uint32_t kBaudRate = 9600;   //Baud Rate If Outputing To Serial
#endif //SerialOut
//---------------------------------

//--------<LCD Constants>----------//***Constants For The LCD Display (Iff Used)***
#ifdef   LCDOut
const uint8_t kNumLCDCollums = 16; //Number Of Columns In The LCD Display
const uint8_t kNumLCDRows = 2;     //Number Of Rows In The LCD Display
const char kBlank = char(32);      //The Blank Character
const char kFull = char(0xff);     //The Full Character

const uint8_t RegisterSwitch = 7;  //The LCD RS Pin
const uint8_t ReadWrite = 8;       //The LCD RW Pin
const uint8_t Enable = 9;          //The LCD Enable(E) Pin
const uint8_t D4 = 10;             //The LCD D4 Pin
const uint8_t D5 = 11;             //The LCD D5 Pin
const uint8_t D6 = 12;             //The LCD D6 Pin
const uint8_t D7 = 13;             //The LCD D7 Pin
#endif //LCDOut
//---------------------------------

//-------<Timing Constants>--------//***Timer Constants***
const uint16_t kPrintStep = 100;   //Number of Miliseconds Between Writes
//---------------------------------
//---------------------------------------------------------------------


//----------------------------<Variables>------------------------------
//-------<Timer Variables>---------//***Variables For Timekeeping***
uint32_t lastPrintOut;             //Time Of The Last Print Out
//---------------------------------

//--------<LCD Variables>----------//***Variables Involving The LCD Display***
#ifdef   LCDOut                    //***Iff Used                           ***
#endif //LCDOut
//---------------------------------

//-------<Serial Variables>--------//***Variables Involving Serial Communications***
#ifdef   SerialOut                 //***Iff Used                                 ***    
#endif //SerialOut
//---------------------------------

//------<Average Variables>--------//***Variables For Data Collection***
uint32_t leftTimesPolled;          //Number Of Items In "leftSum" Set
uint32_t rightTimesPolled;         //Number Of Items In "rightSum" Set
uint32_t leftSum;                  //Sum Of Non-Zero Left Pin Polls
uint32_t rightSum;                 //Sum Of Non-Zero Right Pin Polls
//---------------------------------
//---------------------------------------------------------------------

void setup() {
#ifdef   SerialOut
  Serial.begin(kBaudRate);
  Serial.print("\n----------<VU Meter Start>----------\n");
#endif //SerialOut

  lastPrintOut = millis();
  leftTimesPolled = 0;
  rightTimesPolled = 0;
  leftSum = 0;
  rightSum = 0;
}

void loop() {
  uint8_t leftIn = analogRead(kLeftIn);
  uint8_t rightIn = analogRead(kRightIn);
  if (leftIn != 0) {
    leftSum += leftIn;
    leftTimesPolled += 1;
  }
  if (rightIn != 0) {
    rightSum += rightIn;
    rightTimesPolled += 1;
  }

  if (millis() >= lastPrintOut + kPrintStep) {
    float leftAvg = float(leftSum) / leftTimesPolled;
    float rightAvg = float(rightSum) / rightTimesPolled;
    uint8_t powerRegister = (analogRead(kMaxPot) + 50) / 100 + 1;

#ifdef   SerialOut
    if (leftAvg >= 1023) {
      Serial.print("\n     Left : Max \n");
    } else {
      Serial.print("\n     Left : ");
      Serial.println(int(leftAvg + .5));
    }

    if (rightAvg >= 1023) {
      Serial.print("     Right: Max\n");
    } else {
      Serial.print("     Right: ");
      Serial.println(int(rightAvg + .5));
    }

    Serial.print("     PowLv: ");
    Serial.println(powerRegister);
#endif //SerialOut
#ifdef   LCDOut

#endif //LCDOut
byte(0xff)


    leftSum = 0;
    rightSum = 0;
    leftTimesPolled = 0;
    rightTimesPolled = 0;
    lastPrintOut = millis();
  }
}
