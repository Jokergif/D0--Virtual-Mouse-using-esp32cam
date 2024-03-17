link to tinkercad circuit: 

https://www.tinkercad.com/things/3lxg5Kh8w4H-neat-hillar/editel?sharecode=hkNQmZdKQUZhRgEhEbpUP1DjrUdO9X6mJiIqp0ZCQaw


Code:

#include <Keypad.h>
#include <Adafruit_LiquidCrystal.h>



Adafruit_LiquidCrystal lcd(0);

const byte rows=4;
const byte columns=4;

byte row_pins[rows]={9,8,7,6};
byte column_pins[columns]={5,4,3,2};

char key_array[rows][columns]={
{'1','2','3','A'},
{'4','5','6','B'},
{'7','8','9','C'},
{'*','0','#','D'}
};

Keypad k= Keypad(makeKeymap(key_array),row_pins,column_pins,rows,columns);


const int Actual_pin_size=4;
const int Password_size=Actual_pin_size+1 ;
char pass[Password_size]="12AB";
char Entered_pin[Password_size];

int red=12;
int green=13;
int i=0;


int lock_status=1;


void setup()
{
 Serial.begin(9600);
 lcd.begin(16,2);
 
 
 pinMode(red, OUTPUT);
 pinMode(green, OUTPUT);
 digitalWrite(red,HIGH);
 digitalWrite(green,LOW);
  
 lcd.setCursor(0,0);
 lcd.print("Door is locked.");
 delay(2000);
 lcd.clear();
  
  
  
  
}

void Unlock_activate()
  {
    lcd.setCursor(0,0);
    lcd.print("Enter pin:");
    
    char press = k.getKey();
    if(press)
    {
     Entered_pin[i]=press;
      
     lcd.setCursor(i,1);
      lcd.print(press);
     
     i++;
    
      
     if(i==(Password_size-1))
     {
       delay(1000);
       if(strcmp(Entered_pin,pass)==0)
       {
         digitalWrite(red,LOW);
         digitalWrite(green,HIGH);
         
         lcd.clear();
         lcd.setCursor(0,0);
         lcd.print("Door Unlocked");
         
         i=0;
         delay(2000);
         lock_status=0;
       }
       
       else
       {
         lcd.clear();
         lcd.setCursor(0,0);
         lcd.print("Wrong Pin");
         delay(2200);
         lcd.clear();
         i=0;
         lock_status=1;
         
       }
       
     }
    }
      
    
      
   }
  
  
  
  void Lock_activate()
  {
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);
    
    
  } 

void loop()
{
  if(lock_status==1)
  {
    Unlock_activate();
  }
  
  
} 



Explaination of code:
I have first included the necessary libraries.
Then I have initialised the LCD screen and keypad. 
After this, I have made a char array of password. the size of array is 4+1 i.e. 5 as one null character is there at end.
Then I have named the pins of the LEDs and set lock status as 1.
In void setup(), I have set baud rate, then set (16,2) as the number of columns and rows of the LCD screen respectively.
After this, LED pins have been set as output pins and RED light glows initially as the door is locked.
In void loop, I have just called the Unlock_activate function.
In this function, first the cursor is set at start and then prompt to enter pin.
Then input is taken using getKey() and printed on screen. 
Then when the size reaces 4 characters, it checks whether the password is correct or not. If correct, then green light is switched on and door is unlocked. 
Else it remains red and displayed wronog password.




