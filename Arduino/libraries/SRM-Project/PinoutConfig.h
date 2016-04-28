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
	// ORDER BOTTOM,TOP,FRONT,RIGHT,LEFT
#define ultra_Trig_Pin_Bottom 7
#define ultra_Trig_Pin_Top 3
#define ultra_Trig_Pin_Front 4
#define ultra_Trig_Pin_Right 5
#define ultra_Trig_Pin_Left 6

#define ultra_Echo_Pin_Bottom 8
#define ultra_Echo_Pin_Top 14
#define ultra_Echo_Pin_Front 15
#define ultra_Echo_Pin_Right 16
#define ultra_Echo_Pin_Left 17


	//A0, A1, A2, A3 can power these


	//Accelerometer ( 1 Gnd, 1 VCC, 1 Dig, 2 Analog)
	// #define gyro_int_Pin 2
#define gyro_SCL_Pin 19
#define gyro_SDA_Pin 18
#define gyro_interrupt_pin 2



#endif /* PinoutConfig_h */



	//Each Ultrasonic sensor uses 15 mA when active. Each arduino pin can deliver 40 mA, with a total of 200 mA. Need to split Ultrasonic sensors into groups of 2, triggering them at same time.

