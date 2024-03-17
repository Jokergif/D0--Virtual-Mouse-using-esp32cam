# Link for Simulation

https://www.tinkercad.com/things/kPW2MyriG1N-grand-jaagub-rottis/editel?sharecode=2EsThZhkfGMWn7Qe6fPD4Z4-Tv_e2QylLDLqxc4_iz8

## Code

#include <Keypad.h>
#include <LiquidCrystal.h>
const byte ROWS = 4; 
const byte COLS = 4; 
int length = 0;
int enteredKey = 0;
const int password = 9825;
int matched = 0;
// Initialising lcd object
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  
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
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);

  // Setting maximum size of lcd screen
  lcd.begin(16,2);
  lcd.print("Enter Password:");
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
        lcd.setCursor(0,1);
        lcd.print("Match!");
        // matched is set as one so that keypad doesn’t keep asking for password once lock is opened
        matched = 1;
       // Setting green LED to ON state
        digitalWrite(A0, HIGH);
      }
      else {
        length = 0;
        // Prints No match to the LCD screen
        lcd.setCursor(0,1);
        lcd.print("No match!");
        // Blinks red LED to signify incorrect password and awaits next attempt
        digitalWrite(A1, HIGH);
        delay(1000);
        digitalWrite(A1, LOW);
        delay(1000);
        lcd.clear();
      }
      enteredKey = 0;
    }
  }
}

## Circuit 

![image](https://github.com/Jokergif/D0--Virtual-Mouse-using-esp32cam/assets/161494158/72903693-7210-4ed0-b7a3-f2c56c2ec29b)

