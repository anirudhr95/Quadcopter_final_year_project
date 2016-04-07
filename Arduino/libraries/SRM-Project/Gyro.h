//
//  Gyro.h
//  
//
//  Created by Shyam Ravikumar on 26/03/16.
//
//

#ifndef Gyro_h
#define Gyro_h


// I2C device class (I2Cdev) demonstration Arduino sketch for MPU6050 class using DMP (MotionApps v2.0)
// 6/21/2012 by Jeff Rowberg <jeff@rowberg.net>
// Updates (of the library) should (hopefully) always be available at https://github.com/jrowberg/i2cdevlib

// 1/30/2014
// This sketch was modified by Luis Ródenas <luisrodenaslorda@gmail.com> to include magnetometer and gyro readings
// while DMP is working, in case your magnetometer is attached to aux MPU's I2C lines. It should work with
// any magnetometer, but it has only been tested with HMC5883L.

// Original DMP example sketch has been simplified to my needs, check the original one to see more options.

// This sketch does NOT use the HMC5883L library, but it could be used instead of writing to registers directly.

// Credits to GitHub user muzhig for sharing the code to read magnetometer.


/* ============================================
 I2Cdev device library code is placed under the MIT license
 Copyright (c) 2012 Jeff Rowberg
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
 ===============================================
 */

// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"

// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif


// **********************  CONFIGURATION  **********************************
// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for SparkFun breakout and InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 mpu(0x68); // Most common is 0x68

int interrupt_pin=0; // Check where your INT pin is connected. Check below.


/* =========================================================================
 NOTE: In addition to connection 3.3v, GND, SDA, and SCL, this sketch
 depends on the MPU-6050's INT pin being connected to the Arduino's
 external interrupt #0 pin. 
 On the Arduino Uno and Mega 2560, this is digital I/O pin 2. On DUE you can 
 use ANY pin. Remember to modify this some lines below.
 * ========================================================================= */


// Variables used

#define HMC5883L_DEFAULT_ADDRESS    0x1E
#define HMC5883L_RA_DATAX_H         0x03
#define HMC5883L_RA_DATAZ_H         0x05
#define HMC5883L_RA_DATAY_H         0x07

#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
bool blinkState = false;

// MPU control/status vars
static bool dmpReady = false;  // set true if DMP init was successful
static uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
static uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
static uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
static uint16_t fifoCount;     // count of all bytes currently in FIFO
static uint8_t fifoBuffer[64]; // FIFO storage buffer

// orientation/motion vars
static Quaternion q;           // [w, x, y, z]         quaternion container
static VectorInt16 aa;         // [x, y, z]            accel sensor measurements
static int16_t gyro[3];        //To store gyro's measures
static int16_t mx, my, mz;     //To store magnetometer readings
static VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
static VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
static VectorFloat gravity;    // [x, y, z]            gravity vector
static float ypr[3], magData[4];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector
static float heading;          // Simple magnetic heading. (NOT COMPENSATED FOR PITCH AND ROLL)

// To check DMP frecuency  (it can be changed it the MotionApps v2 .h file)
static int time1,time1old;
static float frec1;



// ================================================================
// ===               INTERRUPT DETECTION ROUTINE                ===
// ================================================================

volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
  mpuInterrupt = true;
}



// ================================================================
// ===                      INITIAL SETUP                       ===
// ================================================================

