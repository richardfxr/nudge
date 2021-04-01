# Nudge

Nudge was conceived as a way to anonymously let someone know you are thinking about them without demanding a response. Especially during these challenging times, Nudge is meant to remind people that they are not alone.

You can find more information about Nudge on [my website](https://www.richardfxr.com/projects/nudge).

## Getting Started

These instructions will get your very own Nudge up and running!

### Hardware Prerequisites

- [Adafruit Matrix Portal](https://www.adafruit.com/product/4745)
- [32x16 LED matrix](https://www.adafruit.com/product/420)
- A web server where you can host the webpage

Note that the code will not work properly with LED matrices of a different resolution without some changes. This is also true for other microcontrollers.

### Software Prerequisites

- [CircuitPython](https://circuitpython.org/)

### Setup

Connect the Matrix Portal to the LED matrix by following [Adafruit’s Matrix Portal prep guide](https://learn.adafruit.com/adafruit-matrixportal-m4/prep-the-matrixportal).

Install CircuitPython on the Matrix Portal using [Adafruit’s CircuitPython guide](https://learn.adafruit.com/adafruit-matrixportal-m4/install-circuitpython).

Upload the HTML, CSS, and SVG files under Webpage to your server and ensure the page works correctly. Here is a [live version of the page](https://www.richardfxr.com/nudge) for comparison. Don’t forget to update the HTML file with your name. 

Update [secrets.py](secrets.py) with the SSID and password of your Wi-Fi network.

Connect the Matrix Portal to your computer. Copy [secrets.py](secrets.py), [code.py](code.py), and everything inside the BMPs folder into CIRCUITRY. Make sure the BMP files are in the top-level directory and not inside a folder like they are here on Github.

The Matrix Portal should start running the code automatically. Check the output in a compatible IDE such as the [Mu editor](https://codewith.mu/). If all goes well, you should see the following output:

```

             *
             *
***  *  *  ***  **   **
*  * *  * *  * *  * ****
*  * *  * *  * *  * *
*  *  ***  **   ***  **
                  *
                **

-- INITIALIZING NUDGE -----
   - Code: v2.5
   - User information imported successfully

-- IMPORTS -------------------
   - Imported: general libraries
   - Imported: display libraries
   - Imported: WiFi libraries
   - Imported: API library
   - SUCCESS

-- BOARD SETUP ---------------
   - SUCCESS

-- DISPLAY SETUP -------------
   - Previous display released
   - Reshader class loaded
   - do_crawl_down function loaded
   - do_crawl_sideways function loaded
   - do_pulse function loaded
   - do_crawl_down function loaded
   - Display object created
   - Displaying boot screen
   - SUCCESS

-- WIFI SETUP ----------------
   - Connecting to yourSSID
   - API value: 0
   - Blanking screen

-- MAIN LOOP -----------------
   - API value: 0
```

## Acknowledgments

Functions by [Erin St Blaine](https://learn.adafruit.com/users/firepixie) from the [Ocean Epoxy Resin Lightbox with RGB LED Matrix Image Scroller guide](https://learn.adafruit.com/ocean-epoxy-resin-lightbox-with-rgb-led-matrix-image-scroller) were used in [code.py](code.py).