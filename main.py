#!/usr/bin/python3
import time
import nxt.locator
import nxt.motor

def drop_card():
    with nxt.locator.find() as b:
        mymotor = b.get_motor(nxt.motor.Port.A)
        mymotor.turn(-25, 220)
        mymotor.turn(100, 200)

while True:
    drop_card() 
    time.sleep(1)
