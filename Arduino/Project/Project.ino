#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors.h>
#include <PID_v1.h>
#include <Baro.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>


String readString;
double MotorSpeeds[3];
double ypr_current[] = {0.0,0.0,0.0}, ypr_desired[] = {0.0,0.0,0.0};
double ypr_stationary[] = {0.0,0.0,0.0};
double altitude_current, altitude_desired; // Requires barometer

int UltraValues[] = {0,0,0,0};

bool should_stabilize = false;  //for hover
bool should_hold_altitude = false; //for holding altitude
// PID myPID(&Input, &Output, &Setpoint,2,5,1, DIRECT);


void quad_takeoff();
void quad_land();
void set_Mode_Altitude_Hold() ;
void remove_Altitude_Hold();
void quad_setSpeed(int speed);
void refreshYPRA();
void set_Mode_Flight();
void set_Mode_Hover();
void set_YPR(float new_ypr[]);
void stabilize_flight();


// YAW DISABLED TILL ACCURATE MAGNETO READING CAN BE OBTAINED. Need to fix direction as well
// To enable, Uncomment following, as well as definitions in Setup(), and stabilize_flight()
// YAW
PID PID_motor_Yaw_FR(&ypr_current[0], &MotorSpeeds[0], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
PID PID_motor_Yaw_FL(&ypr_current[0], &MotorSpeeds[1], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
PID PID_motor_Yaw_BR(&ypr_current[0], &MotorSpeeds[2], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
PID PID_motor_Yaw_BL(&ypr_current[0], &MotorSpeeds[3], &ypr_desired[0], Kp, Ki, Kd, REVERSE);

// PITCH
PID PID_motor_Pitch_FR(&ypr_current[1], &MotorSpeeds[0], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
PID PID_motor_Pitch_FL(&ypr_current[1], &MotorSpeeds[1], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
PID PID_motor_Pitch_BR(&ypr_current[1], &MotorSpeeds[2], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
PID PID_motor_Pitch_BL(&ypr_current[1], &MotorSpeeds[3], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
// ROLL
PID PID_motor_Roll_FR(&ypr_current[2], &MotorSpeeds[0], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
PID PID_motor_Roll_FL(&ypr_current[2], &MotorSpeeds[1], &ypr_desired[2], Kp, Ki, Kd, DIRECT);
PID PID_motor_Roll_BR(&ypr_current[2], &MotorSpeeds[2], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
PID PID_motor_Roll_BL(&ypr_current[2], &MotorSpeeds[3], &ypr_desired[2], Kp, Ki, Kd, DIRECT);

// Commented until Barometer is obtained
// ALTITUDE 
PID PID_motor_Altitude_FR(&altitude_current, &MotorSpeeds[0], &altitude_desired, Kp, Ki, Kd, REVERSE);
PID PID_motor_Altitude_FL(&altitude_current, &MotorSpeeds[1], &altitude_desired, Kp, Ki, Kd, REVERSE);
PID PID_motor_Altitude_BR(&altitude_current, &MotorSpeeds[2], &altitude_desired, Kp, Ki, Kd, REVERSE);
PID PID_motor_Altitude_BL(&altitude_current, &MotorSpeeds[3], &altitude_desired, Kp, Ki, Kd, REVERSE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  ultra_Setup();
  motor_setup();
  gyro_Setup();

  PID_motor_Yaw_FR.SetMode(AUTOMATIC);
  PID_motor_Yaw_FL.SetMode(AUTOMATIC);
  PID_motor_Yaw_BR.SetMode(AUTOMATIC);
  PID_motor_Yaw_BL.SetMode(AUTOMATIC);

  PID_motor_Pitch_FR.SetMode(AUTOMATIC);
  PID_motor_Pitch_FL.SetMode(AUTOMATIC);
  PID_motor_Pitch_BR.SetMode(AUTOMATIC);
  PID_motor_Pitch_BL.SetMode(AUTOMATIC);

  PID_motor_Roll_FR.SetMode(AUTOMATIC);
  PID_motor_Roll_FL.SetMode(AUTOMATIC);
  PID_motor_Roll_BR.SetMode(AUTOMATIC);
  PID_motor_Roll_BL.SetMode(AUTOMATIC);

  PID_motor_Altitude_FR.SetMode(AUTOMATIC);
  PID_motor_Altitude_FL.SetMode(AUTOMATIC);
  PID_motor_Altitude_BR.SetMode(AUTOMATIC);
  PID_motor_Altitude_BL.SetMode(AUTOMATIC);


  Serial.print("Setup Completed");
  Serial.print("Yaw\tPitch\tRoll\tAx\tAy\tAz\t\tUA\tUB\tUC\tRF\tRL\tBR\tBL");

}
void quad_takeoff()
{
  set_Mode_Hover();
  set_Mode_Altitude_Hold_At(takeoff_prefered_altitude);
}
void set_Mode_Altitude_Hold_At(double prefered_altitude) {
  should_hold_altitude =  true;
  altitude_current = baro_getAltitude();
  altitude_desired = prefered_altitude; 
}
void quad_land(){
  
  set_Mode_Altitude_Hold_At(0.0);
}
void set_Mode_Altitude_Hold() {
  should_hold_altitude =  true;
  altitude_current = baro_getAltitude();
  altitude_desired = altitude_current; 
}
void remove_Altitude_Hold(){
  should_hold_altitude = false;
}
void quad_setSpeed(int speed){

  motor_Set_Speed(speed);
  set_Mode_Hover();
}
void refreshYPRA(){
  // Not to be called directly.. Use RefreshPIDS()
  float *asas= getYPR();
  for(int i=0;i<3;i++)
    ypr_current[i] = double(asas[i]);
  altitude_current = baro_getAltitude();
}
void set_Mode_Flight(){
  should_stabilize = false;
}
void set_Mode_Hover(){
  should_stabilize = true;
  for(int i=0;i<3;i++)
    ypr_desired[i] = ypr_stationary[i];
  set_Mode_Altitude_Hold();
}
void set_YPR(float new_ypr[]){
  if(check_ypr_goodness(new_ypr)){
    set_Mode_Flight();
    for(int i=0;i<3;i++)
      ypr_desired[i] = new_ypr[i];
  }
  else{
    set_Mode_Hover();
  }
}

void stabilize_flight(){
  refreshYPRA();
  
  PID_motor_Yaw_FR.Compute();
  PID_motor_Yaw_FL.Compute();
  PID_motor_Yaw_BR.Compute();
  PID_motor_Yaw_BL.Compute();
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
  

  if(should_hold_altitude){
    PID_motor_Altitude_FR.Compute();
    PID_motor_Altitude_FL.Compute();
    PID_motor_Altitude_BR.Compute();
    PID_motor_Altitude_BL.Compute();
  }
  
  refreshMotors(MotorSpeeds);
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
