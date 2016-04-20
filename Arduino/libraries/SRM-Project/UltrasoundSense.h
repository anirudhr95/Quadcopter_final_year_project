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
#include "printHelper.h"
#include <NewPing.h>


unsigned long pingTimer[SONAR_NUM]; // Holds the times when the next ping should happen for each sensor.
unsigned int cm[SONAR_NUM];         // Where the ping distances are stored.
uint8_t currentSensor = 0;          // Keeps track of which sensor is active.


NewPing sonar[SONAR_NUM] = {     // Sensor object array.
	NewPing(ultra_Trig_Pin_Top, ultra_Echo_Pin_Top, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Bottom, ultra_Echo_Pin_Bottom, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Front, ultra_Echo_Pin_Front, MAX_DISTANCE), // Each sensor's trigger pin, echo pin, and max distance to ping.
	NewPing(ultra_Trig_Pin_Right, ultra_Echo_Pin_Right, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Left, ultra_Echo_Pin_Left, MAX_DISTANCE),
	
	
};

void ultra_Compute();
void echoCheck() ;
void ultra_on_Compute_Complete() ;


<<<<<<< HEAD
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
=======
>>>>>>> develop
void ultra_Setup(){
	char buf[100];
	sprintf(buf,FORMAT_SETUP_INIT,"ULTRASOUND");
	Serial.print(buf);
<<<<<<< HEAD
	pinMode(ultra_Trig_Pin_A, OUTPUT);
	pinMode(ultra_Trig_Pin_B, OUTPUT);
	pinMode(ultra_Trig_Pin_C, OUTPUT);
	pinMode(ultra_Trig_Pin_D, OUTPUT);
	pinMode(ultra_Echo_Pin_A  , INPUT);
	pinMode(ultra_Echo_Pin_B  , INPUT);
	pinMode(ultra_Echo_Pin_C  , INPUT);	
	pinMode(ultra_Echo_Pin_D  , INPUT);
=======
		// First ping starts at 75ms, gives time for the Arduino to chill before starting.
	pingTimer[0] = millis() + 100;
		// Set the starting time for each sensor.
	for (uint8_t i = 1; i < SONAR_NUM; i++)
		pingTimer[i] = pingTimer[i - 1] + PING_INTERVAL;
>>>>>>> develop
	sprintf(buf,FORMAT_SETUP_SUCCESS,"ULTRASOUND");
	Serial.print(buf);
	
}
<<<<<<< HEAD
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
=======
void ultra_Compute()
{
		// Run this on every loop. Calls Ultra_on_Compute_complete when each cycle finishes.
		// Loop through all the sensors.
	for (uint8_t i = 0; i < SONAR_NUM; i++)
	{
			// Is it this sensor's time to ping?
		if (millis() >= pingTimer[i]) {
				// Set next time this sensor will be pinged.
			pingTimer[i] += PING_INTERVAL * SONAR_NUM;
			if (i == 0 && currentSensor == SONAR_NUM - 1) {
					// Sensor ping cycle complete, do something with the results.
				ultra_on_Compute_Complete();
				
			}
				// Make sure previous timer is canceled before starting a new ping (insurance).
			sonar[currentSensor].timer_stop();
				// Sensor being accessed.
			currentSensor = i;
				// Make distance zero in case there's no ping echo for this sensor.
			cm[currentSensor] = 0;
				// Do the ping (processing continues, interrupt will call echoCheck to look for echo).
			sonar[currentSensor].ping_timer(echoCheck);
		}
	}
}
void echoCheck() { // If ping received, set the sensor distance to array.
	if (sonar[currentSensor].check_timer())
		cm[currentSensor] = sonar[currentSensor].ping_result / US_ROUNDTRIP_CM + ultra_Offsets[currentSensor];
}

void ultra_on_Compute_Complete() {
		// Sensor ping cycle complete, do something with the results.
	SEND_MSG_ULTRA(cm,SONAR_NUM);
>>>>>>> develop
}

#endif /* UltrasoundSense_h */
