#include <Adafruit_NeoPixel.h>
#define LED_PIN 6 
#define LED_COUNT 1

// Create an instance of the Adafruit_NeoPixel class called "leds".
// That'll be what we refer to from here on...
Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// these constants won't change:
const int mux_sig_pin = A0; // the piezo is connected to analog pin 0
const int threshold = 100;  // threshold value to decide when the detected sound is a knock or not

int mux_ctrl_pins[] = {2, 3, 4, 5};
int sensorReading = 0;

// these variables will change:
int key_state[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};      // variable to store the value read from the sensor pin

// function declaration
int readMux(int chan);     // reads from the analog mux
int flashLight(int led_num);

void setup() {
  for(int i = 0; i < 4; i++){
    pinMode(mux_ctrl_pins[i], OUTPUT);
    digitalWrite(mux_ctrl_pins[i], LOW);
  }
  leds.begin();
  Serial.begin(9600);       // use the serial port
  leds.setPixelColor(0, 0xFFFFFF);
  leds.show();
}

void loop() {
  // read the sensor and store it in the variable sensorReading:
  for(int i = 0; i < 13; i++) {
    sensorReading = readMux(i);    
   // Serial.print("sensor: ");
   // Serial.print(i);
   // Serial.print(" - ");
   // Serial.print(sensorReading); 
    // if the sensor reading is greater than the threshold:
    if (sensorReading >= threshold) {
      // send the string "Knock!" back to the computer, followed by newline
      key_state[i] = !key_state[i];
      Serial.print("hit key: ");
      Serial.println(i);
      Serial.print("sensor val: ");
      Serial.println(sensorReading);
      //flashLight(i);
    }
  }
}

int flashLight(int led_num) {
  if(key_state[led_num] == 1)
    leds.setPixelColor(led_num, 0xFF00FF);
  else
    leds.setPixelColor(led_num, 0x00FF00);
  leds.show();
}

// Read a value from the mux.
int readMux(int chan) {
  for(int i = 0; i < 4; i++){
    if((chan >> i) & 0x0001 == 1)
      digitalWrite(mux_ctrl_pins[i], HIGH);
    else
      digitalWrite(mux_ctrl_pins[i], LOW);
  }
  delayMicroseconds(1);
  return analogRead(mux_sig_pin);
}
