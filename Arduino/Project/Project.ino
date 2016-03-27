#import "UltrasoundSense.h"
#import "Motors.h"
#import "Gyro.h"
void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  ultraSetup();
  motor_setup();
  gyro_Setup();
}

void loop() {
  // put your main code here, to run repeatedly:

}
