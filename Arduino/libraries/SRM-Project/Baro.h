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
#include "printHelper.h"
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
  char buf[100];
  sprintf(buf,FORMAT_SETUP_INIT,"BARO");
  Serial.print(buf);

  if(!ms5611.begin(MS5611_ULTRA_HIGH_RES))
  {
    sprintf(buf,FORMAT_SETUP_FAILURE,"BARO");
    Serial.print(buf);
  }
  else{
    baro_setBaseline();
    sprintf(buf,FORMAT_SETUP_SUCCESS,"BARO");
  }
}






#endif /* Baro_h */
