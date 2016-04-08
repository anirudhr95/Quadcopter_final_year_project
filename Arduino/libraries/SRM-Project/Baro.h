//
//  Altitude.h
//  
//
//  Created by Shyam Ravikumar on 31/03/16.
//
//

#ifndef Baro_h
#define Baro_h
/*
  MS5611 Barometric Pressure & Temperature Sensor. Simple Example
  Read more: http://www.jarzebski.pl/arduino/czujniki-i-sensory/czujnik-cisnienia-i-temperatury-ms5611.html
  GIT: https://github.com/jarzebski/Arduino-MS5611
  Web: http://www.jarzebski.pl
  (c) 2014 by Korneliusz Jarzebski
*/
#include "DelaysAndOffsets.h"
#include <Wire.h>
#include <MS5611.h>

MS5611 ms5611;
static int baro_Offset = 0;
static double baseline;

float baro_getPressure(){
	return float(ms5611.readPressure(true));
	// Measured in Pascals
}
float baro_getTemperature(){
	return float(ms5611.readTemperature(true));	
	// Measured in Celsius
}

void baro_setBaseline(){
	
	baseline = baro_getPressure();
}



float baro_getAltitude(){

	// Measured in cms
	
	return (ms5611.getAltitude(baro_getPressure(), baseline) * 100);
}

void baro_Setup() 
{ // Initialize MS5611 sensor
  Serial.println("Initialize MS5611 Sensor");

  if(!ms5611.begin(MS5611_ULTRA_HIGH_RES))
  {
    Serial.println(F("Could not find a valid MS5611 sensor, check wiring!"));
    Serial.println(F("Baro Connection Failed"));
  }

  // Get reference pressure for relative altitude
  baro_setBaseline();
  Serial.println("Barometer connection Successful");
}






#endif /* Baro_h */
