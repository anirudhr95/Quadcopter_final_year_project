#ifndef printHelper_h
#define printHelper_h
#include <DelaysAndOffsets.h>
	// GENERAL SETUP INITIALIZING,SUCCESS/FAILURE MESSAGES
const char* FORMAT_SETUP_INIT = "SETUP_INITIALIZING:%s\n"; //(MOTOR/GYRO)
const char* FORMAT_SETUP_SUCCESS = "SETUP_SUCCESS:%s\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_FAILURE = "SETUP_FAILURE:%s\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_ERRORCODE = "SETUP_ERRORCODE:%d\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_MESSAGE = "SETUP_MESSAGE:%s\n"; // (MESSAGE)
														 // MOTORS
const char* FORMAT_MOTOR_SPEEDS = "MOTOR:%d;%d;%d;%d\n"; // MOTOR SPEEDS
char buf[100];
void SEND_MSG_ULTRA(unsigned int cm[], int SONAM_NUM)
{
	// ORDER : TOP,BOTTOM,FRONT,RIGHT,LEFT
	Serial.print("ULTRA:");
	for (uint8_t i = 0; i < SONAR_NUM-1; i++) {
		Serial.print(cm[i]);
		Serial.print(F(";"));
	}
	Serial.print(cm[SONAR_NUM-1]);
	Serial.println();
}
void SEND_MSG_GYROMAG(float ypr[], int heading)
{
	Serial.print("GYROMAG:");
	Serial.print(ypr[0]);
	Serial.print(F(";"));
	Serial.print(ypr[1]);
	Serial.print(F(";"));
	Serial.print(ypr[2]);
	Serial.print(F(";"));
	Serial.println(heading);
	
}
#endif /* printHelper_h */