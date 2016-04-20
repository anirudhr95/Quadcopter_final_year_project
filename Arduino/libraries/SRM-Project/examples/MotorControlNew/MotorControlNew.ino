#include <DelaysAndOffsets.h>
#include <Motors_servotimer.h>
#include <PinoutConfig.h>


int n;
void setup() {
  
  Serial.begin(115200);
  
   motor_setup();
   Serial.print(F("Enter new speed : "));
}


void loop() {   
  
    if(Serial.available()){
      n=Serial.parseInt(); 
      Serial.println(n); 
      Serial.print(F("Enter new speed : "));
    }
    motor_Set_Speed(n);
}
