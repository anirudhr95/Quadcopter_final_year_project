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
#define GYRO_TRANSMISSION_RATE_HIGH
// #define GYRO_TRANSMISSION_RATE_MID 
// #define GYRO_TRANSMISSION_RATE_LOW

//	Ultrasound
#define ultra_DelayBetweenReads 200
#define ultra_toWingtipOffset 25
#define ultra_noObjectDetected_Return_Value -1
#define ultra_pulseIn_max_wait 50
// Extra Distance to add to get actual distance (Due to inaccuracies in sensor)
#define ultra_Offset_Front 2
#define ultra_Offset_Right 2
#define ultra_Offset_Left 3
#define ultra_Offset_Top 0
#define ultra_Offset_Bottom 0

//Gyro
#define gyro_X_Accel_Offset -3558
#define gyro_Y_Accel_Offset -946
#define gyro_Z_Accel_Offset 1629
#define gyro_X_Offset 56
#define gyro_Y_Offset -33
#define gyro_Z_Offset 68


#define gyro_limit_pitch_pos 45
#define gyro_limit_pitch_neg 45
#define gyro_limit_roll_pos 45
#define gyro_limit_roll_neg 45

//Motors
#define motor_FR_Offset 0
#define motor_FL_Offset 0
#define motor_BR_Offset 0
#define motor_BL_Offset 0

#define motor_Arm_Delay 4000
#define motor_Arm_Speed 0  //If calibrated correctly, it will arm without problems
#define motor_small_delay 10
#define motor_Min_Speed 1200
#define motor_Max_Speed 2000

// BMP
#define sensor_to_base_offset 5
#define bmp_sensor_refresh_delay 500
#define takeoff_prefered_altitude 150.00
#endif /* DelaysAndOffsets_h */
