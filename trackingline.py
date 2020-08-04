#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev.ev3 import *
from time import sleep

tank_drive = MoveTank(OUTPUT_C, OUTPUT_D)
left_speed = 0
right_speed = 0 
cl = ColorSensor()
cl.mode='COL-REFLECT'

Mid = 13.5

while True:
    if (cl.value() < Mid):
        tank_drive.on(50, 60)    

    else:
        tank_drive.on(60,30)    
