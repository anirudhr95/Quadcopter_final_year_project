#import "UltrasoundSense.h"
#import "Motors.h"
#import "Gyro.h"

String readString;


void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  ultra_Setup();
  motor_setup();
  gyro_Setup();
  Serial.print("Yaw\tPitch\tRoll\tAx\tAy\tAz\t\tUA\tUB\tUC\tRF\tRL\tBR\tBL");
}

void loop() {

  while (Serial.available()) {
    char c = Serial.read();  //gets one byte from serial bufferaa
    
    readString += c; //makes the string readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (readString.length() >0) {
    Serial.println(readString);  //so you can see the captured string 
    if(readString=="w"){
      while(!Serial.available());
          while (Serial.available()) {
        readString="";
        char c = Serial.read();  //gets one byte from serial bufferaa
        
        readString += c; //makes the string readString
        delay(2);  //slow looping to allow buffer to fill with next character
      }
      int n = readString.toInt();  //convert readString into a number
      motor_Set_Speed(n);
    }
    
    readString=""; //empty for next input
  } 
  SoftwareServo::refresh();

  
  // put your main code here, to run repeatedly:
  
  
  float *ypr = getYPR();
  Serial.print("ypr\t");
  Serial.print(ypr[0]);
  Serial.print("\t");
  Serial.print(ypr[1]);
  Serial.print("\t");
  Serial.print(ypr[2]);
// Serial.print("\n");

  VectorInt16 aaReal = getAccel();
  Serial.print("areal\t");
  Serial.print(aaReal.x);
  Serial.print("\t");
  Serial.print(aaReal.y);
  Serial.print("\t");
  Serial.println(aaReal.z);

// Ultrasonic
  Serial.print(ultragetA());
  Serial.print("\t");
  delay(50);
  Serial.print(ultragetB());
  Serial.print("\t");
  delay(50);
  Serial.print(ultragetC());
  Serial.print("\t");
  delay(50);
//  Serial.print(ultragetA());
//  Serial.print("\t");
//  delay(50);


//  MOTOR
  for(int i=0;i<=3;i++){
    Serial.print(motor_Get_Speed()[i]);
    Serial.print("\t");
  }
  Serial.print("\n");

  delay(1000);
  

}
