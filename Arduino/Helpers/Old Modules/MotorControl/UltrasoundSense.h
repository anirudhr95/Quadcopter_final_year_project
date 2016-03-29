//
//  UltrasoundSense.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.z//
//

#ifndef UltrasoundSense_h
#define UltrasoundSense_h

#include "PinoutConfig.h"
#include "DelaysAndOffsets.h"

float ultrainternalDistanceMeasure(){
  int	duration = pulseIn(ultra_Echo_Pin, HIGH) ; //sensor stops reading after some time - adding delay 26/03
	int distance = (duration/2) / 29.1;
	delayMicroseconds(ultra_DelayBetweenReads);
	if(distance >=200 || distance <= 0){
		return -1;
	}
 
 
	return distance;
	
}
void ultra_Setup(){
  pinMode(ultra_Trig_PinA, OUTPUT);
	pinMode(ultra_Trig_PinB, OUTPUT);
	pinMode(ultra_Trig_PinC, OUTPUT);
	pinMode(ultra_Trig_PinD, OUTPUT);
  pinMode(ultra_Echo_Pin  , INPUT);
}
void ultrainternalTrigger(int pin){
	digitalWrite(pin, LOW);
	delayMicroseconds(2);
	digitalWrite(pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(pin, LOW);
}
float ultragetA() {
	ultrainternalTrigger(ultra_Trig_PinA);
	return ultrainternalDistanceMeasure();
}
float ultragetB() {
	ultrainternalTrigger(ultra_Trig_PinB);
	return ultrainternalDistanceMeasure();
}
float ultragetC() {
	ultrainternalTrigger(ultra_Trig_PinC);
	return ultrainternalDistanceMeasure();
}
float ultragetD() {
	ultrainternalTrigger(ultra_Trig_PinD);
	return ultrainternalDistanceMeasure();
}

float* getABCD()
{
	float a[3];
	
	a[0] = ultragetA();
	a[1] = ultragetB();
	a[2] = ultragetC();
	a[3] = ultragetD();
	
	return a;
}

#endif /* UltrasoundSense_h */
