#include <bmpAltitude.h>
#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PinoutConfig.h>
#include <printHelper.h>
#include <UltrasoundSense.h>

String readString;

void setup() {
  
  Serial.begin(9600);
  
   motor_setup();
}


void loop() {   
  
  Serial.println("Enter 'r' to read speed, 'w' to write : ");
  
  
  while(!Serial.available());
  
  readString = Serial.readString();
  if(readString.equals("r"))
  {
    Serial.print("\nCurrent speed is :");
    int *speeds= motor_Get_Speed();
    
    for(int i=0;i<=3;i++)
    {
      Serial.print(speeds[i]);
      Serial.print("\t");
    }
  }
  else if(readString.equals("w")){
    Serial.println("Enter new speed : ");
    while(!Serial.available());
    motor_Set_Speed(Serial.parseInt());
  }
  
  readString=""; //empty for next input
  
}
