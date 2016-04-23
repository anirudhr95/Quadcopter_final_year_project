//#include <ServoTimer2.h>

#include <DelaysAndOffsets.h>
#include <Motors_servotimer.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>
#include <printHelper.h>
#include <Mpu.h>



int MotorSpeeds[3];
String input;
int first_position , second_position, third_position;

unsigned long last_sent = 0;
void setup() {
	Serial.begin (BAUD_RATE);
	sprintf(buf,FORMAT_SETUP_INIT,"ARDUINO");
	Serial.print(buf);
	motor_setup();
	gyro_Setup();
	ultra_Setup();
  sprintf(buf,FORMAT_SETUP_SUCCESS,"ARDUINO");
	Serial.print(buf);
//  TOO LAZY TO FORMAT FOLLOWING LINE.. NEED IT IN THIS FORMAT, for PID THREAD IN SERVER TO START
  Serial.println("SETUP COMPLETED:");
//  motor_Set_Speed(1500);

}


void sendYPR(){
  #ifdef SET_TRANSMISSION_RATE_HIGH
	if(millis() - last_sent >= UPDATE_FREQUENCY_RATE_HIGH){
    last_sent = millis();
//    SEND_MSG_GYROMAG(ypr, getHeading());
	}
	#elif defined SET_TRANSMISSION_RATE_MID
	if(millis() - last_sent >= UPDATE_FREQUENCY_RATE_MID){
    last_sent = millis();
//    SEND_MSG_GYROMAG(ypr, getHeading());
  }
  #elif defined SET_TRANSMISSION_RATE_LOW
	if(millis() - last_sent >= UPDATE_FREQUENCY_RATE_LOW){
    last_sent = millis();
//    SEND_MSG_GYROMAG(ypr, getHeading());
  }
  #endif


}
void loop() {
  
  
  
	if(Serial.available()){
/*
POSSIBLE INPUTS : 
1) MOTOR_SPEEDS:A;B;C;D     -> Set Motor Speeds to Values
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
	}
 ultra_Compute();
  getYPR();
  
  sendYPR();
}

