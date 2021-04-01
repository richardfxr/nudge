# Nudge
# Version 2.5
#
# Author: Richard (Xiangrui Fu)
# Device: Adafruit Matrix Portal M4
# Language: CircuitPython
#
# RISD Hacking the Smart Home final project
#
# Interact with Nudge at https://www.richardfxr.com/nudge
# More info at https://www.richardfxr.com/projects/nudge



#-- INITIALIZATION ----------------------------------------#


# nudge logo
print()
print("             *          ")
print("             *          ")
print("***  *  *  ***  **   ** ")
print("*  * *  * *  * *  * ****")
print("*  * *  * *  * *  * *   ")
print("*  *  ***  **   ***  ** ")
print("                  *     ")
print("                **      ")
print()


print("-- INITIALIZING NUDGE -----")


# code info
print("   - Code: v2.5")


# import user information
try:
    from secrets import secrets
except ImportError:
    print()
    print("-- WARNING -------------------")
    print("   - Failed to import user data")
    print("     Please ensure secrets.py exists in the same directory as code.py")
    print()
    raise

print("   - User information imported successfully")


print()



#-- IMPORTS ----------------------------------------------#


print("-- IMPORTS -------------------")


# general
import math
import time
import random
import board
import busio
import microcontroller

print("   - Imported: general libraries")


# display
import adafruit_imageload.bmp
import displayio
import framebufferio
import rgbmatrix
import ulab

print("   - Imported: display libraries")


# WiFi
from digitalio import DigitalInOut, Direction, Pull
import adafruit_requests as requests
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_matrixportal.network import Network
import adafruit_esp32spi.adafruit_esp32spi_socket as socket

print("   - Imported: WiFi libraries")


# Adafruit IO API
from adafruit_matrixportal.matrixportal import MatrixPortal

print("   - Imported: API library")

print("   - SUCCESS")
print()



#-- BOARD SETUP ------------------------------------------#


print("-- BOARD SETUP ---------------")

matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=False)

print("   - SUCCESS")
print()



#-- DISPLAY SETUP ----------------------------------------#


print("-- DISPLAY SETUP -------------")


# release previous display
displayio.release_displays()

print("   - Previous display released")


# Reshader class
class Reshader:
    '''reshader fades the image to mimic brightness control'''
    def __init__(self, palette):
        self.palette = palette
        ulab_palette = ulab.zeros((len(palette), 3))
        for i in range(len(palette)):
            rgb = int(palette[i])
            ulab_palette[i, 2] = rgb & 0xff
            ulab_palette[i, 1] = (rgb >> 8) & 0xff
            ulab_palette[i, 0] = rgb >> 16
        self.ulab_palette = ulab_palette
 
    def reshade(self, brightness):
        '''reshader'''
        palette = self.palette
        shaded = ulab.array(self.ulab_palette * brightness, dtype=ulab.uint8)
        for i in range(len(palette)):
            palette[i] = tuple(shaded[i])

print("   - Reshader class loaded")


def do_crawl_down(image_file, *,
                  speed=12, weave=4, pulse=.5,
                  weave_speed=1/6, pulse_speed=1/7):
    # pylint:disable=too-many-locals
    '''function to scroll the image from bottom to top'''
    the_bitmap, the_palette = adafruit_imageload.load(
        image_file,
        bitmap=displayio.Bitmap,
        palette=displayio.Palette)
 
    shader = Reshader(the_palette)
 
    group = displayio.Group()
    tile_grid = displayio.TileGrid(bitmap=the_bitmap, pixel_shader=the_palette)
    group.append(tile_grid)
    display.show(group)
 
    start_time = time.monotonic_ns()
    start_y = display.height   # High enough to be "off the top"
    end_y = -the_bitmap.height     # Low enough to be "off the bottom"
 
    # Mix up how the bobs and brightness change on each run
    r1 = random.random() * math.pi
    r2 = random.random() * math.pi
 
    y = start_y
    while y > end_y:
        now = time.monotonic_ns()
        y = start_y - speed * ((now - start_time) / 1e9)
        group.y = round(y)
 
        # wave from side to side
        group.x = round(weave * math.cos(y * weave_speed + r1))
 
        # Change the brightness
        if pulse > 0:
            shader.reshade((1 - pulse) + pulse * math.sin(y * pulse_speed + r2))
 
        display.refresh(minimum_frames_per_second=0, target_frames_per_second=60)

print("   - do_crawl_down function loaded")


