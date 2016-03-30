//
//  bmp-altitude.h
//  
//
//  Created by Shyam Ravikumar on 30/03/16.
//
//

#ifndef bmp_altitude_h
#define bmp_altitude_h

#include <SFE_BMP180.h>
#include <Wire.h>

// You will need to create an SFE_BMP180 object, here called "pressure":

SFE_BMP180 pressure;

double baseline; // baseline pressure

void bmp_Setup()
{
  // Serial.begin(9600);
  // Serial.println("REBOOT");
	Serial.println("Initializing BMP");

  // Initialize the sensor (it is important to get calibration values stored on the device).

  if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    // Oops, something went wrong, this is usually a connection problem,
    // see the comments at the top of this sketch for the proper connections.

    Serial.println("BMP180 init fail (disconnected?)\n\n");
  }

  // Get the baseline pressure:
  
  baseline = bmp_setBaseline();
  
  // Serial.print("baseline pressure: ");
  // Serial.print(baseline);
  // Serial.println(" mb");  
}
void bmp_setBaseline(){
	baseline = getPressure();
}
double bmp_getAltitude(){
	// Returns altitude relative to baseline(in cm)
	double a,P;
  
  // Get a new pressure reading:

  P = bmp_getPressure();

  // Show the relative altitude difference between
  // the new reading and the baseline reading:

  a = pressure.altitude(P,baseline);
  
  // Serial.print("relative altitude: ");
  // if (a >= 0.0) Serial.print(" "); // add a space for positive numbers
  // Serial.print(a,1);
  // Serial.print(" meters, ");
  delay(bmp_sensor_refresh_delay);
  return (a*100);
  
  
}
double bmp_getPressure()
{
  char status;
  double T,P,p0,a;

  // You must first get a temperature measurement to perform a pressure reading.
  
  // Start a temperature measurement:
  // If request is successful, the number of ms to wait is returned.
  // If request is unsuccessful, 0 is returned.

  status = pressure.startTemperature();
  if (status != 0)
  {
    // Wait for the measurement to complete:

    delay(status);

    // Retrieve the completed temperature measurement:
    // Note that the measurement is stored in the variable T.
    // Use '&T' to provide the address of T to the function.
    // Function returns 1 if successful, 0 if failure.

    status = pressure.getTemperature(T);
    if (status != 0)
    {
      // Start a pressure measurement:
      // The parameter is the oversampling setting, from 0 to 3 (highest res, longest wait).
      // If request is successful, the number of ms to wait is returned.
      // If request is unsuccessful, 0 is returned.

      status = pressure.startPressure(3);
      if (status != 0)
      {
        // Wait for the measurement to complete:
        delay(status);

        // Retrieve the completed pressure measurement:
        // Note that the measurement is stored in the variable P.
        // Use '&P' to provide the address of P.
        // Note also that the function requires the previous temperature measurement (T).
        // (If temperature is stable, you can do one temperature measurement for a number of pressure measurements.)
        // Function returns 1 if successful, 0 if failure.

        status = pressure.getPressure(P,T);
        if (status != 0)
        {
          return(P);
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
    }
    else Serial.println("error retrieving temperature measurement\n");
  }
  else Serial.println("error starting temperature measurement\n");
}


#endif /* bmp_altitude_h */
