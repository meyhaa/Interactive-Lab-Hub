import time 
import os
import subprocess
import digitalio
import board
import datetime
from PIL import Image, ImageDraw, ImageFont
from time import strftime, sleep
from datetime import timedelta, datetime
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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


while True:
    #image = Image.new("RGB", (width, height))
    y = top
 
    backlight.value = True
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    date = strftime("%A, %b %d") #displaying the date 
    clock = strftime("%I:%M:%S %p")   #displaying the time
    clock1 = '08:00:25 AM'
    clock2 = '1:15:40 PM'
    clock3 = '6:30:55 PM'
    # [-15, -10, -3]
    a = -15
    
    #draw.text((x, top), date, font=font, fill='#FFFFFF')
    #draw.text((x, top+30), clock, font=font, fill='#FFFFFF')
    
    if (int(strftime("%H"))+a >= 7 and int(strftime("%H"))+a < 12):
        draw.rectangle((0,0, width, height), outline=0, fill="#F8C22E")
        message = 'Rise and Shine'
        if buttonA.value and not buttonB.value:
            image = Image.open("sun.png")
    elif (int(strftime("%H"))+a >= 12 and int(strftime("%H"))+a < 17):
        draw.rectangle((0,0,width, height), outline=0, fill="#63CCE2")
        message = 'Productivity vibes'
        if buttonA.value and not buttonB.value:
            image = Image.open("productive.png")
    elif (int(strftime("%H"))+a >= 17 and int(strftime("%H"))+a < 22):
        draw.rectangle((0,0, width, height), outline=0, fill="#6B8BE2")
        message = 'Remember to take breaks'
        if buttonA.value and not buttonB.value:
            image = Image.open("bread.jpeg")
    elif (int(strftime("%H"))+a >= 22 or int(strftime("%H"))+a < 7):
        draw.rectangle((0,0, width, height), outline=0, fill="#1A2F57")
        message = 'Time to sleep!'
        #draw.text((x, top+90), 'Time to sleep!', font=font, fill='#FFFFFF')
        if buttonA.value and not buttonB.value:
            image = Image.open("sleep.jpeg")
            
    draw.text((x, top), date, font=font, fill='#FFFFFF')
    draw.text((x, top+30), clock1, font=font, fill='#FFFFFF')
    draw.text((x, top+90), message, font=font, fill='#FFFFFF')
    
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