void gyro_Setup() {

  // join I2C bus (I2Cdev library doesn't do this automatically)
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.begin();
  // **************************************************************
  // It is best to configure I2C to 400 kHz. 
  // If you are using an Arduino DUE, modify the variable TWI_CLOCK to 400000, defined in the file:
  // c:/Program Files/Arduino/hardware/arduino/sam/libraries/Wire/Wire.h
  // If you are using any other Arduino instead of the DUE, uncomment the following line:
  //TWBR = 24; // 400kHz I2C clock (200kHz if CPU is 8MHz)  //This line should be commented if you are using Arduino DUE
  // **************************************************************
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif

  // initialize serial communication
  //while (!Serial); // wait for Leonardo enumeration, others continue immediately

  // NOTE: 8MHz or slower host processors, like the Teensy @ 3.3v or Ardunio
  // Pro Mini running at 3.3v, cannot handle this baud rate reliably due to
  // the baud timing being too misaligned with processor ticks. You must use
  // 38400 or slower in these cases, or use some kind of external separate
  // crystal solution for the UART timer.

  // wait for ready


  // while (Serial.available() && Serial.read()); // empty buffer
  // while (!Serial.available()) {
  //   Serial.println(F("\nSend any character to begin DMP programming and demo: "));  // wait for data
  //   delay(1000);
  //   }
  // while (Serial.available() && Serial.read()); // empty buffer again

  // initialize device
  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();

  // verify connection
  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));

  // load and configure the DMP
  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();

  // supply your own gyro offsets here, scaled for min sensitivity
  // If you don't know yours, you can find an automated sketch for this task from: http://www.i2cdevlib.com/forums/topic/96-arduino-sketch-to-automatically-calculate-mpu6050-offsets/

  mpu.setXAccelOffset(gyro_X_Accel_Offset);
  mpu.setYAccelOffset(gyro_Y_Accel_Offset);
  mpu.setZAccelOffset(gyro_Z_Accel_Offset);

  mpu.setXGyroOffset(gyro_X_Offset);
  mpu.setYGyroOffset(gyro_Y_Offset);
  mpu.setZGyroOffset(gyro_Z_Offset);

  // In case you want to change MPU sensors' measurements ranges, you should implement it here. This has not been tested with DMP.

  // Magnetometer configuration

  mpu.setI2CMasterModeEnabled(0);
  mpu.setI2CBypassEnabled(1);

  Wire.beginTransmission(HMC5883L_DEFAULT_ADDRESS);
  Wire.write(0x02); 
  Wire.write(0x00);  // Set continuous mode
  Wire.endTransmission();
  delay(5);

  Wire.beginTransmission(HMC5883L_DEFAULT_ADDRESS);
  Wire.write(0x00);
  Wire.write(B00011000);  // 75Hz
  Wire.endTransmission();
  delay(5);

  mpu.setI2CBypassEnabled(0);

  // X axis word
  mpu.setSlaveAddress(0, HMC5883L_DEFAULT_ADDRESS | 0x80); // 0x80 turns 7th bit ON, according to datasheet, 7th bit controls Read/Write direction
  mpu.setSlaveRegister(0, HMC5883L_RA_DATAX_H);
  mpu.setSlaveEnabled(0, true);
  mpu.setSlaveWordByteSwap(0, false);
  mpu.setSlaveWriteMode(0, false);
  mpu.setSlaveWordGroupOffset(0, false);
  mpu.setSlaveDataLength(0, 2);

  // Y axis word
  mpu.setSlaveAddress(1, HMC5883L_DEFAULT_ADDRESS | 0x80);
  mpu.setSlaveRegister(1, HMC5883L_RA_DATAY_H);
  mpu.setSlaveEnabled(1, true);
  mpu.setSlaveWordByteSwap(1, false);
  mpu.setSlaveWriteMode(1, false);
  mpu.setSlaveWordGroupOffset(1, false);
  mpu.setSlaveDataLength(1, 2);

  // Z axis word
  mpu.setSlaveAddress(2, HMC5883L_DEFAULT_ADDRESS | 0x80);
  mpu.setSlaveRegister(2, HMC5883L_RA_DATAZ_H);
  mpu.setSlaveEnabled(2, true);
  mpu.setSlaveWordByteSwap(2, false);
  mpu.setSlaveWriteMode(2, false);
  mpu.setSlaveWordGroupOffset(2, false);
  mpu.setSlaveDataLength(2, 2);

  mpu.setI2CMasterModeEnabled(1);


  // make sure it worked (returns 0 if so)
  if (devStatus == 0) {
    // turn on the DMP, now that it's ready
    Serial.println(F("Enabling DMP..."));
    mpu.setDMPEnabled(true);

    // enable Arduino interrupt detection
    Serial.println(F("Enabling interrupt detection (Arduino external interrupt 0)..."));
    attachInterrupt(interrupt_pin, dmpDataReady, RISING);
    mpuIntStatus = mpu.getIntStatus();

    // set our DMP Ready flag so the main loop() function knows it's okay to use it
    Serial.println(F("DMP ready! Waiting for first interrupt..."));
    dmpReady = true;

    // get expected DMP packet size for later comparison
    packetSize = mpu.dmpGetFIFOPacketSize();
  } 
  else {
    // ERROR!
    // 1 = initial memory load failed
    // 2 = DMP configuration updates failed
    // (if it's going to break, usually the code will be 1)
    Serial.print(F("DMP Initialization failed (code "));
    Serial.print(devStatus);
    Serial.println(F(")"));
  }

  // configure LED for output
  pinMode(LED_PIN, OUTPUT);

}


	// ================================================================
	// ===                    MAIN PROGRAM LOOP                     ===
	// ================================================================
