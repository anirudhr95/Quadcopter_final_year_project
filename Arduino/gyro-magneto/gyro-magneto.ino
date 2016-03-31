#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PinoutConfig.h>
#include <printHelper.h>
#include <UltrasoundSense.h>

void setup() {
  
   Serial.begin(9600);
   gyro_Setup();
   
}

void loop() {

float *ypr = getYPR();
 Serial.print("ypr\t");
 Serial.print(ypr[0]);
 Serial.print("\t");
 Serial.print(ypr[1]);
 Serial.print("\t");
 Serial.print(ypr[2]);
 Serial.print("\t");
// Serial.print("\n");

 float *mag = getMAG();
 for(int i=0;i<3;i++){
  Serial.print(mag[i]);
  Serial.print("\t");
 }
 float heading = getHeading();
 Serial.println(heading);
}
