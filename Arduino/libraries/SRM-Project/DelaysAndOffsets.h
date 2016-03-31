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
#define gyro_X_Offset 12
#define gyro_Y_Offset 2
#define gyro_Z_Offset 70
#define gyro_X_Accel_Offset -3593
#define gyro_Y_Accel_Offset -939
#define gyro_Z_Accel_Offset 1291

#define gyro_limit_pitch_pos 45
#define gyro_limit_pitch_neg 45
#define gyro_limit_roll_pos 45
#define gyro_limit_roll_neg 45

//Motors
#define motor_FR_Offset 0
#define motor_FL_Offset 0
#define motor_BR_Offset 0
#define motor_BL_Offset 0

#define motor_Arm_Delay 5000
#define motor_Arm_Speed 65
#define motor_small_delay 50

// BMP
#define sensor_to_base_offset 5
#define bmp_sensor_refresh_delay 500
#define takeoff_prefered_altitude 150.00
#endif /* DelaysAndOffsets_h */
