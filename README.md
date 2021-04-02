# Nudge

Nudge was conceived as a way to anonymously let someone know you are thinking about them without demanding a response. Especially during these challenging times, Nudge is meant to remind people that they are not alone.

You can find more information about Nudge on [my website](https://www.richardfxr.com/projects/nudge).

## Prerequisites

You'll need these before you can get Nudge up and running.

### Hardware Prerequisites

- [Adafruit Matrix Portal](https://www.adafruit.com/product/4745)
- [32x16 LED matrix](https://www.adafruit.com/product/420)
- A web server where you can host the webpage

Note that the code will not work properly with LED matrices of a different resolution without some changes. This is also true for other microcontrollers.

### Software Prerequisites

- [CircuitPython](https://circuitpython.org/)
- [Adafruit IO](https://io.adafruit.com/)

## Setup

### LED Matrix and CircuitPython

Connect the Matrix Portal to the LED matrix by following [Adafruit’s Matrix Portal prep guide](https://learn.adafruit.com/adafruit-matrixportal-m4/prep-the-matrixportal).

Install CircuitPython on the Matrix Portal using [Adafruit’s CircuitPython guide](https://learn.adafruit.com/adafruit-matrixportal-m4/install-circuitpython).

### Adafruit IO

Setup an Adafruit IO account and create a new feed. Ensure that the new feed has one data point.

Open [index.html](Webpage/index.html), you will find the URL for the PUT requests on lines 125, 139, 153, 167, and 181 that looks like:

```
url: "https://io.adafruit.com/api/v2/IO_USERNAME/feeds/feed_id/data/id?x-aio-key=IO_KEY",
```

Replace the following:

- ``IO_USERNAME``: Your Adafruit IO username found under the “My Key” tab.
- ``feed_id``: The feed ID found under the “Feed Info” section of your new feed.
- ``id``: The ID for the data point can be found by going to ``https://io.adafruit.com/api/v2/IO_USERNAME/feeds/feed_id/data/``.
- ``IO_KEY``: Your Adafruit IO key found under the “My Key” tab.

Note that Adafruit IO may be updated in the future. Refer to the [Adafruit IO API documentation](https://io.adafruit.com/api/docs/#adafruit-io-http-api) if above method fails.

### Webpage

Upload the updated HTML, CSS, and SVG files under the Webpage folder to your server and ensure the page works correctly. Here is a [live version of the page](https://www.richardfxr.com/nudge) for comparison. Don’t forget to update line 19 of [index.html](Webpage/index.html) with your name. 

### Matrix Portal

Update [secrets.py](secrets.py) with the SSID and password of your Wi-Fi network.

Connect the Matrix Portal to your computer. Copy [secrets.py](secrets.py), [code.py](code.py), and everything inside the BMPs folder into CIRCUITRY. Make sure the BMP files are in the top-level directory and not inside a folder like they are here on Github.

The Matrix Portal should start running the code automatically. Check the output in a compatible editor such as the [Mu editor](https://codewith.mu/). If all goes well, you should see the following output:

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

Functions by [Erin St Blaine](https://learn.adafruit.com/users/firepixie) from the [Ocean Epoxy Resin Lightbox with RGB LED Matrix Image Scroller guide](https://learn.adafruit.com/ocean-epoxy-resin-lightbox-with-rgb-led-matrix-image-scroller/circuitpython-code) were used in [code.py](code.py).