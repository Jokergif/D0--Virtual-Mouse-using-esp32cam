#SOLUTION 1

import pyautogui #autopy
print("size of screen ", pyautogui.size()) #autopy.screen.size()
x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))
pyautogui.moveTo(x,y,1)  #autopy.mouse.move(x,y)
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
        
    if not any(keyboard.is_pressed(vowel) for vowel in ['a','e','i','o', 'u']) and val:
        val = False
