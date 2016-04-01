#include <Servo.h>

Servo a,b,c,d;
#define motor_FR_Pin 10
#define motor_FL_Pin 6
#define motor_BR_Pin 12
#define motor_BL_Pin 13
int n;
void setup() {
  
  Serial.begin(9600);
  a.attach(motor_FR_Pin,2000,1000);  //the pin for the servo control 
  b.attach(motor_FL_Pin,2000,1000); 
  c.attach(motor_BR_Pin,2000,1000); 
  d.attach(motor_BL_Pin,2000,1000);
  arm();
}
void arm(){
  motor_Set_Speed(2000);
  Serial.println("Enter any key after connecting power ");
  while(!Serial.available());
  Serial.println("Calibrating..");
  delay(8000);
  motor_Set_Speed(1000);
  delay(5000);
  motor_Set_Speed(1500);
  Serial.println("Calibration completed..");
  
}

void motor_Set_Speed(int n){
  a.writeMicroseconds(n);
  b.writeMicroseconds(n);
  c.writeMicroseconds(n);
  d.writeMicroseconds(n);
}
void loop() {   
  
  if(Serial.available()){
    n=Serial.parseInt();
    motor_Set_Speed(n);  
    Serial.println(n);
    Serial.print("\nEnter Speed : ");
  }
  
  
    

  
  
}

