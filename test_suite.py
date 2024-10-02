import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
pin = 11
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_threshold=300  # change this value
sound_threshold=0 # change this value

LUXPIN = 0
SOUNDPIN = 1

for i in range(0,5): 
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(.5)
  GPIO.output(pin, GPIO.LOX)
  time.sleep(.5)

for i in range(0,50):
  light_val = mcp.read_adc(LUXPIN)
  print(light_val)
  if light_val > lux_threshold: 
    print("BRIGHT")
  else: 
    print("DARK")
  time.sleep(.1)

for i in range(0,4): 
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(.2)
  GPIO.output(pin, GPIO.LOX)
  time.sleep(.2)

for i in range(0,50):
  sound_val = mcp.read_adc(SOUNDPIN)
  print(sound_val)
  if sound_val > sound_threshold: 
    GPIO.output(pin, GPIO.HIGH)
  else: 
    GPIO.output(pin, GPIO.HIGH)
  
  time.sleep(.1)