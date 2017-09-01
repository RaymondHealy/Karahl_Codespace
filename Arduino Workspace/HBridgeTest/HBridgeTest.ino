const uint8_t reversePin = 22;
const uint8_t pwmPin = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(reversePin,OUTPUT);
  pinMode(pwmPin,OUTPUT);

  digitalWrite(reversePin, LOW);
  analogWrite(pwmPin, 255);
}

void loop() {
  // put your main code here, to run repeatedly:

}
