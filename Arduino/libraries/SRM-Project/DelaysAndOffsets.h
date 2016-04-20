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
#define PRINT_MOTOR_CHANGES
// GYRO TRANSMISSION RATE 
/*
Uncomment the transmission rate to use
//HIGH = 3 for every other possible type of message
//MID = 2 for every other possible type of message
//LOW = 1 for every other possible type of message
*/
// #define GYRO_TRANSMISSION_RATE_HIGH
// #define GYRO_TRANSMISSION_RATE_MID 
#define GYRO_TRANSMISSION_RATE_LOW

<<<<<<< HEAD
// PID
#define Kp 1
#define Ki 1
#define Kd 1

//	Ultrasound
#define ultra_DelayBetweenReads 200
// #define ultra_toWingtipOffset 25
#define ultra_toWingtipOffset 0
#define ultra_safe_distance_from_wingtip 20
#define ultra_Offset_A 2
#define ultra_Offset_B 2
#define ultra_Offset_C 3
#define ultra_Offset_D 0

//Gyro
#define gyro_X_Accel_Offset -3481
#define gyro_Y_Accel_Offset -974
#define gyro_Z_Accel_Offset 1612
#define gyro_X_Offset 60
#define gyro_Y_Offset -23
#define gyro_Z_Offset 14


#define gyro_limit_pitch_pos 45
#define gyro_limit_pitch_neg 45
#define gyro_limit_roll_pos 45
#define gyro_limit_roll_neg 45
=======

#define BAUD_RATE 115200
#define PRINT_MOTOR_CHANGES true
#define SET_TRANSMISSION_RATE_HIGH
// #define SET_TRANSMISSION_RATE_MID 
// #define SET_TRANSMISSION_RATE_LOW

#define UPDATE_FREQUENCY_RATE_HIGH 50
#define UPDATE_FREQUENCY_RATE_MID 200
#define UPDATE_FREQUENCY_RATE_LOW 400


/* GYRO TRANSMISSION RATE 
Uncomment the transmission rate to use
HIGH = 3 for every other possible type of message
MID = 2 for every other possible type of message
LOW = 1 for every other possible type of message
*/



/*	
Ultrasound
*/

#define PING_INTERVAL 33 // Milliseconds between sensor pings (29ms is about the min to avoid cross-sensor echo).
#define MAX_DISTANCE 200 // Maximum distance (in cm) to ping.

// Order : Front, Right, Left, Top, Bottom
// Offset is the value to add, so that measurement is correct.Provide offsets for correct number of sensors
const int ultra_Offsets[] = {0,0,0,0,0};
#define SONAR_NUM     5 // Number of sensors.





// Chennai's magnetic declination as given by http://www.magnetic-declination.com/India/Chennai/1136292.html
#define declination -1.30 
#define DOSELFTEST false
#define USE_MADGWICK true //Madgwick filter if true, Mahony if false.
#define SerialDebug false   // set to true to get Serial output for debugging
#define ypr_refresh_time 10 //Used by functions other than getYPR, which depend on its values, to determine if getYPR has to be called again

>>>>>>> develop

//Motors
#define motor_FR_Offset 0
#define motor_FL_Offset 0
#define motor_BR_Offset 0
#define motor_BL_Offset 0

#define motor_Arm_Delay 4000
<<<<<<< HEAD
#define motor_Arm_Speed 0  //If calibrated correctly, it will arm without problems
#define motor_small_delay 10
#define motor_Min_Speed 1200
=======
#define motor_Min_Speed 1000
>>>>>>> develop
#define motor_Max_Speed 2000


#endif /* DelaysAndOffsets_h */
