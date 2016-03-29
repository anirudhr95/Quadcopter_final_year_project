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

float ultrainternalDistanceMeasure(int echo_pin){
  int	duration = pulseIn(echo_pin, HIGH,ultra_DelayBetweenReads) ; //sensor stops reading after some time - adding delay 26/03
  int distance = (duration/2) / 29.1;
  
  if(distance >=200 || distance <= 0){
  	return -1;
  }
  
  
  return distance;
  
}
void ultra_Setup(){
	pinMode(ultra_Trig_Pin_AB, OUTPUT);
	pinMode(ultra_Trig_Pin_CD, OUTPUT);
	pinMode(ultra_Echo_Pin_AC  , INPUT);
	pinMode(ultra_Echo_Pin_BD  , INPUT);
}
void ultrainternalTrigger(int trig_pin){
	digitalWrite(trig_pin, LOW);
	delayMicroseconds(2);
	digitalWrite(trig_pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trig_pin, LOW);
}
float ultragetA() {
	ultrainternalTrigger(ultra_Trig_Pin_AB);
	return ultrainternalDistanceMeasure(ultra_Echo_Pin_AC);
}
float ultragetB() {
	ultrainternalTrigger(ultra_Trig_Pin_AB);
	return ultrainternalDistanceMeasure(ultra_Echo_Pin_BD);
}
float ultragetC() {
	ultrainternalTrigger(ultra_Trig_Pin_CD);
	return ultrainternalDistanceMeasure(ultra_Echo_Pin_AC);
}
float ultragetD() {
	ultrainternalTrigger(ultra_Trig_Pin_CD);
	return ultrainternalDistanceMeasure(ultra_Echo_Pin_BD);
}

float* getABCD()
{
	float a[3];
	// The following order & delay is important, as the pairs of functions should not have echo/trigger pins same
	a[0] = ultragetA();
	a[3] = ultragetD();	
	// delay(ultra_DelayBetweenReads);
	a[1] = ultragetB();
	a[2] = ultragetC();
	
	
	return a;
}

#endif /* UltrasoundSense_h */
