//
//  Motors.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//

#ifndef Motors_h
#define Motors_h
#include "Servo.h"
#include "DelaysAndOffsets.h"
#include "PinoutConfig.h"
#include "Servo.h"

Servo a,b,c,d;
float speeds[3];


void motor_setup(){
//  Arming Process
	a.attach(motorAPin);  //the pin for the servo control
	a.write(motorARMSpeed); //set initial servo position if desired
 
	b.attach(motorBPin);
	b.write(motorARMSpeed); //set initial servo position if desired
 
	c.attach(motorCPin);
	
	c.write(motorARMSpeed); //set initial servo position if desired
 
	d.attach(motorDPin);
  
	d.write(motorARMSpeed); //set initial servo position if desired
	
	delay(motorARMDelay);
	Serial.println("Arming Completed"); // so I can keep track of what is loaded
}

float motor_Get_Speed_A(){
	return speeds[0];
}
float motor_Get_Speed_B(){
	return speeds[1];
}
float motor_Get_Speed_C(){
	return speeds[2];
}
float motor_Get_Speed_D(){
	return speeds[3];
}
float *motor_Get_Speed(){
	return speeds;
}

void motor_Set_Speed_A(int n){
	a.write(n + motorAOffset);
	speeds[0] =n + motorAOffset;
//	delay(motor_small_delay);
}
void motor_Set_Speed_B(int n){
	b.write(n + motorBOffset);
	speeds[1] =n + motorBOffset;
//	delay(motor_small_delay);
}
void motor_Set_Speed_C(int n){
	c.write(n + motorCOffset);
	speeds[2] =n + motorCOffset;
//	delay(motor_small_delay);
}
void motor_Set_Speed_D(int n){
	d.write(n + motorDOffset);
	speeds[3] =n + motorDOffset;
//	delay(motor_small_delay);
}


void motor_Set_Speed(int n){
	motor_Set_Speed_A(n);
	motor_Set_Speed_B(n);
	motor_Set_Speed_C(n);
	motor_Set_Speed_D(n);
  delay(motor_small_delay);
	Serial.println("Speed set to " + String(n));
	
}


#endif /* Motors_h */
