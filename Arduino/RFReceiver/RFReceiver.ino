#include <VirtualWire.h>
String x ="";
void setup()
{
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_set_rx_pin(12);
    vw_setup(4000);  // Bits per sec
    Serial.begin(9600);

    vw_rx_start();       // Start the receiver PLL running
}
    void loop()
{
    x="";
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;

    if (vw_get_message(buf, &buflen)) // Non-blocking
    {
      
      for(int i=0;i<buflen;i++)
      {
   //  Serial.print(char(buf[i]));
     x.concat(char(buf[i]));

    
      }
     Serial.println(x);      
      
    }
    
}

