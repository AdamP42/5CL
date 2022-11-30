# screen /dev/tty.usbmodem0740D1DAFC051 115200
# True clockwise (unscrew mirror)

import board
import digitalio
import time

step = digitalio.DigitalInOut(board.IO7)
step.direction = digitalio.Direction.OUTPUT
dir = digitalio.DigitalInOut(board.IO10)
dir.direction = digitalio.Direction.OUTPUT
micro_step = digitalio.DigitalInOut(board.IO3)
micro_step.direction = digitalio.Direction.OUTPUT
micro_step.value = True
dir.value = True
step.value = False

def rotate(num, delay, mod):
for i in range(int(200 * mod * num)):
step.value = True
step.value = False
time.sleep(delay)

def rotate():
if micro_step.value:
mod = 16

for i in range(int(200 * mod)):
step.value = True
# time.sleep(.01)
step.value = False
time.sleep(.01)

def rotate(num, delay, mod):
for i in range(int(200 * mod * num)):
step.value = True
step.value = False
time.sleep(delay)