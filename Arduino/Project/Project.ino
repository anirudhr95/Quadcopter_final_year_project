//#include <ServoTimer2.h>

#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors_servotimer.h>
#include <Baro.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>

// #define SENSORS_ON
//#define TEST_MODE_ON
double MotorSpeeds[3];
String input;
int first_position , second_position, third_position;
int UltraValues[] = {0,0,0,0};


String sender;
String sendData()
{
//  Y;P;R;Mx;My;Mz;He;Al;U1;U2;U3;U4
String x = String(ypr[0]) + ";" + String(ypr[1]) + ";" + String(ypr[2]) + ";" + String(magData[0]) + ";" + String(magData[1]) + ";" + String(magData[2]) +";"+ String(getHeading())+";"+String(baro_getAltitude())
+ ";" + String(ultra_values[0]) + ";" + String(ultra_values[1])+ ";" + String(ultra_values[2])+ ";" + String(ultra_values[3]) ;
return x;
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin (38400);
//  motor_setup();
  ultra_Setup();
  gyro_Setup();
  baro_Setup();
  #ifdef TEST_MODE_ON
  Serial.print("Setup Completed");
  Serial.print("Yaw\tPitch\tRoll\tAx\tAy\tAz\t\tUA\tUB\tUC\tRF\tRL\tBR\tBL");
  #endif

}
void loop() {
  sender="";
  if(Serial.available()){
    
    input = Serial.readString();
    if(input.startsWith("M")){
//      M:50;30;20;10
      first_position = input.indexOf(';');
      second_position = input.indexOf(';',first_position+1);
      third_position = input.indexOf(';',second_position+1);
      MotorSpeeds[0] = input.substring(2,first_position).toInt();
      MotorSpeeds[1] = input.substring(first_position+1,second_position).toInt();
      MotorSpeeds[2] = input.substring(second_position+1,third_position).toInt();
      MotorSpeeds[3] = input.substring(third_position+1).toInt();
      
    }
    else if(input.startsWith("R")){
//      RESET BAROMETER
      baro_setBaseline();
    }
    
    
    #ifdef TEST_MODE_ON
    Serial.println("VALUES ARE : ");
    for(int i=0;i<4;i++)
      Serial.println(MotorSpeeds[i]);
    #endif

  }
  getYPR();
//  getMAG();
  ultragetA();
  Serial.println(sendData());
}