def do_crawl_sideways(image_file, *,
                  speed=12, weave=4, pulse=.5,
                  weave_speed=1/6, pulse_speed=1/7):
    # pylint:disable=too-many-locals
    '''function to scroll the image from left to right'''
    the_bitmap, the_palette = adafruit_imageload.load(
        image_file,
        bitmap=displayio.Bitmap,
        palette=displayio.Palette)
 
    shader = Reshader(the_palette)
 
    group = displayio.Group()
    tile_grid = displayio.TileGrid(bitmap=the_bitmap, pixel_shader=the_palette)
    group.append(tile_grid)
    display.show(group)
 
    start_time = time.monotonic_ns()
    start_x = display.width   # High enough to be "off the top"
    end_x = -the_bitmap.width     # Low enough to be "off the bottom"
 
    # Mix up how the bobs and brightness change on each run
    r1 = random.random() * math.pi
    r2 = random.random() * math.pi
 
    x = start_x
    while x > end_x:
        now = time.monotonic_ns()
        x = start_x - speed * ((now - start_time) / 1e9)
        group.x = round(x)
 
        # wave from side to side
        group.y = round(weave * math.cos(x * weave_speed + r1))
 
        # Change the brightness
        if pulse > 0:
            shader.reshade((1 - pulse) + pulse * math.sin(x * pulse_speed + r2))
 
        display.refresh(minimum_frames_per_second=0, target_frames_per_second=60)

print("   - do_crawl_sideways function loaded")


def do_pulse(image_file, *, duration=4, pulse_speed=1/8, pulse=.5):
    '''pulse animation'''
    the_bitmap, the_palette = adafruit_imageload.load(
        image_file,
        bitmap=displayio.Bitmap,
        palette=displayio.Palette)
 
    shader = Reshader(the_palette)
 
    group = displayio.Group()
    tile_grid = displayio.TileGrid(bitmap=the_bitmap, pixel_shader=the_palette)
    group.append(tile_grid)
    group.x = (display.width - the_bitmap.width) // 2
    group.y = (display.height - the_bitmap.height) // 2
    display.show(group)
 
    start_time = time.monotonic_ns()
    end_time = start_time + int(duration * 1e9)
 
    now_ns = time.monotonic_ns()
    while now_ns < end_time:
        now_ns = time.monotonic_ns()
        current_time = (now_ns - start_time) / 1e9
 
        shader.reshade((1 - pulse) - pulse
                       * math.cos(2*math.pi*current_time*pulse_speed)**2)
 
        display.refresh(minimum_frames_per_second=0, target_frames_per_second=60)

print("   - do_pulse function loaded")


def frameAni(image_file, frame):
    # pylint:disable=too-many-locals
    '''fucntion for frame-by-frame animation'''
    i = 0

    while i < frame:
        do_pulse(image_file + str(i) +".bmp", duration=0.005, pulse=0)
        i += 1


print("   - do_crawl_down function loaded")



# create display object
matrix = rgbmatrix.RGBMatrix(
    width=32, bit_depth=5,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2
    ],
    addr_pins=[
        board.MTX_ADDRA,
        board.MTX_ADDRB,
        board.MTX_ADDRC
    ],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)

print("   - Display object created")

# display boot screen
do_pulse("/nudgelogo.bmp", duration=0.1, pulse=0)

print("   - Displaying boot screen")

print("   - SUCCESS")
print()



#-- ANIMATIONS -------------------------------------------#


def aniOne():
    print("   - Playing: Animation 1")
    do_crawl_sideways("/aniOne.bmp", speed=70, weave=0, pulse=0)
    do_crawl_sideways("/aniOne.bmp", speed=70, weave=0, pulse=0)
    blankScreen()


def aniTwo():
    print("   - Playing: Animation 2")
    frameAni("aniTwo", 19)
    blankScreen()


def aniThree():
    print("   - Playing: Animation 3")
    frameAni("aniThree", 25)
    blankScreen()


def aniFour():
    print("   - Playing: Animation 4")
    do_crawl_down("/aniFour.bmp", speed=60, weave=0, pulse=0)
    blankScreen()


def blankScreen():
    print("   - Blanking screen")
    do_pulse("/blank.bmp", duration=0.1, pulse=0)


#-- WIFI SETUP -------------------------------------------#


print("-- WIFI SETUP ----------------")

# connect to WiFi
print("   - ", end="")
apiFeed = matrixportal.get_io_feed("nudge", detailed=True)
aniNum = apiFeed["last_value"]

print("   - API value: " + aniNum)

# erase boot screen
blankScreen()

print()


#-- MAIN LOOP --------------------------------------------#


print("-- MAIN LOOP -----------------")

prevNum = aniNum

while True:

    #-- ADAFRUIT IO API ----------------------------------#

    apiFeed = matrixportal.get_io_feed("nudge", detailed=True)
    aniNum = apiFeed["last_value"]

    print("   - API value: " + aniNum)


    #-- TRIGGER ANIMTION ---------------------------------#

    if aniNum != prevNum:

        if aniNum == "1":
            aniOne()
        
        elif aniNum == "2":
            aniTwo()

        elif aniNum == "3":
            aniThree()
        
        elif aniNum == "4":
            aniFour()

        else:
            blankScreen()

    prevNum = aniNum
    
    