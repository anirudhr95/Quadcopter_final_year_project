//
//  PinoutConfig.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//


#ifndef PinoutConfig_h
#define PinoutConfig_h

//A=Front, B= Back, C= Left, D= Right

//Motors ( 4 Gnd, 4 Digital)
#define motor_FR_Pin 6
#define motor_FL_Pin 10
#define motor_BR_Pin 11
#define motor_BL_Pin 12

//Ultrasound Sensors ( 4 Gnd, 4 VCC, 2 Dig each)
#define ultraTrigPinA 3
#define ultraTrigPinB 4
#define ultraTrigPinC 5
#define ultraTrigPinD 6`
#define ultraEchoPin 13

//Accelerometer ( 1 Gnd, 1 VCC, 1 Dig, 2 Analog)
#define gyrointPin 2
#define gyroSCLPin A5
#define gyroSDAPin A4

//Barometer
#define baroSCLPin 8
#define baroSDAPin 7



#endif /* PinoutConfig_h */
