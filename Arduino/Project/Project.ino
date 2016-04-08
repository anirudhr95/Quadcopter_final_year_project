//#include <ServoTimer2.h>

#include <DelaysAndOffsets.h>
#include <Gyro.h>
#include <Motors_servotimer.h>
#include <Baro.h>
#include <PinoutConfig.h>
#include <UltrasoundSense.h>


//#define TEST_MODE_ON
//#define MAG_ON
#define GYRO_ON
#define ALT_ON
#define ULTRA_ON
#define DONT_SETUP_MOTORS



double MotorSpeeds[3];
String input,x;
int first_position , second_position, third_position;
float *UltraValues;
int count = 0;
String sender;
void setup() {
  // put your setup code here, to run once:
  Serial.begin (115200);
  #ifndef DONT_SETUP_MOTORS
  motor_setup();
  #endif
  ultra_Setup();
  gyro_Setup();
  baro_Setup();

}
String sendData(){
  #ifdef GYRO_ON
  if(count%4==0)
    {
      
      getYPR();
   
      
     x = String("ypr:") + String(ypr[0]) + ";" + String(ypr[1]) + ";" + String(ypr[2]) + ";";
      
      
    }
    #endif
    #ifdef MAG_ON
    if(count%4==1)
    {
        getMAG();
         x = String("Magdata:") + ";" + String(mx) + ";" + String(my) + ";" + String(mz) + ";" + String(getHeading());
        
    
      
    }
    #endif
    #ifdef ULTRA_ON
    if(count%4==2)
    {
      UltraValues = getABCD();
     x = String("Ultra:")+";" + String(UltraValues[0]) + ";" + String(UltraValues[1])+ ";" + String(UltraValues[2])+ ";" + String(UltraValues[3])+";" ;
    
    
    }
    #endif
    #ifdef ALT_ON
    if(count%4==3){
      x=String("Alt:")+String(baro_getAltitude());
    }
    #endif
    
  
  count += 1;
  return x;
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
  Serial.println(sendData());
  delay(1000);
}

