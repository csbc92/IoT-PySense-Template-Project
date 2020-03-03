import pycom
import time

# Colors
RED=0xff0000
GREEN=0x00ff00
BLUE=0x0000ff
YELLOW=0xffff00

pycom.heartbeat(False)
while 1: # stop after 10 cycles
    pycom.rgbled(RED)
    time.sleep(1)
    pycom.rgbled(GREEN)
    time.sleep(1)
    pycom.rgbled(BLUE)
    time.sleep(1)
    pycom.rgbled(YELLOW)
    time.sleep(1)