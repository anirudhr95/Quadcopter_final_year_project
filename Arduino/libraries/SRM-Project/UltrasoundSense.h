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


int *Ultra_Values;
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
	char buf[100];
	sprintf(buf,FORMAT_SETUP_INIT,"ULTRASOUND");
	Serial.print(buf);
	pinMode(ultra_Trig_Pin_A, OUTPUT);
	pinMode(ultra_Trig_Pin_B, OUTPUT);
	pinMode(ultra_Trig_Pin_C, OUTPUT);
	pinMode(ultra_Trig_Pin_D, OUTPUT);
	pinMode(ultra_Echo_Pin_A  , INPUT);
	pinMode(ultra_Echo_Pin_B  , INPUT);
	pinMode(ultra_Echo_Pin_C  , INPUT);	
	pinMode(ultra_Echo_Pin_D  , INPUT);
	sprintf(buf,FORMAT_SETUP_SUCCESS,"ULTRASOUND");
	Serial.print(buf);
	
}
void ultrainternalTrigger(int trig_pin){
	digitalWrite(trig_pin, LOW);
	delayMicroseconds(2);
	digitalWrite(trig_pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trig_pin, LOW);
}
int getDistance(int trig_pin, int echo_pin){
	ultrainternalTrigger(trig_pin);
	return ultrainternalDistanceMeasure(echo_pin);
}
int get_Ultra_A() {
	Ultra_Values[0] = (getDistance(ultra_Trig_Pin_A,ultra_Echo_Pin_A ) - ultra_toWingtipOffset + ultra_Offset_A);
	return Ultra_Values[0];
}
int get_Ultra_B() {
	Ultra_Values[1] = (getDistance(ultra_Trig_Pin_B,ultra_Echo_Pin_B) - ultra_toWingtipOffset + ultra_Offset_B);
	return Ultra_Values[1];
}
int get_Ultra_C() {
	Ultra_Values[2] = (getDistance(ultra_Trig_Pin_C,ultra_Echo_Pin_C ) - ultra_toWingtipOffset + ultra_Offset_C);
	return Ultra_Values[2];
}
int get_Ultra_D() {
	Ultra_Values[3] = (getDistance(ultra_Trig_Pin_D,ultra_Echo_Pin_D ) - ultra_toWingtipOffset + ultra_Offset_D);
	return Ultra_Values[3];
}

int* get_Ultra_ABCD()
{
	
	// The following order & delay is important, as the pairs of functions should not have echo/trigger pins same
	
	get_Ultra_A();
	get_Ultra_B();	
	get_Ultra_C();
	get_Ultra_D();
	return Ultra_Values;
}

#endif /* UltrasoundSense_h */
