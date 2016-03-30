#ifndef printHelper_h
#define printHelper_h
  void printData(float *ypr, int *ultra, int *motorSpeeds){ 
    
    Serial.print("ypr\t");
    Serial.print(ypr[0]);
    Serial.print("\t");
    Serial.print(ypr[1]);
    Serial.print("\t");
    Serial.print(ypr[2]);


    // VectorInt16 aaReal = getAccel();
    // Serial.print("areal\t");
    // Serial.print(aaReal.x);
    // Serial.print("\t");
    // Serial.print(aaReal.y);
    // Serial.print("\t");
    // Serial.println(aaReal.z);

  // Ultrasonic
    Serial.print(ultragetA());
    Serial.print("\t");
    Serial.print(ultragetB());
    Serial.print("\t");
    Serial.print(ultragetC());
    Serial.print("\t");
    Serial.print(ultragetD());

  //  Serial.print(ultragetA());
  //  Serial.print("\t");
  //  delay(50);


  //  MOTOR
    for(int i=0;i<=3;i++){
      Serial.print(motorSpeeds[i]);
      Serial.print("\t");
    }
    Serial.println();

    
  }

#endif /* printHelper_h */