#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>

void setup(){
  Serial.begin(38400);
  gyro_Setup();
  
}
void loop(){
 float *ypr = getYPR();
 Serial.print("ypr\t");
 Serial.print(ypr[0]);
 Serial.print("\t");
 Serial.print(ypr[1]);
 Serial.print("\t");
 Serial.print(ypr[2]);
 getMag();
 Serial.println();
 delay(500);

// VectorInt16 aaReal = getAccel();
// Serial.print("areal\t");
// Serial.print(aaReal.x);
// Serial.print("\t");
// Serial.print(aaReal.y);
// Serial.print("\t");
// Serial.println(aaReal.z);
//  delay(500);
}

