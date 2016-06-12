#include <Adafruit_NeoPixel.h>
#define LED_PIN 6 
#define LED_COUNT 12

// Create an instance of the Adafruit_NeoPixel class called "leds".
// That'll be what we refer to from here on...
Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// using A0 -- A12 as inputs
int key_state[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};      // variable to store the value read from the sensor pin
int key_play_time[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int threshold[] = {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20};
int max_time = 90;

// function declaration
int flashLight(int led_num);

void setup() {
  leds.begin();
  Serial.begin(9600);       // use the serial port
  for(int i = 0; i < LED_COUNT; i++) {
    leds.setPixelColor(i, 0x111111);
  }
  leds.show();
}

void loop() {
  for(int i = 0; i <= 12; i++) {
    int piezo = analogRead(i);
    if(piezo > threshold[i]) {
      if(key_state[i] == 0) {
        key_play_time[i] = 0;
        key_state[i] = 1;        
        flashLight(i);
      }
      else {
        key_play_time[i] += 1;
      }
    }
    else if (key_state[i] == 1) {
      key_play_time[i] += 1;
      if (key_play_time[i] > max_time) {
        key_state[i] = 0;
        flashLight(i);
      }
    }
  }
}


/*
void loop() {
  // read the sensor and store it in the variable sensorReading:
  for(int i = 0; i <= 12; i++) {
    sensorReading = analogRead(i);    
    // if the sensor reading is greater than the threshold and key_state is 0:
    if (sensorReading >= threshold && key_state[i] == 0) {
      // send the string "Knock!" back to the computer, followed by newline
        key_state[i] = 1;
        Serial.print("hit key: ");
        Serial.print(i);
        Serial.print(" sensor val: ");
        Serial.println(sensorReading);
    }
    else if (sensorReading < threshold ) {
      key_state[i] = 0;
    }
    flashLight(i);
  }
}
*/
int flashLight(int led_num) {
  if(key_state[led_num] == 1)
    leds.setPixelColor(led_num, 0xFFFFFF);
  else
    leds.setPixelColor(led_num, 0x111111);
  leds.show();
}
