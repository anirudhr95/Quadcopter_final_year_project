#include "Baro.h"
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  baro_Setup();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  Serial.print(baro_getPressure());
  Serial.print("\t");
//  Serial.print(baro_getPrecisePressure());
//  Serial.print("\t");
  Serial.print(baro_getTemperature());
  Serial.print("\t");
  Serial.print(baro_getAltitude());
  Serial.print("\t");
//  Serial.print(baro_getAltitude(true));
//  Serial.println();
  delay(1000);

}
