#include "Gyro.h"
void setup(){
  Serial.begin(9600);
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
 Serial.print("\n");

 VectorInt16 aaReal = getAccel();
 Serial.print("areal\t");
 Serial.print(aaReal.x);
 Serial.print("\t");
 Serial.print(aaReal.y);
 Serial.print("\t");
 Serial.println(aaReal.z);
  
}

