#include <Mpu.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
   
   gyro_Setup();

}

void loop() {
  // put your main code here, to run repeatedly:
float *ypr = getYPR();
 Serial.print("ypr\t");
 Serial.print(ypr[0]);
 Serial.print("\t");
 Serial.print(ypr[1]);
 Serial.print("\t");
 Serial.print(ypr[2]);
}
