#include "serialInterface.h"

SerialInterface::SerialInterface(uint32_t baud) {
	Serial.begin(baud);
	serialIn = "";
}

void SerialInterface::SerialRead(bool& stringChanged, String& output) {
	if (Serial.available() > 0) {
		stringChanged = true;
		while (Serial.available() > 0) {
			serialIn += char(Serial.read());
			delayMicroseconds(100);
		}
		output = serialIn;
		serialIn = "";
	} else {
		stringChanged = false;
		output = "";
	}
}

void SerialInterface::SerialWrite (String toWrite){
	Serial.print(toWrite);
}
