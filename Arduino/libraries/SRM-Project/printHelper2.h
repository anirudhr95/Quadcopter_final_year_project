#ifndef printHelper2_h
#define printHelper2_h
char buf[100];
#include "printHelper.h"
void SEND_MSG_GyroMag(){
  getYPR();
  getMAG();
  sprintf(buf,FORMAT_GYROMAG,int(ypr[0]),int(ypr[1]),int(ypr[2]),mx,my,mz,int(heading));
  Serial.print(buf);
}
void SEND_MSG_UltraSound_ALL(){
  get_Ultra_ABCD();
  
  sprintf(buf,FORMAT_ULTRA_ALL,Ultra_Values[0],Ultra_Values[1],Ultra_Values[2],Ultra_Values[3]);
  Serial.print(buf);
}
void SEND_MSG_UltraSound_F(){
  get_Ultra_A();
  sprintf(buf,FORMAT_ULTRA_F,Ultra_Values[0]);
  Serial.print(buf);
}
void SEND_MSG_UltraSound_R(){
  
  get_Ultra_B();
  sprintf(buf,FORMAT_ULTRA_R,Ultra_Values[1]);
  Serial.print(buf);
}
void SEND_MSG_UltraSound_L(){
  
  get_Ultra_C();
  sprintf(buf,FORMAT_ULTRA_L,Ultra_Values[2]);
  Serial.print(buf);
}
void SEND_MSG_UltraSound_T(){
  
  get_Ultra_D();
  sprintf(buf,FORMAT_ULTRA_T,Ultra_Values[3]);
  Serial.print(buf);
}
void SEND_MSG_ULTRA_CONDITIONAL(int mode){
	switch(mode){
      case 0: SEND_MSG_UltraSound_ALL();
              break;
      case 1: SEND_MSG_UltraSound_F();
              SEND_MSG_UltraSound_R();
              break;
      case 2: SEND_MSG_UltraSound_F();
              SEND_MSG_UltraSound_L();
              break;
      case 3: SEND_MSG_UltraSound_T();
    }
}

void SEND_MSG_ALTITUDE(){
	sprintf(buf,FORMAT_BARO,int(baro_getAltitude()));
	Serial.print(buf);
}
#endif