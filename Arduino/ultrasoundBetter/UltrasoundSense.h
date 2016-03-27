//
//  UltrasoundSense.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.z//
//

#ifndef UltrasoundSense_h
#define UltrasoundSense_h

#include "PinoutConfig.h"
#include "Delays.h"

float ultrainternalDistanceMeasure(){
  int	duration = pulseIn(ultraEchoPin, HIGH) ; //sensor stops reading after some time - adding delay 26/03
	int distance = (duration/2) / 29.1;
	delayMicroseconds(ultraDelayBetweenReads);
	if(distance >=200 || distance <= 0){
		return -1;
	}
 
 
	return distance;
	
}
void ultraSetup(){
  pinMode(ultraTrigPinA, OUTPUT);
  pinMode(ultraEchoPin  , INPUT);
}
void ultrainternalTrigger(int pin){
	digitalWrite(pin, LOW);
	delayMicroseconds(2);
	digitalWrite(pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(pin, LOW);
}
float ultragetA() {
	ultrainternalTrigger(ultraTrigPinA);
	return ultrainternalDistanceMeasure();
}
float ultragetB() {
	ultrainternalTrigger(ultraTrigPinB);
	return ultrainternalDistanceMeasure();
}
float ultragetC() {
	ultrainternalTrigger(ultraTrigPinC);
	return ultrainternalDistanceMeasure();
}
float ultragetD() {
	ultrainternalTrigger(ultraTrigPinD);
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
