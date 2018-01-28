#include <Wire.h>
#include <math.h>
#include "MMA7660.h"
MMA7660 accelemeter;

const int tempPin = A3;
const int B = 4275;               // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
const int redLedPin = 3;
const int greenLedPin = 4;


String readString;
String startstring;
int8_t x;
int8_t y;
int8_t z;
float ax, ay, az;
float temperature;
float R;
int a;

void setup()
{
  accelemeter.init();
  Serial.begin(9600);
  pinMode(tempPin, INPUT);
  pinMode(redLedPin, OUTPUT);
  pinMode(greenLedPin, OUTPUT);

}
void loop()
{
      accelemeter.getXYZ(&x, &y, &z);
      Serial.print("x");
      Serial.print(x);
      Serial.print("y");
      Serial.print(y);
      Serial.print("z");
      Serial.print(z);

      accelemeter.getAcceleration(&ax, &ay, &az);
      Serial.print("a");
      Serial.print(ax);
      Serial.print("b");
      Serial.print(ay);
      Serial.print("c");
      Serial.print(az);

      a = analogRead(tempPin);
      R = 1023.0 / a - 1.0;
      R = R0 * R;
      temperature = 1.0 / (log(R / R0) / B + 1 / 298.15) - 273.15; // convert to temperature via datasheet
      Serial.print("t");
      Serial.print(temperature);
      Serial.println("k");

      if(temperature>33.0) // 30 Celsius ->86 F //41 Cel -> 105.8
      {
        float exceed = temperature - 33.0;
        digitalWrite(redLedPin, HIGH);
        delay(15 - 2*exceed);
        digitalWrite(redLedPin, LOW);
        delay(30 - 2*exceed);
        digitalWrite(redLedPin, HIGH);
        delay(15 - 2*exceed);
        digitalWrite(redLedPin, LOW);
      }
      else{
      digitalWrite(greenLedPin, HIGH);
      delay(15);
      digitalWrite(greenLedPin, LOW);
      delay(30);
      digitalWrite(greenLedPin, HIGH);
      delay(15);
      digitalWrite(greenLedPin, LOW);
      }

}


