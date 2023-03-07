void setup() {
  Serial.begin(9600);
  

}

void loop() {
  if(Serial.available() > 0) {
    byte incomingByte = Serial.read();
    //Serial.println(incomingByte);
    switch(incomingByte) {
      case 0x1:
        Serial.println("LEFT");
        break;
      case 0x2:
        Serial.println("RIGHT");
        break;
      case 0x3:
        Serial.println("UP");
        break;
      case 0x4:
        Serial.println("DOWN");
        break;   
    }
    Serial.read();
  }

}
