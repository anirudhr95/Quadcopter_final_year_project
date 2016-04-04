//#include <ServoTimer2.h>

#include <DelaysAndOffsets.h>
#include <Gyro.h>
//#include <Motors.h>
#include <Motors_servotimer.h>
#include <PID_v1.h>
#include <Baro.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>



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
  Serial.begin (115200);
  gyro_Setup();
  ultra_Setup();
  motor_setup();
  

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

  PID_motor_Yaw_FR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Yaw_FL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Yaw_BR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Yaw_BL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Pitch_FR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Pitch_FL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Pitch_BR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Pitch_BL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Roll_FR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Roll_FL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Roll_BR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Roll_BL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Altitude_FR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Altitude_FL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Altitude_BR.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);
  PID_motor_Altitude_BL.SetOutputLimits(motor_Min_Speed,motor_Max_Speed);


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
  //TODO : Decrement very small amount till 0.0!!
  // Use setTunings();
  // Eg : http://playground.arduino.cc/Code/PIDLibraryAdaptiveTuningsExample
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

//UNCOMMENT AFTER REINTRODUCING THE FUNCTION IN GYRO.H ( REMOVED DUE TO MEMORY CONSTRAINTS)
//  if(check_ypr_goodness(new_ypr)){
  if(true){
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

  Serial.print("\nCalib Motor Speeds : ");
  for(int i=0;i<4;i++){
    Serial.print(MotorSpeeds[i]);
    Serial.print("\t");
  }
  
  refreshMotors(MotorSpeeds);
}



void loop() {
  String input;
  if(Serial.available()){
    input = Serial.readString();
    arduinoAction(input);
    
  }
    input=""; //empty for next input
  
  stabilize_flight();
}

void arduinoAction(String action)
{
  if(action=="takeoff")
  {
    Serial.println(F("Taking off!"));
    quad_takeoff();
  }
  else if(action=="land")
  {
    Serial.println(F("Landing"));
     quad_land();
  }
  else if(action=="hover")
  {
    Serial.println(F("Hovering!!"));
    set_Mode_Hover();
  }
  else if(action=="hold_altitude")
  {
    set_Mode_Altitude_Hold();
  }
  else if(action.startsWith("quad_setSpeed"))
  {
    String speed = action.substring(15);
    quad_setSpeed(speed.toInt());

  }
  else if(action.startsWith("set_ypr"))
  {
    String ypr = action.substring(9);
    int first_position , second_position;
    first_position = ypr.indexOf(';');
    second_position = ypr.indexOf(';',first_position+1);

    float setypr[] = {ypr.substring(0,first_position).toFloat(), ypr.substring(first_position+1,second_position).toFloat(), ypr.substring(second_position+1).toFloat()} ;
    
    
    
    set_YPR(setypr);
    //should work - but hey this is arduino!!

  }
}
