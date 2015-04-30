// zoomkat 10-22-11 serial servo test
// type servo position 0 to 180 in serial monitor
// or for writeMicroseconds, use a value like 1500
// for IDE 0022 and later
// Powering a servo from the arduino usually *DOES NOT WORK*.

String readString;
//#include <Servo.h> 
#include <VirtualWire.h>
#include <SoftwareServo.h> 
SoftwareServo a,b,c,d;  // create servo object to control a servo 
static int aoff=-6;
static int boff=2;
static int coff=4;
static int doff=-4;
String x = "";
int speedRequested;
void setup() {
  
  Serial.begin(9600);
  initReceiver();
   arm();
}
void arm(){
  a.attach(9);  //the pin for the servo control 
  b.attach(10);
  c.attach(11);
  d.attach(12);

  
  
  a.write(65); //set initial servo position if desired
  delay(50);
  b.write(65); //set initial servo position if desired
  delay(50);
  c.write(65); //set initial servo position if desired
  delay(50);
  d.write(65); //set initial servo position if desired
  
  delay(8000);  
  Serial.println("Arming Completed"); // so I can keep track of what is loaded
}
void initReceiver()
{
    vw_set_ptt_inverted(true); // Required for DR3100
    vw_set_rx_pin(6);
    vw_setup(2000);  // Bits per sec
    

    vw_rx_start();       // Start the receiver PLL running
    delay(1000);
    Serial.println("Receiver initialization Completed");
}
bool getInputs()
{ x="";
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN;

    if (vw_get_message(buf, &buflen)) // Non-blocking
    {
      for(int i=0;i<buflen;i++)
        x += char(buf[i]);
      Serial.println("Received Speed Request of " + String(x.toInt()));
      delay(20);
      
      return true;
    }
    delay(400);
    return false;
}
void setSpeed(int n){
        a.write(n + aoff);
        b.write(n + boff);
        c.write(n + coff);
        d.write(n + doff);
        Serial.println("Speed set to " + String(n));
}
void loop() {
  if(getInputs()){
    speedRequested = x.toInt();
    setSpeed(speedRequested);
  }
  SoftwareServo::refresh();
}
//
//  
//  while (Serial.available()) {
//    char c = Serial.read();  //gets one byte from serial bufferaa
//    
//    readString += c; //makes the string readString
//    delay(2);  //slow looping to allow buffer to fill with next character
//  }
//
//  if (readString.length() >0) {
//    Serial.println(readString);  //so you can see the captured string 
//    int n = readString.toInt();  //convert readString into a number
//    Serial.print("\nInput speed is :");
//    Serial.print(n);
//  
//    // auto select appropriate value, copied from someone elses code.
////if(n>0 && n<180){   
//      Serial.print("\nwriting Angle: ");
//      Serial.println(n);
//      a.write(n + aoff);
//            b.write(n + boff);
//                  c.write(n + coff);
//                        d.write(n + doff);
////    }
//
//    readString=""; //empty for next input
//  } 
//  SoftwareServo::refresh();
//}
