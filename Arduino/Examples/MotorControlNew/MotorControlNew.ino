#include <DelaysAndOffsets.h>
//#include <Motors.h>
#include <Motors_servotimer.h>
#include <PinoutConfig.h>


int n;
String readString;

void setup() {
  
  Serial.begin(115200);
  
   motor_setup();
}


void loop() {   
  
//  Serial.println("Enter 'r' to read speed, 'w' to write : ");
//  Serial.println("Enter Speed");
  Serial.print("Enter new speed : ");
  while(!Serial.available());
  
//  readString = Serial.readString();
//  if(readString.equals("r"))
//  {
//    Serial.print("\nCurrent speed is :");
//    int *speeds= motor_Get_Speed();
//    
//    for(int i=0;i<=3;i++)
//    {
//      Serial.print(speeds[i]);
//      Serial.print("\t");
//    }
//  }
//  else if(readString.equals("w")){
    
    while(!Serial.available());
    n=Serial.parseInt();
    motor_Set_Speed(n);
    Serial.println(n);
//  }
  
  readString=""; //empty for next input
  
}