float *getYPR(){
  // if programming failed, don't try to do anything
  //  TODO FIX NEXT LINE
  //    if (!dmpReady) return [-1.0];
	
		// wait for MPU interrupt or extra packet(s) available
	while (!mpuInterrupt && fifoCount < packetSize) {
			// other program behavior stuff here
			// .
			// .
			// .
			// if you are really paranoid you can frequently test in between other
			// stuff to see if mpuInterrupt is true, and if so, "break;" from the
			// while() loop to immediately process the MPU data
			// .
			// .
			// .
	}
	
		// reset interrupt flag and get INT_STATUS byte
	mpuInterrupt = false;
	mpuIntStatus = mpu.getIntStatus();
	
		// get current FIFO count
	fifoCount = mpu.getFIFOCount();
	
		// check for overflow (this should never happen unless our code is too inefficient)
	if ((mpuIntStatus & 0x10) || fifoCount == 1024) {
			// reset so we can continue cleanly
		mpu.resetFIFO();
//		Serial.println(F("FIFO overflow!"));
//		delay(1);
		
			// otherwise, check for DMP data ready interrupt (this should happen frequently)
	} else if (mpuIntStatus & 0x02) {
			// wait for correct available data length, should be a VERY short wait
		while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
		
			// read a packet from FIFO
		mpu.getFIFOBytes(fifoBuffer, packetSize);
		
			// track FIFO count here in case there is > 1 packet available
			// (this lets us immediately read more without waiting for an interrupt)
		fifoCount -= packetSize;
			// display Euler angles in degrees
		mpu.dmpGetQuaternion(&q, fifoBuffer);
		mpu.dmpGetGravity(&gravity, &q);
		mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
		for(int i=0;i<3;i++)
			ypr[i] *= (180/M_PI);
		return ypr;
		
		
	}
}

float *getMAG(){
	magData[0]=mpu.getExternalSensorWord(0);
    magData[1]=mpu.getExternalSensorWord(2);
    magData[2]=mpu.getExternalSensorWord(4);
    
    return magData;

    
}
float getHeading(){
	getMAG();
	heading = atan2(magData[1], magData[0]);
    if(heading < 0) heading += 2 * M_PI;
    return heading * 180/M_PI;
}


  VectorInt16 getAccel() {
      // if programming failed, don't try to do anything
//      if (!dmpReady) return;
  
      // wait for MPU interrupt or extra packet(s) available
      while (!mpuInterrupt && fifoCount < packetSize) {
          // other program behavior stuff here
          // .
          // .
          // .
          // if you are really paranoid you can frequently test in between other
          // stuff to see if mpuInterrupt is true, and if so, "break;" from the
          // while() loop to immediately process the MPU data
          // .
          // .
          // .
      }
  
      // reset interrupt flag and get INT_STATUS byte
      mpuInterrupt = false;
      mpuIntStatus = mpu.getIntStatus();
  
      // get current FIFO count
      fifoCount = mpu.getFIFOCount();
  
      // check for overflow (this should never happen unless our code is too inefficient)
      if ((mpuIntStatus & 0x10) || fifoCount == 1024) {
          // reset so we can continue cleanly
          mpu.resetFIFO();
          Serial.println(F("FIFO overflow!"));
  
      // otherwise, check for DMP data ready interrupt (this should happen frequently)
      } else if (mpuIntStatus & 0x02) {
          // wait for correct available data length, should be a VERY short wait
          while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
  
          // read a packet from FIFO
          mpu.getFIFOBytes(fifoBuffer, packetSize);
  
          // track FIFO count here in case there is > 1 packet available
          // (this lets us immediately read more without waiting for an interrupt)
          fifoCount -= packetSize;
  
  
              // display real acceleration, adjusted to remove gravity
              mpu.dmpGetQuaternion(&q, fifoBuffer);
              mpu.dmpGetAccel(&aa, fifoBuffer);
              mpu.dmpGetGravity(&gravity, &q);
              mpu.dmpGetLinearAccel(&aaReal, &aa, &gravity);
              return aaReal;
  
  
  
      }
  }


#endif /* Gyro_h */
