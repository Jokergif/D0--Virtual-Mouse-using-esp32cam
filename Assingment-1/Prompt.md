# Link to Tinkercad simulation

[Simulation link](https://www.tinkercad.com/things/lwO5oeR44gj-spectacular-wluff?sharecode=F-7gNb_psBFdDZKYmgDVeq7S7xp1P5aNCYsEcEbRX1c)


# Code/Circuit and explanations

## Code

#include <Keypad.h>
#include <LiquidCrystal.h>

const byte ROWS = 4; 
const byte COLS = 4; 
int length = 0;
int enteredKey = 0;
const int password = 1034;
int matched = 0;

// Initialising lcd object
LiquidCrystal lcd(A4, A5, 13, 12, 11, 10);  

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; 
byte colPins[COLS] = {5, 4, 3, 2}; 

// Initialising keypad object
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  Serial.begin(9600);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, OUTPUT);

  // Setting maximum size of lcd screen
  lcd.begin(16,2);
}
  
void loop(){
  // Condition below checks if the password has been entered correctly or not
  if(!matched){
    char customKey = customKeypad.getKey();
  
    // If length of entered key is under four, keep accepting numbers
    if (customKey && length < 4){
      enteredKey = enteredKey*10 + (customKey - 48);
      length++;
      lcd.clear();
      lcd.print(enteredKey);
      delay(1000);
      lcd.clear();
      // Changes display to asterisks so that password is not displayed on the LCD screen (for more 
     // than 1 second)
      for(int i = 0; i < length; lcd.print("*"), i++);
    }
    else if (length == 4){
      if (enteredKey == password){
        // Prints Match to the LCD screen
        lcd.setCursor(0, 1);
        lcd.print("Match!");
        // matched is set as one so that keypad doesn’t keep asking for password once lock is opened
        matched = 1;
       // Setting green LED to ON state
        digitalWrite(A2, HIGH);
      }
      else {
        length = 0;
        // Prints No match to the LCD screen
        lcd.setCursor(0, 1);
        lcd.print("No match!");
        // Blinks red LED to signify incorrect password and awaits next attempt
        digitalWrite(A3, HIGH);
        delay(1000);
        digitalWrite(A3, LOW);
        delay(1000);
        lcd.clear();
      }
      enteredKey = 0;
    }
  }
}





## Circuit
 

8 pins run from keypad to the Arduino

4 data pins of LCD screen are connected to the Arduino

Register select and Enable pins are connected to Arduino and are set automatically by the library

V0 contrast pin is connected to a potentiometer so the contrast on the screen can be controlled by the user

LED pins are connected through pull up resistor to power and ground to control the backlight on the screen
When a number is entered, it is displayed on the screen like so for 1 second:
 

Then the number is replaced by an asterisk to hide the entered password:

 

When the 4 digit code matches the hard coded pre-set password, the green LED turns on:
 

When the password is wrong, the red LED blinks and the screen is cleared for the next attempt:
 
 


