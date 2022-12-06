#define AZM_PIN A1
#define ELV_PIN A2

#define DOWN_PIN 12
#define UP_PIN 11
#define LEFT_PIN 10
#define RIGHT_PIN 9

#define LED_PIN 3

#define SWITCH_PIN 4
#define BUTTON_PIN 5

#include <EEPROM.h>



void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);

  pinMode(DOWN_PIN, OUTPUT);
  pinMode(UP_PIN, OUTPUT);
  pinMode(LEFT_PIN, OUTPUT);
  pinMode(RIGHT_PIN, OUTPUT);

  pinMode(LED_PIN, OUTPUT);

  pinMode(SWITCH_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  digitalWrite(LEFT_PIN, HIGH);
  digitalWrite(RIGHT_PIN, HIGH);
  digitalWrite(UP_PIN, HIGH);
  digitalWrite(DOWN_PIN, HIGH);
  digitalWrite(LED_PIN, LOW);

  analogReference(EXTERNAL);
  
}

void loop() {
  Serial.println(getAZMAngle(2.0,4.5));
  /*
  Serial.print(Serial.read());
  Serial.print(" ");
  Serial.println(Serial.available());
  
  
  if(Serial.available() > 1) {
    Serial.println("Hello World!");
  }  
  if(Serial.available() > 0) {
    int x = Serial.read();
    if(x == 49) {
      digitalWrite(13, HIGH);
      Serial.println("LED ON");
    }
    else if(x == 48) {
      digitalWrite(13, LOW);
      Serial.println("LED OFF");
    }
  }
  */
  delay(500);
}

void calibrate() {
  float voltageMin;
  float voltageMax; 

  EEPROM.update(0, voltageMin*10);
  EEPROM.update(0x8, voltageMax*10);
   
}

float getMinVoltage() {
  float minVoltage = EEPROM.read(0) / 10;
  return minVoltage;
}

float getMaxVoltage() {
  float maxVoltage = EEPROM.read(0x8) / 10;
  return maxVoltage;
}

void setMinVoltage(float minVoltage) {
  EEPROM.update(0, minVoltage);
}

void setMaxVoltage(float maxVoltage) {
  EEPROM.update(0x8, maxVoltage);
}


float getAZMAngle(float minVolts, float maxVolts) {
  
  int analogVal = analogRead(AZM_PIN);

  float voltage = analogVal*5.0/1023.0;
  float angle = (voltage - minVolts) * (450) / (maxVolts - minVolts) + 0;
  
  //(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
  return voltage;
}

float getELVAngle(float minVolts, float maxVolts) {
  
  int analogVal = analogRead(ELV_PIN);

  float voltage = analogVal*5.0/1023.0;
  float angle = (voltage - minVolts) * (450) / (maxVolts - minVolts) + 0;
  
  //(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
  return angle;
}

bool azmAction(int angle, float minVolts, float maxVolts) {

  float currentAngle = getAZMAngle(minVolts, maxVolts); 
  
  if(currentAngle > angle){
    while(currentAngle > angle) {
      currentAngle = getAZMAngle(minVolts, maxVolts);
      
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(LEFT_PIN, LOW);
    }
    digitalWrite(LED_PIN, LOW);
    digitalWrite(LEFT_PIN, HIGH);
    return true;
  }
  else if(currentAngle < angle){
    while(currentAngle < angle) {
      currentAngle = getAZMAngle(minVolts, maxVolts);
      
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(RIGHT_PIN, LOW);
    }
    digitalWrite(LED_PIN, LOW);
    digitalWrite(RIGHT_PIN, HIGH);
    return true;
  }
  else {
    return false;
  }
    
}

bool elvAction(int angle, float minVolts, float maxVolts) {

  float currentAngle = getELVAngle(minVolts, maxVolts); 
  
  if(currentAngle > angle){
    while(currentAngle > angle) {
      currentAngle = getELVAngle(minVolts, maxVolts);
      
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(DOWN_PIN, LOW);
    }
    digitalWrite(LED_PIN, LOW);
    digitalWrite(DOWN_PIN, HIGH);
    return true;
  }
  else if(currentAngle < angle){
    while(currentAngle < angle) {
      currentAngle = getELVAngle(minVolts, maxVolts);
      
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(UP_PIN, LOW);
    }
    digitalWrite(LED_PIN, LOW);
    digitalWrite(UP_PIN, HIGH);
    return true;
  }
  else {
    return false;
  }
    
}
