//
//  DelaysAndOffsets.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//

#ifndef DelaysAndOffsets_h
#define DelaysAndOffsets_h

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

//Motors
#define motor_FR_Offset 0
#define motor_FL_Offset 0
#define motor_BR_Offset 0
#define motor_BL_Offset 0

#define motor_Arm_Delay 8000
#define motor_Arm_Speed 0  //If calibrated correctly, it will arm without problems
#define motor_small_delay 10
#define motor_Min_Speed 1200
#define motor_Max_Speed 2000

// BMP
#define sensor_to_base_offset 5
#define bmp_sensor_refresh_delay 500
#define takeoff_prefered_altitude 150.00
#endif /* DelaysAndOffsets_h */
