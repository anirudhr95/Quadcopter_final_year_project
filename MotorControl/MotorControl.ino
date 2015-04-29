// zoomkat 10-22-11 serial servo test
// type servo position 0 to 180 in serial monitor
// or for writeMicroseconds, use a value like 1500
// for IDE 0022 and later
// Powering a servo from the arduino usually *DOES NOT WORK*.

String readString;
#include <Servo.h> 
#include <SoftwareServo.h> 
SoftwareServo a,b,c,d;  // create servo object to control a servo 
static int aoff=-6;
static int boff=2;
static int coff=4;
static int doff=-4;
void setup() {
  
  Serial.begin(9600);
 
  
  a.attach(9);  //the pin for the servo control 
delay(100);
    b.attach(10);
      c.attach(11);
        d.attach(12);
          delay(100);
   a.write(65); //set initial servo position if desired
      b.write(65); //set initial servo position if desired
         c.write(65); //set initial servo position if desired
            d.write(65); //set initial servo position if desired
//myservo.writeMicroseconds(1500);
//myservo.writeMicroseconds(1500);
  delay(8000);  
  Serial.println("servo-test-22-dual-input"); // so I can keep track of what is loaded



  Serial.println("Enter inputs"); // so I can keep track of what is loaded
}

void loop() {
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
  
    // auto select appropriate value, copied from someone elses code.
//if(n>0 && n<180){   
      Serial.print("\nwriting Angle: ");
      Serial.println(n);
      a.write(n + aoff);
            b.write(n + boff);
                  c.write(n + coff);
                        d.write(n + doff);
//    }

    readString=""; //empty for next input
  } 
  SoftwareServo::refresh();
}
