#include <Servo.h>


String readString;
//#include <Servo.h> 
//#include <VirtualWire.h> 
Servo a,b,c,d;  // create servo object to control a servo 

#define aoff 0
#define boff 0
#define coff 0
#define doff 0

//static int aoff=-6;
//static int boff=0;
//static int coff=4;
//static int doff=-4;
String x = "";
int speedRequested;
void setup() {
  
  Serial.begin(9600);
//  initReceiver();
   arm();
}
void arm(){
  a.attach(5);  //the pin for the servo control 
  a.write(65); //set initial servo position if desired    
  b.attach(3);
    b.write(65); //set initial servo position if desired
  c.attach(6);
    c.write(65); //set initial servo position if desired
  d.attach(10);
  d.write(65); //set initial servo position if desired
    delay(15);
    
    
    
    
    delay(1500);
 
  
  
  Serial.println("Arming Completed"); // so I can keep track of what is loaded
}

void setSpeed(int n){
        a.write(n);
        
        b.write(n);
        
        c.write(n);
        
        d.write(n);
        delay(15);
        
        Serial.println("Speed set to " + String(n));
        
}
void loop() {
  
//  
  while (Serial.available()) {
    char c = Serial.read();  //gets one byte from serial bufferaa
    
    readString += c; //makes the string readString
    delay(2);  //slow looping to allow buffer to fill with next character
  }

  if (readString.length() >0) {
    Serial.println(readString);  //so you can see the captured string 
    int n = readString.toInt();  //convert readString into a number
    Serial.print("\nInput speed is :");
    Serial.print(n);
    setSpeed(n);
    readString=""; //empty for next input
  } 
  
}
