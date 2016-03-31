#include <DelaysAndOffsets.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  ultra_Setup();
}

void loop() {
  
  // put your main code here, to run repeatedly:
  float *a = getABCD();
  for(int i=0;i<4;i++){
  Serial.print(a[i]);
  Serial.print("\t");}
  Serial.println();
Serial.println();
delay(1000);
  
    

}
