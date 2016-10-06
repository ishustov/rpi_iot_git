import RPi.GPIO as GPIO
from time import sleep

# For I600 RaspberyPi v2
red = 10  # GPIO number where red led is connected
green = 22 # GPIO number where green led is connected
blue = 27 # GPIO number where blue led is connected

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Reset led light
def cleanLed():
  GPIO.output(red, True)
  GPIO.output(blue, True)
  GPIO.output(green, True)

# turn on red led
def redOn():
  GPIO.output(red, False)

# turn on blue led
def blueOn():
  GPIO.output(blue, False)

# turn on green led
def greenOn():
  GPIO.output(green, False)

# turn red led off
def redOff():
  GPIO.output(red, True)

# turn blue led off
def blueOff():
  GPIO.output(blue, True)

# turn green led off
def greenOff():
  GPIO.output(green, True)

# turns the leds on and off in Polyrithmic fashion
def polyrithmOn():
  for i in range (0, 60, 1):

    if i%3==0:
      greenOn()
    elif i%3!=0:
      greenOff()

    if i%4==0:
      blueOn()
    elif i%4!=0:
      blueOff()

    if i%5==0:
      redOn()
    elif i%5!=0:
      redOff()

sleep(0.5)
