//
//  Motors.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//

#ifndef Motors_h
#define Motors_h
#include <ServoTimer2.h>
#include "DelaysAndOffsets.h"
#include "PinoutConfig.h"
#include "Servo.h"

ServoTimer2 a,b,c,d;
int speeds[3];

int atom(int angle){
	return map(angle, 0,180,1000,2000);
}

void motor_setup(){
//  Arming Process
	a.attach(motor_FR_Pin);  //the pin for the servo control 
	b.attach(motor_FL_Pin); 
	c.attach(motor_BR_Pin); 
	d.attach(motor_BL_Pin);
	

	a.write(motor_Arm_Speed); //set initial servo position if desired
  	b.write(motor_Arm_Speed); //set initial servo position if desired
  	c.write(motor_Arm_Speed); //set initial servo position if desired
  	d.write(motor_Arm_Speed); //set initial servo position if desired

  	
  	delay(motor_Arm_Delay);	
	Serial.println("Arming Completed"); // so I can keep track of what is loaded
}

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
	a.write(atom(n + motor_FR_Offset));
	speeds[0] = n + motor_FR_Offset;
	//	delay(motor_small_delay);
}
void motor_Set_Speed_FL(int n){
	b.write(atom(n + motor_FL_Offset));
	speeds[1] =n + motor_FL_Offset;
	//	delay(motor_small_delay);
}
void motor_Set_Speed_BR(int n){
	c.write(atom(n + motor_BR_Offset));
	speeds[2] =n + motor_BR_Offset;
	//	delay(motor_small_delay);
}
void motor_Set_Speed_BL(int n){
	d.write(atom(n + motor_BL_Offset));
	speeds[3] =n + motor_BL_Offset;
	//	delay(motor_small_delay);
}


void motor_Set_Speed(int n){
	motor_Set_Speed_FR(n);
	motor_Set_Speed_FL(n);
	motor_Set_Speed_BR(n);
	motor_Set_Speed_BL(n);
	
	delay(motor_small_delay);
	Serial.println("Speed set to " + String(n));
	
}


#endif /* Motors_h */
