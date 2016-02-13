#include <Servo.h>
 
Servo motors[4];
#define NUM_MOTORS (4)
//                      N S W  E
int pins[NUM_MOTORS] = {5,6,11,9};
 
#define ARM_VALUE (22)
#define MAX_VALUE (65)
#define START_VALUE (30)
 
 
void armMotors() {
  Serial.println("Arming motors");
  for (int i=0; i<NUM_MOTORS; i++) {
    motors[i].write(ARM_VALUE);
  }
  Serial.println("Waiting for 7555 milliseconds");
  delay(7555);
  Serial.println("Now running them at value 38 for 1111");
  for (int i=0; i<NUM_MOTORS; i++) {
    motors[i].write(38);
  }
  delay(1111);
  Serial.println("Back to ARM_VALUE");
  for (int i=0; i<NUM_MOTORS; i++) {
    motors[i].write(ARM_VALUE);
  }
  Serial.println("Finished");
}
 
void setup()
{
  for (int i=0; i<NUM_MOTORS; i++) {
    motors[i].attach(pins[i]);
  }
 
  Serial.begin(19200);
 
  armMotors();
}
 
 
void loop()
{
  static int currentMotor = -1;
  static int volt = 0;
 
  if (Serial.available() > 0) {
    byte cur = Serial.read();
    if ( (cur >= '0' && cur <= '9') || cur == 'n' || cur == 'N') {
      if (currentMotor == -1) {
        currentMotor = cur - '0';
        if (currentMotor < 0 || currentMotor >= NUM_MOTORS) {
          currentMotor = -1;
        }
        Serial.print("Motor number ");
        Serial.println(currentMotor, DEC);
      } else {
        if (cur == 'n') {
          if (currentMotor >= 0 && currentMotor < NUM_MOTORS) {
            if (volt < ARM_VALUE || volt > MAX_VALUE) {
              volt = ARM_VALUE;
            }
            motors[currentMotor].write(volt);
            Serial.print("Power = ");
            Serial.println(volt, DEC);
          }
          volt = 0;
          currentMotor = -1;
        }
        else {
          volt = volt * 10 + cur - '0';
        }
      }
    }
  }
}
asd  
