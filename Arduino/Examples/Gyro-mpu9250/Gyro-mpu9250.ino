#include <Mpu.h>
<<<<<<< refs/remotes/origin/develop
unsigned long timer;
=======
>>>>>>> Changed gyro.h to support MPU.. initial tests - Works
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
   
   gyro_Setup();

}

void loop() {
  // put your main code here, to run repeatedly:
<<<<<<< refs/remotes/origin/develop
  timer = millis();
float *ypr = getYPR();
 timer = millis() - timer;
=======
float *ypr = getYPR();
>>>>>>> Changed gyro.h to support MPU.. initial tests - Works
 Serial.print("ypr\t");
 Serial.print(ypr[0]);
 Serial.print("\t");
 Serial.print(ypr[1]);
 Serial.print("\t");
 Serial.print(ypr[2]);
<<<<<<< refs/remotes/origin/develop
 Serial.print("\t");
 Serial.println(timer);
 
=======
>>>>>>> Changed gyro.h to support MPU.. initial tests - Works
}
