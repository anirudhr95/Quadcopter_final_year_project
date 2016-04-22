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

int PING_INTERVAL;
unsigned long pingTimer[SONAR_NUM]; // Holds the times when the next ping should happen for each sensor.
unsigned int cm[SONAR_NUM];         // Where the ping distances are stored.
uint8_t currentSensor = 0;          // Keeps track of which sensor is active.


NewPing sonar[SONAR_NUM] = {     // Sensor object array.
	// ORDER : BOTTOM, TOP,FRONT,RIGHT,LEFT
	
	NewPing(ultra_Trig_Pin_Bottom, ultra_Echo_Pin_Bottom, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Top, ultra_Echo_Pin_Top, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Front, ultra_Echo_Pin_Front, MAX_DISTANCE), // Each sensor's trigger pin, echo pin, and max distance to ping.
	NewPing(ultra_Trig_Pin_Right, ultra_Echo_Pin_Right, MAX_DISTANCE),
	NewPing(ultra_Trig_Pin_Left, ultra_Echo_Pin_Left, MAX_DISTANCE)
	
	
};

void ultra_Compute();
void echoCheck() ;
void ultra_on_Compute_Complete() ;


void ultra_Setup(){
	char buf[100];
	sprintf(buf,FORMAT_SETUP_INIT,"ULTRASOUND");
	Serial.print(buf);
		// First ping starts at 75ms, gives time for the Arduino to chill before starting.
	pingTimer[0] = millis() + 100;
		// Set the starting time for each sensor.
	for (uint8_t i = 1; i < SONAR_NUM; i++)
		pingTimer[i] = pingTimer[i - 1] + PING_INTERVAL;
	sprintf(buf,FORMAT_SETUP_SUCCESS,"ULTRASOUND");
	Serial.print(buf);
	#ifdef SET_TRANSMISSION_RATE_HIGH
		PING_INTERVAL = UPDATE_FREQUENCY_RATE_HIGH;
	#elif defined SET_TRANSMISSION_RATE_MID
		PING_INTERVAL = UPDATE_FREQUENCY_RATE_MID;
	#elif defined SET_TRANSMISSION_RATE_LOW
		PING_INTERVAL = UPDATE_FREQUENCY_RATE_LOW;
	#endif

	
}
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
		cm[currentSensor] = sonar[currentSensor].ping_result / US_ROUNDTRIP_CM;
}

void ultra_on_Compute_Complete() {
		// Sensor ping cycle complete, do something with the results.
	SEND_MSG_ULTRA(cm,SONAR_NUM);
}

#endif /* UltrasoundSense_h */
