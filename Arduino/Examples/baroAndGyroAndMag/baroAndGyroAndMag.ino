#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <PinoutConfig.h>
#include <Baro.h>

void setup() {
  
   Serial.begin(115200);
   
   gyro_Setup();
   baro_Setup();
   
   
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
 Serial.print(heading);
 delay(50);
 Serial.println(baro_getAltitude());
// delay(2000);
 
}
