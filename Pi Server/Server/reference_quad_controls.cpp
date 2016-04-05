# PID PID_motor_Yaw_FR(&ypr_current[0], &MotorSpeeds[0], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_FL(&ypr_current[0], &MotorSpeeds[1], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_BR(&ypr_current[0], &MotorSpeeds[2], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_BL(&ypr_current[0], &MotorSpeeds[3], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
#
# // PITCH
# PID PID_motor_Pitch_FR(&ypr_current[1], &MotorSpeeds[0], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Pitch_FL(&ypr_current[1], &MotorSpeeds[1], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Pitch_BR(&ypr_current[1], &MotorSpeeds[2], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
# PID PID_motor_Pitch_BL(&ypr_current[1], &MotorSpeeds[3], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
# // ROLL
# PID PID_motor_Roll_FR(&ypr_current[2], &MotorSpeeds[0], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Roll_FL(&ypr_current[2], &MotorSpeeds[1], &ypr_desired[2], Kp, Ki, Kd, DIRECT);
# PID PID_motor_Roll_BR(&ypr_current[2], &MotorSpeeds[2], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Roll_BL(&ypr_current[2], &MotorSpeeds[3], &ypr_desired[2], Kp, Ki, Kd, DIRECT);
#
# // Commented until Barometer is obtained
# // ALTITUDE
# PID PID_motor_Altitude_FR(&altitude_current, &MotorSpeeds[0], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_FL(&altitude_current, &MotorSpeeds[1], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_BR(&altitude_current, &MotorSpeeds[2], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_BL(&altitude_current, &MotorSpeeds[3], &altitude_desired, Kp, Ki, Kd, REVERSE);
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