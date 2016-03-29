// zoomkat 10-22-11 serial servo test
// type servo position 0 to 180 in serial monitor
// or for writeMicroseconds, use a value like 1500
// for IDE 0022 and later
// Powering a servo from the arduino usually *DOES NOT WORK*.

String readString;
#include <Servo.h> 
Servo myservo;  // create servo object to control a servo 

void setup() {
  
  Serial.begin(9600);
 
  
  myservo.attach(12);  //the pin for the servo control 
  delay(100);
   myservo.write(65); //set initial servo position if desired
//myservo.writeMicroseconds(1500);
  delay(4000);  
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
      myservo.write(n);
//    }

    readString=""; //empty for next input
  } 
}
