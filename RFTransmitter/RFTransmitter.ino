#include<VirtualWire.h> 

int i=0;

void setup()
{
Serial.begin(9600); 
vw_setup(2000); 
vw_set_tx_pin(12);
vw_set_ptt_inverted(true);
delay(1000);
Serial.println("Initialized communication with python SM");

}
void Transmit()
{
  char cad[50];
  i=0;
  memset(cad,0,50);
  //Serial.println(strlen(cad));
if( Serial.available()> 0)
{
  
  
  while(Serial.available()){
    cad[i] = Serial.read(); 
    i++;
    delay(2);
  }
 
}
if(strlen(cad)>0)
{
vw_send((byte *)cad, strlen(cad));
vw_wait_tx();
Serial.println("Transmitted : " + String(cad));
delay(400);
}

}
void loop()
{

Transmit();
}
