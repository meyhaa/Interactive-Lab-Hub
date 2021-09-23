import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
import emoji

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

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

# These setup the code for our buttons
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

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
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    date = strftime("%A, %b %d")
    clock = strftime("%I:%M:%S %p")

    shape = [(0.8*width,0.9*height), (width, height+0.33*height)]

    # Morning color: yellow
    if (int(strftime("%H")) >= 7 and int(strftime("%H")) < 12):
        draw.rectangle((0,0, width, height), outline=0, fill="#F8C22E")
        if buttonB.value and not buttonA.value: # just button A
            print('here') #display.fill

    # Afternoon color: blue
    elif (int(strftime("%H")) >= 12  and int(strftime("%H")) < 17):
        draw.rectangle((0,0, width, height), outline=0, fill="#63CCE2")
    # Evening color: purple
    elif (int(strftime("%H")) >= 17  and int(strftime("%H")) < 21):
        draw.rectangle((0,0, width, height), outline=0, fill="#6B8BE2")
    # Night color: dark blue    elif (int(strftime("%H")) >= 21  or  int(strftime("%H")) < 7):
        draw.rectangle((0,0,width, height), outline=0, fill="#1A2F57")
    draw.text((x, top), date, font=font, fill="#FFFFFF")
    draw.text((x, top+30), clock, font=font, fill="#FFFFFF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
