#define AZM_PIN A1
#define ELV_PIN A2

#define BLEFT_PIN 9
#define BRIGHT_PIN 10
#define BUP_PIN 11
#define BDOWN_PIN 12

#define UP_PIN 5
#define DOWN_PIN 6
#define LEFT_PIN 7
#define RIGHT_PIN 8

#define LED_PIN 3

#define SWITCH_PIN 4
#define BUTTON_PIN 5

#define MINVOLTAGE_AZM_ADDRESS 0
#define MAXVOLTAGE_AZM_ADDRESS 0x8

#include <EEPROM.h>



void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);

  pinMode(BDOWN_PIN, INPUT_PULLUP);
  pinMode(BUP_PIN, INPUT_PULLUP);
  pinMode(BLEFT_PIN, INPUT_PULLUP);
  pinMode(BRIGHT_PIN, INPUT_PULLUP);

  pinMode(UP_PIN ,OUTPUT);
  pinMode(DOWN_PIN ,OUTPUT);
  pinMode(LEFT_PIN ,OUTPUT);
  pinMode(RIGHT_PIN ,OUTPUT);

  pinMode(LED_PIN, OUTPUT);

  pinMode(SWITCH_PIN, INPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  digitalWrite(LEFT_PIN, HIGH);
  digitalWrite(RIGHT_PIN, HIGH);
  digitalWrite(UP_PIN, HIGH);
  digitalWrite(DOWN_PIN, HIGH);
  digitalWrite(LED_PIN, LOW);

  analogReference(EXTERNAL);

  Serial.println("hello");
  
}

int commandAction(byte command) { 
 switch(command) {
  case 0x1:
    azmLeft(); 
    return 0xFFFFFFFF;
  case 0x2:
    azmRight();
    return 0xFFFFFFFF; 
  case 0x3:
    elvUp();
    return 0xFFFFFFFF; 
  case 0x4:
    elvDown();
    return 0xFFFFFFFF; 
  case 0x5:
    return 0xFFFFFFFF; 
  case 0x6: 
    return 0xFFFFFFFF;
  case 0x7:
    return 0xFFFFFFFF; 
  case 0x8:
    azmStop();
    return 0xFFFFFFFF; 
  case 0x9:
    elvStop(); 
    return 0xFFFFFFFF;
  case 0xA:
    allStop();
    return 0xFFFFFFFF;
  case 0xB:
    return 0xFFFFFFFF; 
  case 0xC:
    return 0xFFFFFFFF;
  case 0xD:
    return 0xFFFFFFFF;
  case 0xE:
    return 0xFFFFFFFF;
  case 0xF:
    return 0xFFFFFFFF;
 }
 if(command >= 0x30 && command < 0x40) {
  return command ^ 0x30 ;
 }
 if(command >= 0x20 && command < 0x30) {
  return command ^ 0x20;  
 }
}

void calibrate() {
  float voltageMin;
  float voltageMax; 

  //Needs to be written

  //EEPROM.update(MINVOLTAGE_ADDRESS, voltageMin*10);
  //EEPROM.update(MAXVOLTAGE_ADDRESS, voltageMax*10);
   
}

float getMinVoltage() {
  //float minVoltage = EEPROM.read(MINVOLTAGE_ADDRESS) / 10;
  //return minVoltage;
}

float getMaxVoltage() {
  //float maxVoltage = EEPROM.read(MAXVOLTAGE_ADDRESS) / 10;
  //return maxVoltage;
}

void setMinVoltage(float minVoltage) {
  //EEPROM.update(MINVOLTAGE_ADDRESS, minVoltage);
}

void setMaxVoltage(float maxVoltage) {
  //EEPROM.update(MAXVOLTAGE_ADDRESS, maxVoltage);
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

void azmLeft() {
  digitalWrite(LEFT_PIN, LOW);
  digitalWrite(LED_PIN, HIGH);
}  

void azmRight() {
  digitalWrite(RIGHT_PIN, LOW);
  digitalWrite(LED_PIN, HIGH);
}  

void elvUp() {
  digitalWrite(UP_PIN, LOW);
  digitalWrite(LED_PIN, HIGH);
}  

void elvDown() {
  digitalWrite(DOWN_PIN, LOW);
  digitalWrite(LED_PIN, HIGH);
}  

void azmStop() {
  digitalWrite(LEFT_PIN, HIGH);
  digitalWrite(RIGHT_PIN, HIGH);
  digitalWrite(LED_PIN, LOW);
}  

void elvStop() {
  digitalWrite(UP_PIN, HIGH);
  digitalWrite(DOWN_PIN, HIGH);
  digitalWrite(LED_PIN, LOW);
}  

void allStop(){
  azmStop();
  elvStop();
} 

void loop() {
  //Serial.println(getAZMAngle(2.0,4.5));
  /*
  Serial.print(Serial.read());
  Serial.print(" ");
  Serial.println(Serial.available());
  
  
  if(Serial.available() > 0) {
    byte message = Serial.read();
    //Serial.println(message, HEX);
    int response = commandAction(message);
    Serial.println(response, HEX);
    //Serial.read();
  } */

  //float voltage = analogRead(AZM_PIN)*5.0/1023.0;
  //Serial.println(voltage);
  //delay(10);

  if(digitalRead(BUP_PIN) == LOW) digitalWrite(UP_PIN, LOW);
  else digitalWrite(UP_PIN,HIGH);

  if(digitalRead(BDOWN_PIN) == LOW) digitalWrite(DOWN_PIN, LOW);
  else digitalWrite(DOWN_PIN,HIGH);

  if(digitalRead(BLEFT_PIN) == LOW) digitalWrite(LEFT_PIN, LOW);
  else digitalWrite(LEFT_PIN,HIGH);

  if(digitalRead(BRIGHT_PIN) == LOW) digitalWrite(RIGHT_PIN, LOW);
  else digitalWrite(RIGHT_PIN,HIGH);
}
