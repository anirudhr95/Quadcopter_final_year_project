#include <VirtualWire.h>
char *controller;
int index = 0;
void setup() {
  vw_set_ptt_inverted(true); //
  vw_set_tx_pin(12);
  vw_setup(4000);// speed of data transfer Kbps
  Serial.begin(9600);
  
  Serial.print("Initialization Completed");
}

void loop(){
doTransmission();

}
void getString()
{
  
  index=0;
  controller="";
  while(Serial.available())   
        controller[index++]= Serial.read(); 
  
  
  if(strlen(controller)>0)
  {
    controller[index]='\0';
    for(int i=0;i<strlen(controller);i++)
      Serial.print(controller[i]);
  }
}

void doTransmission()
{
  
  getString();
  if(strlen(controller) > 0 ) 
  { 
    for(int i=0;i<100;i++){
    vw_send((uint8_t *)controller, strlen(controller));
    vw_wait_tx(); // Wait until the whole message is gone
    delay(1000);
    }
  }
}
