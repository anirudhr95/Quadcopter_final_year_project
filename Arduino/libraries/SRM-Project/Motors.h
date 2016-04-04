//
//  Motors.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//
/* 
To calibrate motors, use Calibrate() function.. Concept : max(2000) microsecond pulse is applied, and power is connected. After some time, a musical note will be heard, signifying that calibration has started. Now apply Min(1000) pulse.Wait for 5 seconds, and remove power.
*/
#ifndef Motors_h
#define Motors_h
#include <Servo.h>
#include "DelaysAndOffsets.h"
#include "PinoutConfig.h"

Servo a,b,c,d;
int speeds[3];





int motor_Get_Speed_FR(){
	return speeds[0];
}
int motor_Get_Speed_FL(){
	return speeds[1];
}
int motor_Get_Speed_BR(){
	return speeds[2];
}
int motor_Get_Speed_BL(){
	return speeds[3];
}
int *motor_Get_Speed(){
	return speeds;
}

void motor_Set_Speed_FR(int n){
	a.writeMicroseconds(n + motor_FR_Offset);
	speeds[0] = n + motor_FR_Offset;
		delay(motor_small_delay);
}
void motor_Set_Speed_FL(int n){
	b.writeMicroseconds(n + motor_FL_Offset);
	speeds[1] =n + motor_FL_Offset;
		delay(motor_small_delay);
}
void motor_Set_Speed_BR(int n){
	c.writeMicroseconds(n + motor_BR_Offset);
	speeds[2] =n + motor_BR_Offset;
		delay(motor_small_delay);
}
void motor_Set_Speed_BL(int n){
	d.writeMicroseconds(n + motor_BL_Offset);
	speeds[3] =n + motor_BL_Offset;
		delay(motor_small_delay);
}
void refreshMotors(double MotorSpeeds[]){
  motor_Set_Speed_FR(int(MotorSpeeds[0]));
  motor_Set_Speed_FL(int(MotorSpeeds[1]));
  motor_Set_Speed_BR(int(MotorSpeeds[2]));
  motor_Set_Speed_BL(int(MotorSpeeds[3]));
}



void motor_Set_Speed(int n){
	
	motor_Set_Speed_FR(n);
	
	motor_Set_Speed_FL(n);
	
	motor_Set_Speed_BL(n);
	motor_Set_Speed_BR(n);
	
	
	
	
	
	Serial.println("Speed set to " + String(n));
	
}
void motor_setup(){
//  Arming Process
	Serial.println(F("Arming motors..."));
	a.attach(motor_FR_Pin,2000,1000);  //the pin for the servo control
	b.attach(motor_FL_Pin,2000,1000);
	c.attach(motor_BR_Pin,2000,1000);
	d.attach(motor_BL_Pin,2000,1000);
	
	// Arming speed should be 0 for sometime
	a.writeMicroseconds(000);
	b.writeMicroseconds(000);
	c.writeMicroseconds(000);
	d.writeMicroseconds(000);
	delay(motor_Arm_Delay);
  	
	
  	Serial.println(F("Motors Armed..."));
	// Serial.println("Arming Completed"); // so I can keep track of what is loaded
}

void motor_calibrate(){
	Serial.println(F("Please remove power to motors.. Once done, press (1)"));
	while(!Serial.available());
	int read = Serial.parseInt();
	if(read==1){
		a.writeMicroseconds(2000);
		b.writeMicroseconds(2000);
		c.writeMicroseconds(2000);
		d.writeMicroseconds(2000);
		Serial.println(F("Connect Power, and wait for melody.. Once you hear that, press any key to continue..."));
		while(!Serial.available());
		Serial.println(F("Calibrating.."));
  		delay(8000);
		a.writeMicroseconds(1000);
		b.writeMicroseconds(1000);
		c.writeMicroseconds(1000);
		d.writeMicroseconds(1000);
		delay(5000);
		motor_Set_Speed(1500);
  		Serial.println(F("Calibration completed.."));
		Serial.println(F("If all motors are spinning, calibration is successful..Restart program if not confirmed"));
	}
	else{
		motor_calibrate();

	}

}
#endif /* Motors_h */
