//
//  DelaysAndOffsets.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//

#ifndef DelaysAndOffsets_h
#define DelaysAndOffsets_h


#define BAUD_RATE 115200
#define PRINT_MOTOR_CHANGES true


// #define SET_TRANSMISSION_RATE_HIGH
// #define SET_TRANSMISSION_RATE_MID 
#define SET_TRANSMISSION_RATE_LOW

#define UPDATE_FREQUENCY_RATE_HIGH 100
#define UPDATE_FREQUENCY_RATE_MID 300
#define UPDATE_FREQUENCY_RATE_LOW 800
#define NUM_GYRO_READINGS_PER_ULTRA 3

/* GYRO TRANSMISSION RATE 
Uncomment the transmission rate to use
HIGH = 3 for every other possible type of message
MID = 2 for every other possible type of message
LOW = 1 for every other possible type of message
*/

// Pitch is -Roll, Roll is -Pitch
#define GYRO_ANGLES_REVERSED true
#define GYRO_PITCH_OFFSET -8.5
#define GYRO_ROLL_OFFSET 8.8
/*	
Ultrasound
*/

// USES UPDATE FREQUENCY RATE OF GYRO
#define MAX_DISTANCE 300 // Maximum distance (in cm) to ping.
#define SONAR_NUM     5 // Number of sensors.




// Chennai's magnetic declination as given by http://www.magnetic-declination.com/India/Chennai/1136292.html
#define declination -1.30 
#define DOSELFTEST false
#define USE_MADGWICK true //Madgwick filter if true, Mahony if false.
#define SerialDebug false   // set to true to get Serial output for debugging
#define ypr_refresh_time 10 //Used by functions other than getYPR, which depend on its values, to determine if getYPR has to be called again


//Motors
#define USE_SERVOTIMER2 false
static const int motor_offsets[] = {0,0,0,0};

#define motor_Arm_Delay 4000
#define motor_Min_Speed 1000
#define motor_Max_Speed 2000


#endif /* DelaysAndOffsets_h */
