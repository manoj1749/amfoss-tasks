int distance = 0;

#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  
  lcd.begin(16, 2);
  lcd.print("Parking Slot");
}

void loop()
{ // getting input from parking slot
  distance = 0.01723 * readUltrasonicDistance(7, 7);
  // checking parking slot
  if (distance <= 300) {
            lcd.setCursor(0, 1);
    // Printing a message on the LCD.
             lcd.print("Filled Up ");
}
  if (distance > 300) {
            lcd.setCursor(0, 1);
    // Printing a message on the LCD.
            lcd.print("Is Empty");
  }  
} 
