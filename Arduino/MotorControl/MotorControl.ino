
#include "Motors.h"

String readString;
String x = "";

void setup() {
  
  Serial.begin(9600);
   motor_setup();
}


void loop() {
  
//  
  while (Serial.available()) {
    char c = Serial.read();  //gets one byte from serial bufferaa
    
    readString += c; //makes the string readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (readString.length() >0) {
    Serial.println(readString);  //so you can see the captured string 
    int n = readString.toInt();  //convert readString into a number
    
    motor_Set_Speed(n);
    Serial.print("\nInput speed is :");
    for(int i=0;i<=3;i++){
      Serial.print(motor_Get_Speed()[i]);
      Serial.print("\t");
    }
    
    readString=""; //empty for next input
  } 
  
}
