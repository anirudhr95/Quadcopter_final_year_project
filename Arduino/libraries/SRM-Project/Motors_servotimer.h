	//
	//  Motors.h
	//
	//
	//  Created by Shyam Ravikumar on 26/03/16.
	//
	//

#ifndef Motors_h
#define Motors_h


#include "DelaysAndOffsets.h"
#include "PinoutConfig.h"
#include "printHelper.h"

#if USE_SERVOTIMER2
	#include <ServoTimer2.h>
	ServoTimer2 motor[4];

#else
	#include<Servo.h>
	Servo motor[4];
#endif





// int motor_Get_Speed_FR(){
// 	return a.read();
// }
// int motor_Get_Speed_FL(){
// 	return b.read();
// }
// int motor_Get_Speed_BR(){
// 	return c.read();
// }
// int motor_Get_Speed_BL(){
// 	return d.read();
// }
// int *motor_Get_Speed(){
// 	int as[4];
// 	as[0] = motor_Get_Speed_FR();
// 	as[1] = motor_Get_Speed_FL();
// 	as[2] = motor_Get_Speed_BR();
// 	as[3] = motor_Get_Speed_BL();
// 	return as;
// }
void __motor_set_speed__(int index, int speed){
	#if USE_SERVOTIMER2
	motor[index].write(speed + motor_offsets[index]);
	#else
	motor[index].writeMicroseconds(speed + motor_offsets[index]);
	#endif
}
void motor_Set_Speed_FR(int n){
	__motor_set_speed__(0,n);
}
void motor_Set_Speed_FL(int n){
	__motor_set_speed__(1,n);
}
void motor_Set_Speed_BR(int n){
	__motor_set_speed__(2,n);
}
void motor_Set_Speed_BL(int n){
	__motor_set_speed__(3,n);
}
void refreshMotors(int MotorSpeeds[]){
	motor_Set_Speed_FR(MotorSpeeds[0]);
	motor_Set_Speed_FL(MotorSpeeds[1]);
	motor_Set_Speed_BR(MotorSpeeds[2]);
	motor_Set_Speed_BL(MotorSpeeds[3]);
#if PRINT_MOTOR_CHANGES
	char buf[30];
	sprintf(buf, FORMAT_MOTOR_SPEEDS, MotorSpeeds[0],MotorSpeeds[1],MotorSpeeds[2],MotorSpeeds[3]);
	Serial.print(buf);
#endif
}



void motor_Set_Speed(int n){
	
	motor_Set_Speed_FR(n);
	motor_Set_Speed_FL(n);
	motor_Set_Speed_BL(n);
	motor_Set_Speed_BR(n);
#ifdef PRINT_MOTOR_CHANGES
	char buf[30];
	sprintf(buf, FORMAT_MOTOR_SPEEDS, n,n,n,n);
	Serial.print(buf);
#endif
}
void motor_setup(){
		//  Arming Process
	char buf[100];
	sprintf(buf,FORMAT_SETUP_INIT,"MOTOR");
	Serial.print(buf);
	
	
	motor[0].attach(motor_FR_Pin);  //the pin for the servo control
	motor[1].attach(motor_FL_Pin);
	motor[2].attach(motor_BR_Pin);
	motor[3].attach(motor_BL_Pin);
	
		// Arming speed should be LOW for sometime, to instruct the ESC that it is in "WORKING" mode
	motor_Set_Speed(1000);
	
	delay(motor_Arm_Delay);
	
	sprintf(buf,FORMAT_SETUP_SUCCESS,"MOTOR");
}
/*
 To calibrate motors, use motor_calibrate() function.. Concept : max(2000) microsecond pulse is applied, and power is connected. After some time, a musical note will be heard, signifying that calibration has started. Now apply Min(1000) pulse.Wait for 5 seconds, and remove power.
 */
void motor_calibrate(){
	motor[0].attach(motor_FR_Pin);  //the pin for the servo control
	motor[1].attach(motor_FL_Pin);
	motor[2].attach(motor_BR_Pin);
	motor[3].attach(motor_BL_Pin);
	Serial.println(F("Beginning Calibration.."));
	Serial.println(F("Please remove power to motors.. Once done, press any key.."));
	while(!Serial.available());
	motor_Set_Speed(motor_Max_Speed);
	Serial.println(F("Connect Power, and immediately press any key to continue..."));
	while(!Serial.available());
	Serial.println(F("Calibrating.."));
	delay(3000);
	motor_Set_Speed(motor_Min_Speed);
	delay(5000);
	motor_Set_Speed(1500);
	
	Serial.println(F("Calibration completed.."));
	Serial.println(F("If all motors are spinning, calibration is successful..Restart program if not confirmed\nPress any key to stop motors.."));
	while(!Serial.available());
	motor_Set_Speed(motor_Min_Speed);
}
#endif /* Motors_h */
