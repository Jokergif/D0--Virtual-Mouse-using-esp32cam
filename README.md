  # ESP32 Based Virtual Mouse #
Abhinith D, Jobin Jacob, Madhav Kedia 

<br>

## INTRODUCTION ##
In this project we are designing a virtual mouse controlled by hand gestures. The project will implement an ESP32CAM microcontroller attached to the OV2640 Camera Module. The microcontroller is used to capture the hand gestures, and the hand gestures are processed and identified using Image Processing using OpenCV. The mouse would be able to be controlled wirelessly and perform tracking and clicking operations.

<br>

## OBJECTIVE  ##
The main objective is to implement the virtual mouse, while using an ESP32CAM to capture video and to build proficiency in using embedded systems and microcontrollers, image processing and OpenCV libraries.

<br>


## DESCRIPTION ##
* The project consists of two main parts – ESP32CAM embedded system and Image processing using python
* The ESP32CAM is used to record continuous video and stream it to a web server created using the wi-fi capabilities of the ESP32CAM.
* The Image processing consists of writing python code to identify hands and fingers in the streamed video and recognize hand gestures to wirelessly control a mouse
* The functionalities of the virtual mouse will include movement and clicking

<br>


### MATERIALS ###
* ESP32CAM
* FT232RL FTDI USB to TTL Adapter
* Micro USB cable
* Breadboard
* Jumper cables

<br>


## TIMELINE ##

| Phase	Time               | 	Goals |
| -----------              | ------ |
| Phase 1 (learning phase) | Feb 1 – Feb12 :	Learning Arduino basics and simulation of basic circuits |
| | Feb 13 – Feb 28 :	Learn ESP interface with Adafruit and camera applications |
| | Mar 1 – Mar 20 :	Introduction to python and OpenCV libraries |
| Phase 2 (implementation) |  Mar 21 – Apr 5	: Implementing the gesture identification using OpenCV libraries on webcam |
| | April 5 - April 22	: Implementing the ESP32CAM Web Server  |




