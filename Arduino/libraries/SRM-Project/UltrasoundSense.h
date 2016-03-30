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
  int	duration = pulseIn(echo_pin, HIGH) ; //sensor stops reading after some time - adding delay 26/03
  // Serial.println(duration);
  int distance = (duration/2) / 29.1;
  
  if(distance >=200 || distance <= 0){
  	return -1;
  }
  
  
  return distance;
  
}
void ultra_Setup(){
	pinMode(ultra_Trig_Pin_A, OUTPUT);
	pinMode(ultra_Trig_Pin_B, OUTPUT);
	pinMode(ultra_Trig_Pin_C, OUTPUT);
	pinMode(ultra_Trig_Pin_D, OUTPUT);
	pinMode(ultra_Echo_Pin_A  , INPUT);
	pinMode(ultra_Echo_Pin_B  , INPUT);
	pinMode(ultra_Echo_Pin_C  , INPUT);	
	pinMode(ultra_Echo_Pin_D  , INPUT);
	
}
void ultrainternalTrigger(int trig_pin){
	digitalWrite(trig_pin, LOW);
	delayMicroseconds(2);
	digitalWrite(trig_pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trig_pin, LOW);
}
float getDistance(int trig_pin, int echo_pin){
	ultrainternalTrigger(trig_pin);
	return ultrainternalDistanceMeasure(echo_pin);
}
float ultragetA() {
	return (getDistance(ultra_Trig_Pin_A,ultra_Echo_Pin_A ) - ultra_toWingtipOffset + ultra_Offset_A);
}
float ultragetB() {
	return (getDistance(ultra_Trig_Pin_B,ultra_Echo_Pin_B) - ultra_toWingtipOffset + ultra_Offset_B);
}
float ultragetC() {
	return (getDistance(ultra_Trig_Pin_C,ultra_Echo_Pin_C ) - ultra_toWingtipOffset + ultra_Offset_C);
}
float ultragetD() {
	return (getDistance(ultra_Trig_Pin_D,ultra_Echo_Pin_D ) - ultra_toWingtipOffset + ultra_Offset_);
}

float* getABCD()
{
	float a[3];
	// The following order & delay is important, as the pairs of functions should not have echo/trigger pins same
	
	a[0] = ultragetA();
	a[1] = ultragetB();	
	a[2] = ultragetC();
	a[3] = ultragetD();
	
	
	return a;
}

#endif /* UltrasoundSense_h */
