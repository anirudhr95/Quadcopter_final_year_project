//#include <ServoTimer2.h>

#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors_servotimer.h>
#include <Baro.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>
#include <printHelper.h>
#include <printHelper2.h>



int MotorSpeeds[3];
String input;
int first_position , second_position, third_position;
int ULTRA_MODE = 0; //0:ALL,1:FR,2:FL,3:TOP
unsigned int count = 0;
void setup() {
	Serial.begin (BAUD_RATE);
	sprintf(buf,FORMAT_SETUP_INIT,"ARDUINO");
	Serial.print(buf);
	motor_setup();
	ultra_Setup();
	gyro_Setup();
	baro_Setup();

	sprintf(buf,FORMAT_SETUP_SUCCESS,"ARDUINO");
	Serial.print(buf);

}

void sendData(){
  #ifdef GYRO_TRANSMISSION_RATE_HIGH
	if(count%5 == 1)
      SEND_MSG_ULTRA_CONDITIONAL(ULTRA_MODE);
	
	else if(count%5 == 3)
    SEND_MSG_ALTITUDE();
	else
    SEND_MSG_GyroMag();
	
		
  #elif defined GYRO_TRANSMISSION_RATE_MID
	if(count%4 == 1)
		SEND_MSG_ULTRA_CONDITIONAL(ULTRA_MODE);
	else if(count%4 == 3)
		SEND_MSG_ALTITUDE();
	else
		SEND_MSG_GyroMag();
  
  #elif defined GYRO_TRANSMISSION_RATE_LOW
	if(count%3 == 1)
		SEND_MSG_ULTRA_CONDITIONAL(ULTRA_MODE);
	else if(count%3 == 2)
		SEND_MSG_ALTITUDE();
	else
		SEND_MSG_GyroMag();
  #endif
  count++;


}
void loop() {
	if(Serial.available()){
/*
POSSIBLE INPUTS : 
1) MOTOR_SPEEDS:A;B;C;D     -> Set Motor Speeds to Values
2) RESET_BARO
3) ULTRA_MODE:MODE   -> 0,1,2,3 (0:ALL,1:FR,2:FL,3:TOP)
*/
		input = Serial.readString();
    
		if(input.startsWith("MOTOR_SPEEDS")){
//      M:50;30;20;10
			first_position = input.indexOf(';');
			second_position = input.indexOf(';',first_position+1);
			third_position = input.indexOf(';',second_position+1);
			MotorSpeeds[0] = input.substring(input.indexOf(':')+1,first_position).toInt();
			MotorSpeeds[1] = input.substring(first_position+1,second_position).toInt();
			MotorSpeeds[2] = input.substring(second_position+1,third_position).toInt();
			MotorSpeeds[3] = input.substring(third_position+1).toInt();
     refreshMotors(MotorSpeeds);

		}
   if(input.startsWith("A:")){
      motor_Set_Speed(input.substring(input.indexOf(':')+1).toInt());
   }
		else if(input.startsWith("RESET_BARO")){
//      RESET BAROMETER
			baro_setBaseline();
		}
		else if(input.startsWith("ULTRA_MODE")){
			// SET ULTRASONIC MODE
			ULTRA_MODE = input.substring(input.indexOf(':')+1).toInt();
		}
	}
	sendData();
 delay(500);
}

