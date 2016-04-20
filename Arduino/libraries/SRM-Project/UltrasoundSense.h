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
int	duration, distance;
void ultra_Setup(){
	char buf[100];
	sprintf(buf,FORMAT_SETUP_INIT,"ULTRASOUND");
	Serial.print(buf);
	pinMode(ultra_Trig_Pin_Front, OUTPUT);
	pinMode(ultra_Trig_Pin_Right, OUTPUT);
	pinMode(ultra_Trig_Pin_Left, OUTPUT);
	pinMode(ultra_Trig_Pin_Top, OUTPUT);
	pinMode(ultra_Trig_Pin_Bottom, OUTPUT);
	pinMode(ultra_Echo_Pin_Front  , INPUT);
	pinMode(ultra_Echo_Pin_Right  , INPUT);
	pinMode(ultra_Echo_Pin_Left  , INPUT);	
	pinMode(ultra_Echo_Pin_Top  , INPUT);
	pinMode(ultra_Echo_Pin_Bottom  , INPUT);
	sprintf(buf,FORMAT_SETUP_SUCCESS,"ULTRASOUND");
	Serial.print(buf);
	
}
void __ultrainternalTrigger__(int trig_pin){
	digitalWrite(trig_pin, LOW);
	delayMicroseconds(2);
	digitalWrite(trig_pin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trig_pin, LOW);
}
int __getDistance__(int trig_pin, int echo_pin){
	__ultrainternalTrigger__(trig_pin);
	duration = pulseIn(echo_pin, HIGH, ultra_pulseIn_max_wait) ; //sensor stops reading after some time - adding delay 26/03
	// Serial.println(duration);
	distance = (duration/2) / 29.1;
	if(distance >=200 || distance <= 0){
		return ultra_noObjectDetected_Return_Value;
	}
	return distance;
}
int __get_Ultra_Distance__(int trig_pin, int echo_pin_pin, int offset=0){
	int temp = __getDistance__(trig_pin,echo_pin);
	if(temp == ultra_noObjectDetected_Return_Value){
		return ultra_noObjectDetected_Return_Value;
	}
	temp += offset - ultra_toWingtipOffset;
	return temp;
}
int get_Ultra_Front() {
	Ultra_Values[0] = __get_Ultra_Distance__(ultra_Trig_Pin_Front,ultra_Echo_Pin_Front,ultra_Offset_Front);
	return Ultra_Values[0];
}
int get_Ultra_Right() {
	Ultra_Values[1] = __get_Ultra_Distance__(ultra_Trig_Pin_Right,ultra_Echo_Pin_Right,ultra_Offset_Right);
	return Ultra_Values[1];
}
int get_Ultra_Left() {
	Ultra_Values[2] = __get_Ultra_Distance__(ultra_Trig_Pin_Left,ultra_Echo_Pin_Left,ultra_Offset_Left);
	return Ultra_Values[2];
}
int get_Ultra_Top() {
	Ultra_Values[3] = __get_Ultra_Distance__(ultra_Trig_Pin_Top,ultra_Echo_Pin_Top,ultra_Offset_Top);
	return Ultra_Values[3];
}
int get_Ultra_Bottom() {
	Ultra_Values[4] = __get_Ultra_Distance__(ultra_Trig_Pin_Bottom,ultra_Echo_Pin_Bottom,ultra_Offset_Bottom);
	return Ultra_Values[4];
}
int* get_Ultra_ABCD()
{
	// The following order & delay is important, as the pairs of functions should not have echo/trigger pins same
	get_Ultra_Front();
	get_Ultra_Right();	
	get_Ultra_Left();
	get_Ultra_Top();
	get_Ultra_Bottom();
	return Ultra_Values;
}

#endif /* UltrasoundSense_h */
