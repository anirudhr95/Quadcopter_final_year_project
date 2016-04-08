#ifndef printHelper_h
#define printHelper_h

// GENERAL SETUP INITIALIZING,SUCCESS/FAILURE MESSAGES
const char* FORMAT_SETUP_INIT = "SETUP_INITIALIZING:%s\n"; //(MOTOR/GYRO)
const char* FORMAT_SETUP_SUCCESS = "SETUP_SUCCESS:%s\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_FAILURE = "SETUP_FAILURE:%s\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_ERRORCODE = "SETUP_ERRORCODE:%d\n"; // (MOTOR/GYRO)
const char* FORMAT_SETUP_MESSAGE = "SETUP_MESSAGE:%s\n"; // (MESSAGE)
// MOTORS
const char* FORMAT_MOTOR_SPEEDS = "MOTOR:%d;%d;%d;%d\n"; // MOTOR SPEEDS
// GYRO+MAG
const char* FORMAT_GYROMAG = "GYROMAG:%d;%d;%d;%d;%d;%d;%d\n"; //YPR,MAG(x,y,z),heading
// ULTRASOUND

const char* FORMAT_ULTRA_F = "ULTRA_F:%d\n";
const char* FORMAT_ULTRA_ALL = "ULTRA_ALL:%d;%d;%d;%d\n";
const char* FORMAT_ULTRA_L = "ULTRA_L:%d\n";
const char* FORMAT_ULTRA_R = "ULTRA_R:%d\n";
const char* FORMAT_ULTRA_T = "ULTRA_T:%d\n";

const char* FORMAT_BARO = "ALTITUDE:%d\n";
#endif /* printHelper_h */