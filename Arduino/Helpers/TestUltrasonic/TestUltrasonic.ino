#define ultra_Trig_Pin_A 10

#define ultra_Echo_Pin_A 11
#define ultra_Trig_Pin_B 14
#define ultra_Echo_Pin_B 15

float ultrainternalDistanceMeasure(int echo_pin){
  int  duration = pulseIn(echo_pin, HIGH) ; //sensor stops reading after some time - adding delay 26/03
//  Serial.println(duration);
  int distance = (duration/2) / 29.1;
  
  if(distance >=200 || distance <= 0){
    return -1;
  }
  
  
  return distance;
  
}
float ultrainternalTrigger(int trig_pin, int echo_pin){
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);
  return ultrainternalDistanceMeasure(echo_pin);
}
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ultra_Trig_Pin_A, OUTPUT);
pinMode(ultra_Trig_Pin_B, OUTPUT);
pinMode(ultra_Echo_Pin_A  , INPUT);
pinMode(ultra_Echo_Pin_B  , INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.flush();
//  Serial.print(ultrainternalTrigger(ultra_Trig_Pin_A,ultra_Echo_Pin_A));
//  Serial.print("\t");
  delay(500);
  Serial.print(ultrainternalTrigger(ultra_Trig_Pin_B,ultra_Echo_Pin_B));
  Serial.println();
  
  

}
