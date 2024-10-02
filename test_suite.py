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
lux_threshold=0  # change this value
sound_threshold=0 # change this value

LUXPIN = 0
SOUNDPIN = 1

epoch = time.time() 

system_time = time.time() - epoch
while True: 
  if system_time <= 5: 
    # Blink LED 
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(.5) 
    GPIO.output(pin, GPIO.LOW)
    time.sleep(.5) 
  elif system_time <= 10: 
    # Read Light Sensor and Output Value #

    val = mcp.read(LUXPIN)
    print(val)
    if val > lux_threshold: 
      print("BRIGHT")
    else: 
      print("DARK")
  else: 
    break

  system_time = time.time() - epoch
