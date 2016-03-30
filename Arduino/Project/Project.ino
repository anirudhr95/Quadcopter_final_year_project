#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PID_v1.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>


String readString;
int MotorSpeeds[3];
float *ypr, *ypr_desired;
float *ypr_stationary = {0.0,0.0,0.0}
float *altitude, *altitude_desired; // Requires barometer

bool should_stabilize = false;  //for hover
bool should_hold_altitude = false; //for holding altitude
// PID myPID(&Input, &Output, &Setpoint,2,5,1, DIRECT);

// YAW DISABLED TILL ACCURATE MAGNETO READING CAN BE OBTAINED. Need to fix direction as well
// To enable, Uncomment following, as well as definitions in Setup(), and refreshPIDS()
// YAW
// PID PID_motor_Yaw_FR(&ypr[0], MotorSpeeds[0], &desired_ypr[0], Kp, Ki, Kd, REVERSE);
// PID PID_motor_Yaw_FL(&ypr[0], MotorSpeeds[1], &desired_ypr[0], Kp, Ki, Kd, REVERSE);
// PID PID_motor_Yaw_BR(&ypr[0], MotorSpeeds[2], &desired_ypr[0], Kp, Ki, Kd, REVERSE);
// PID PID_motor_Yaw_BL(&ypr[0], MotorSpeeds[3], &desired_ypr[0], Kp, Ki, Kd, REVERSE);

// PITCH
PID PID_motor_Pitch_FR(&ypr[1], MotorSpeeds[0], &desired_ypr[1], Kp, Ki, Kd, REVERSE);
PID PID_motor_Pitch_FL(&ypr[1], MotorSpeeds[1], &desired_ypr[1], Kp, Ki, Kd, REVERSE);
PID PID_motor_Pitch_BR(&ypr[1], MotorSpeeds[2], &desired_ypr[1], Kp, Ki, Kd, DIRECT);
PID PID_motor_Pitch_BL(&ypr[1], MotorSpeeds[3], &desired_ypr[1], Kp, Ki, Kd, DIRECT);
// ROLL
PID PID_motor_Roll_FR(&ypr[2], MotorSpeeds[0], &desired_ypr[2], Kp, Ki, Kd, REVERSE);
PID PID_motor_Roll_FL(&ypr[2], MotorSpeeds[1], &desired_ypr[2], Kp, Ki, Kd, DIRECT);
PID PID_motor_Roll_BR(&ypr[2], MotorSpeeds[2], &desired_ypr[2], Kp, Ki, Kd, REVERSE);
PID PID_motor_Roll_BL(&ypr[2], MotorSpeeds[3], &desired_ypr[2], Kp, Ki, Kd, DIRECT);

// Commented until Barometer is obtained
// ALTITUDE 
// PID PID_motor_Altitude_FR(&altitude, MotorSpeeds[0], &altitude_desired, Kp, Ki, Kd, REVERSE);
// PID PID_motor_Altitude_FL(&altitude, MotorSpeeds[1], &altitude_desired, Kp, Ki, Kd, REVERSE);
// PID PID_motor_Altitude_BR(&altitude, MotorSpeeds[2], &altitude_desired, Kp, Ki, Kd, REVERSE);
// PID PID_motor_Altitude_BL(&altitude, MotorSpeeds[3], &altitude_desired, Kp, Ki, Kd, REVERSE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  ultra_Setup();
  motor_setup();
  gyro_Setup();

  // PID_motor_Yaw_FR.setMode(AUTOMATIC);
  // PID_motor_Yaw_FL.setMode(AUTOMATIC);
  // PID_motor_Yaw_BR.setMode(AUTOMATIC);
  // PID_motor_Yaw_BL.setMode(AUTOMATIC);

  PID_motor_Pitch_FR.setMode(AUTOMATIC);
  PID_motor_Pitch_FL.setMode(AUTOMATIC);
  PID_motor_Pitch_BR.setMode(AUTOMATIC);
  PID_motor_Pitch_BL.setMode(AUTOMATIC);

  PID_motor_Roll_FR.setMode(AUTOMATIC);
  PID_motor_Roll_FL.setMode(AUTOMATIC);
  PID_motor_Roll_BR.setMode(AUTOMATIC);
  PID_motor_Roll_BL.setMode(AUTOMATIC);

  // PID_motor_Altitude_FR.setMode(AUTOMATIC);
  // PID_motor_Altitude_FL.setMode(AUTOMATIC);
  // PID_motor_Altitude_BR.setMode(AUTOMATIC);
  // PID_motor_Altitude_BL.setMode(AUTOMATIC);


  Serial.print("Setup Completed");
  Serial.print("Yaw\tPitch\tRoll\tAx\tAy\tAz\t\tUA\tUB\tUC\tRF\tRL\tBR\tBL");

}
void refreshYPR(){
  ypr = getYPR();
  if(should_stabilize)
    *ypr_desired = *ypr_stationary;

}
void refreshMotors(){
  motor_Set_Speed_FR(MotorSpeeds[0]);
  motor_Set_Speed_FL(MotorSpeeds[1]);
  motor_Set_Speed_BR(MotorSpeeds[2]);
  motor_Set_Speed_BL(MotorSpeeds[3]);
}
void refreshPIDS(){
  refreshYPR();
  
  // PID_motor_Yaw_FR.Compute();
  // PID_motor_Yaw_FL.Compute();
  // PID_motor_Yaw_BR.Compute();
  // PID_motor_Yaw_BL.Compute();

  PID_motor_Pitch_FR.Compute();
  PID_motor_Pitch_FL.Compute();
  PID_motor_Pitch_BR.Compute();
  PID_motor_Pitch_BL.Compute();
  
  PID_motor_Roll_FR.Compute();
  PID_motor_Roll_FL.Compute();
  PID_motor_Roll_BR.Compute();
  PID_motor_Roll_BL.Compute();

  // if(should_hold_altitude){
  //   PID_motor_Altitude_FR.Compute();
  //   PID_motor_Altitude_FL.Compute();
  //   PID_motor_Altitude_BR.Compute();
  //   PID_motor_Altitude_BL.Compute();
  // }
  refreshMotors();
}

void printData(){ 
  float *ypr = getYPR();
  Serial.print("ypr\t");
  Serial.print(ypr[0]);
  Serial.print("\t");
  Serial.print(ypr[1]);
  Serial.print("\t");
  Serial.print(ypr[2]);


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
  Serial.print(ultragetB());
  Serial.print("\t");
  Serial.print(ultragetC());
  Serial.print("\t");
  Serial.print(ultragetD());

//  Serial.print(ultragetA());
//  Serial.print("\t");
//  delay(50);


//  MOTOR
  for(int i=0;i<=3;i++){
    Serial.print(motorSpeeds[i]);
    Serial.print("\t");
  }
  Serial.println();

  
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
  
  

}
