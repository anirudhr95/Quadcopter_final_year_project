#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PID_v1.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>


String readString;
int MotorSpeeds[3];
float *ypr = {{0.0,0.0,0.0}, *ypr_desired = {0.0,0.0,0.0};
float *ypr_stationary = {0.0,0.0,0.0};
double *altitude, *altitude_desired; // Requires barometer

int *UltraValues = {0,0,0,0};

bool should_stabilize = false;  //for hover
bool should_hold_altitude = false; //for holding altitude
// PID myPID(&Input, &Output, &Setpoint,2,5,1, DIRECT);

// YAW DISABLED TILL ACCURATE MAGNETO READING CAN BE OBTAINED. Need to fix direction as well
// To enable, Uncomment following, as well as definitions in Setup(), and stabilize_flight()
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
void quad_takeoff()
{
  set_Mode_Hover(takeoff_prefered_altitude);
}
void quad_land(){
  set_Mode_Hover(0.0);
}
void set_Mode_Altitude_Hold(double desired=0.0) {
  should_hold_altitude =  true;
  id(desired == 0.0){
    altitude = bmp_getAltitude();
    *altitude_desired = *altitude;
  }
  else {
    *altitude_desired = desired; 
  }
}
void remove_Altitude_Hold(){
  should_hold_altitude = false;
}
void refreshYPRA(){
  // Not to be called directly.. Use RefreshPIDS()
  ypr = getYPR();
  altitude = bmp_getAltitude();
}
void set_Mode_Flight(){
  should_stabilize = false;
}
void set_Mode_Hover(double desired=0.0){
  should_stabilize = true;
  *ypr_desired = *ypr_stationary;
  set_Mode_Altitude_Hold(desired);
}
void set_YPR(float *new_ypr){
  if(check_ypr_goodness(new_ypr)){
    set_Mode_Flight();
    *ypr_desired = *new_ypr;
  }
  else{
    set_Mode_Hover();
  }
}

void stabilize_flight(){
  refreshYPRA();
  
  // PID_motor_Yaw_FR.Compute();
  // PID_motor_Yaw_FL.Compute();
  // PID_motor_Yaw_BR.Compute();
  // PID_motor_Yaw_BL.Compute();
  if(should_stabilize){
    PID_motor_Pitch_FR.Compute();
    PID_motor_Pitch_FL.Compute();
    PID_motor_Pitch_BR.Compute();
    PID_motor_Pitch_BL.Compute();
    
    PID_motor_Roll_FR.Compute();
    PID_motor_Roll_FL.Compute();
    PID_motor_Roll_BR.Compute();
    PID_motor_Roll_BL.Compute();
  }
  

  // if(should_hold_altitude){
  //   PID_motor_Altitude_FR.Compute();
  //   PID_motor_Altitude_FL.Compute();
  //   PID_motor_Altitude_BR.Compute();
  //   PID_motor_Altitude_BL.Compute();
  // }
  refreshMotors(motorSpeeds);
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
  stabilize_flight();

  
  // put your main code here, to run repeatedly:
  
  

}
