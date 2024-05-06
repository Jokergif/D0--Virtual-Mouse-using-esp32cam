#SOLUTION 1

import pyautogui #autopy
print("size of screen ", pyautogui.size()) #autopy.screen.size()    #returns resolution of the screen in format (x,y)
x = int(input("Enter X coordinate: "))            
y = int(input("Enter Y coordinate: "))
pyautogui.moveTo(x,y,1)  #autopy.mouse.move(x,y)  #moves the mouse to this location
print("Mouse moved")


#SOLUTION 2

import keyboard
import pyautogui
while True:
    if keyboard.is_pressed("j"):
        pyautogui.click() #autopy.mouse.click()'



#SOLUTION 3
import time
import keyboard
val = False
start = time.time()
while True:
    if any(keyboard.is_pressed(vowel) for vowel in ['a','e','i','o', 'u']) and not val:
        val = True
        keyboard.press_and_release("space")
        end = time.time()
        print(f"time: {end-start} ")
        start = time.time()
        
    if not any(keyboard.is_pressed(vowel) for vowel in ['a','e','i','o', 'u']) and val:   #if you run the code without this line and the val thing 
        #you will notice that the while loop runs multiple times even though you pressed it once. val ensures that it only runs once. only when you release the key the val returns to false
        #allowing you to run the code again when pressing a new key
        val = False
