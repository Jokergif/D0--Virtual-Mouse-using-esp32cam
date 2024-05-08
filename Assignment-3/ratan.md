## 1)Create a python file such that the user can input the x, y location and the mouse moves to that location. return the pixel values at that location and display it on the screen. library to be used are autopy or pyautogui 

```
import pyautogui

x=int(input("Enter the x coordinate between 0 to 1919 "))

y=int(input("Enter the y coordinate between 0 to 1079 "))

if x<1920 and y<1079 :
    pyautogui.moveTo(x,y,2)
    print(pyautogui.position())
```

## 2)Create a python file such that when you press a certain letter mouse is clicked automatically. use autopy/pyautogui and keyboard module
```
import keyboard
import pyautogui
while True:
    if keyboard.is_pressed("r"):
        pyautogui.click() 

```

## 3)Create a python file such that when a vowel is pressed you trigger the spacebar and the time between vowels being pressed in printed on the screen. use modules time and keyboard

```
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
```
