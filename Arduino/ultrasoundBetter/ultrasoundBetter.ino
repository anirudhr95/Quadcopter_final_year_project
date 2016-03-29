#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>


void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
    digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);

  ultra_Setup();
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(ultragetA());
  Serial.print("\t");
  delay(500);
  Serial.println(ultragetB());
    delay(500);
//  Serial.println(ultragetC());
  
//    float *a = getABCD();
//    for(int i=0;i<=3;i++){
//      Serial.print(a[i]);
//      Serial.print("\t\t\t");
//    }
//    Serial.println();
//    Serial.flush();
    
}
