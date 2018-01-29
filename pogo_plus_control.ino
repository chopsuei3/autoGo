bool vibrating = false;
unsigned long timeSincePress = 0;
unsigned long vibStart = 0;
int userInput;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  pinMode(9, OUTPUT);
  delay(1000);
  analogWrite(9, 255);
  delay(50);
  analogWrite(9, 0);
  Serial.begin(9600);
  Serial.println("Initialization");
}

// the loop routine runs over and over again forever:
void loop() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);
  userInput = Serial.read();

  if (userInput == 35) {
//    Serial.println("Reset signal received, pressing button");
    analogWrite(9, 255);
    delay(50);
    analogWrite(9, 0);
  }
  
 // Serial.println(voltage);
  if (voltage < 0.1) {
    if (vibrating == false) {
      vibrating = true;
      vibStart = millis();
    }
  }
  else {
    if (voltage > 3.1) {
      if (vibrating == true) {
        vibrating = false;
        int vibDuration = millis() - vibStart;
        Serial.print(millis());
        Serial.print(", ");
        Serial.print(vibDuration);
        if (vibDuration > 800 && vibDuration < 1100) { // only press for existing mons
            if (millis() - timeSincePress >= 3000) {
              Serial.println("ms, Button pressed");
              timeSincePress = millis();
              analogWrite(9, 255);
              delay(50);
              analogWrite(9, 0);
            }
            else {
              Serial.println("ms");
            }
        }
        else if (vibDuration > 2200 && vibDuration < 2400) {
          Serial.println("ms, Pokemon Caught");
        }
        else if (vibDuration  > 450 && vibDuration < 650){
          Serial.println("ms, Pokemon Not Caught");
        }
        else {
          Serial.println("ms");
        }
      }
    }
  }
}
