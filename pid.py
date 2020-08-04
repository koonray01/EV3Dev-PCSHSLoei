#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_C, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor

tank = MoveTank(OUTPUT_C, OUTPUT_D)
tank.cs = ColorSensor()

try:
    # Follow the line for 4500ms
    tank.follow_line(
        kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(30),
        follow_for=follow_for_ms,
        ms=4500
    )
except LineFollowErrorTooFast:
    tank.stop()
    raise