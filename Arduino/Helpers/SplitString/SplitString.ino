void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int id1, id2, id3;
  int pos1, pos2, pos3;
//  char* buf = "1:90&2:80&3:180";
  String buaf= "1:90&2:80&3:180";
  char buf[100];
  buaf.toCharArray(buf,sizeof(buaf));
  int n = sscanf(buf, "%d:%d&%d:%d&%d:%d", &id1, &pos1, &id2, &pos2, &id3, &pos3);
  Serial.print(F("n="));
  Serial.println(n);
  Serial.print(F("id1="));
  Serial.print(id1);
  Serial.print(F(", pos1="));
  Serial.println(pos1);
  Serial.print(F("id2="));
  Serial.print(id2);
  Serial.print(F(", pos2="));
  Serial.println(pos2);
  Serial.print(F("id3="));
  Serial.print(id3);
  Serial.print(F(", pos3="));
  Serial.println(pos3);

}
