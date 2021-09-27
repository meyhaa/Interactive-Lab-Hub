import time 
import os
import subprocess
import digitalio
import board
import datetime
from PIL import Image, ImageDraw, ImageFont
from time import strftime, sleep
from datetime import timedelta
import adafruit_rgb_display.st7789 as st7789



# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

#defining the buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    #image = Image.new("RGB", (width, height))
    draw.rectangle((0, 0, width, height), outline=0, fill=0) #NOT WORKING - need to find a way to clear the image from the screen after button A and B are pressed
    #draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,255))
    y = top
    date = "Today is: " + (strftime("%m/%d/%Y")) #displaying the date in an easy to read fashion
    time1 = "The time is: " + (strftime("%H:%M:%S"))    #displaying the time in an easy to read fashion

    
    if buttonB.value and not buttonA.value:  # just button A pressed
        #print ("in here3")
        image = Image.open("congrats.jpg") # set the screen to a congratulatory image
    if buttonA.value and not buttonB.value:  # just button B pressed
        #print ("in here4")
        image = Image.open("motivational.jpg")  # set the screen to a motivational image
        #draw.rectangle((0, 0, width, height), outline='black', fill=(0,0,0,255)) #clearing the image
    backlight = digitalio.DigitalInOut(board.D22)
    backlight.switch_to_output()
    backlight.value = True
   
    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))
    
    disp.image(image, rotation)