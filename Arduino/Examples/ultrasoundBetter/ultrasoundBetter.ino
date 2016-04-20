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
<<<<<<< HEAD
  
  // put your main code here, to run repeatedly:
  Serial.println(ultragetB());
//  float *a = getABCD();
//  for(int i=0;i<4;i++){
//  Serial.print(a[i]);
//  Serial.print("\t");}
//  Serial.println();
Serial.println();
delay(1000);
  
    

=======
  ultra_Compute();
>>>>>>> develop
}
