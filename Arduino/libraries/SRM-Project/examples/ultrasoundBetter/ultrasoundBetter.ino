#include <DelaysAndOffsets.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>
unsigned int *vals;
void setup() {
  // put your setup code here, to run once:
  Serial.begin (115200);
  ultra_Setup();
}

void loop() {
  ultra_Compute();
}
