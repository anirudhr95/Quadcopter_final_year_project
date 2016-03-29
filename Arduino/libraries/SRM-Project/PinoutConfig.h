//
//  PinoutConfig.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//


#ifndef PinoutConfig_h
#define PinoutConfig_h

//Motors ( 4 Gnd, 4 Digital)
#define motor_FR_Pin 10
#define motor_FL_Pin 11
#define motor_BR_Pin 12
#define motor_BL_Pin 13



//Ultrasound Sensors ( 4 Gnd, 4 VCC, 2 Dig each)
//A=Front, B= Back, C= Left, D= Right

//#define ultra_Trig_PinA 3
//#define ultra_Trig_PinB 4
//#define ultra_Trig_PinC 5
//#define ultra_Trig_PinD 6
//#define ultra_Echo_Pin 13

#define ultra_Trig_Pin_AB 3
#define ultra_Trig_Pin_CD 4
#define ultra_Echo_Pin_AC 5
#define ultra_Echo_Pin_BD 6
//Pins 7,8 can be used to power these.


//Accelerometer ( 1 Gnd, 1 VCC, 1 Dig, 2 Analog)
#define gyro_int_Pin 2
#define gyro_SCL_Pin A5
#define gyro_SDA_Pin A4

//Barometer
//#define baro_SCLPin 8
//#define baroSDAPin 7



#endif /* PinoutConfig_h */



//Each Ultrasonic sensor uses 15 mA when active. Each arduino pin can deliver 40 mA, with a total of 200 mA. Need to split Ultrasonic sensors into groups of 2, triggering them at same time.

