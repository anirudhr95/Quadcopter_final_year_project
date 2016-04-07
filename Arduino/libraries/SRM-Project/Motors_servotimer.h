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
// #include <Servo.h>
#include <ServoTimer2.h>
#include "DelaysAndOffsets.h"
#include "PinoutConfig.h"

ServoTimer2 a,b,c,d;





int motor_Get_Speed_FR(){
	return a.read();
}
int motor_Get_Speed_FL(){
	return b.read();
}
int motor_Get_Speed_BR(){
	return c.read();
}
int motor_Get_Speed_BL(){
	return d.read();
}
int *motor_Get_Speed(){
	int as[4];
	as[0] = motor_Get_Speed_FR();
	as[1] = motor_Get_Speed_FL();
	as[2] = motor_Get_Speed_BR();
	as[3] = motor_Get_Speed_BL();
	return as;
}

void motor_Set_Speed_FR(int n){
	a.write(n + motor_FR_Offset);
		delay(motor_small_delay);
}
void motor_Set_Speed_FL(int n){
	b.write(n + motor_FL_Offset);
		delay(motor_small_delay);
}
void motor_Set_Speed_BR(int n){
	c.write(n + motor_BR_Offset);
		delay(motor_small_delay);
}
void motor_Set_Speed_BL(int n){
	d.write(n + motor_BL_Offset);
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
	a.attach(motor_FR_Pin);  //the pin for the servo control
	b.attach(motor_FL_Pin);
	c.attach(motor_BR_Pin);
	d.attach(motor_BL_Pin);
	// a.attach(motor_FR_Pin,2000,1000);  //the pin for the servo control
	// b.attach(motor_FL_Pin,2000,1000);
	// c.attach(motor_BR_Pin,2000,1000);
	// d.attach(motor_BL_Pin,2000,1000);
	
	// Arming speed should be 0 for sometime
	a.write(2300);
	b.write(2300);
	c.write(2300);
	d.write(2300);
	// delay(motor_Arm_Delay);
  	
	
  	Serial.println(F("Motors Armed..."));
	// Serial.println("Arming Completed"); // so I can keep track of what is loaded
}

void motor_calibrate(){
	Serial.println(F("Please remove power to motors.. Once done, press (1)"));
	while(!Serial.available());
	int read = Serial.parseInt();
	if(read==1){
		a.write(2000);
		b.write(2000);
		c.write(2000);
		d.write(2000);
		Serial.println(F("Connect Power, and wait for melody.. Once you hear that, press any key to continue..."));
		while(!Serial.available());
		Serial.println(F("Calibrating.."));
  		delay(8000);
		a.write(1000);
		b.write(1000);
		c.write(1000);
		d.write(1000);
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
