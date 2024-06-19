# Adafruit FT232H USB Breakout Board Setup

## This document describes how to setup the Adafruit FT232H USB breakout board on a Debian system.

### What is the Adafruit FT232H USB breakout board?
The Adafruit FT232H USB breakout board is a USB to serial UART interface with a GPIO and I2C interface.  
https://www.adafruit.com/product/2264

### Getting the environment setup to use the board

#### Install libusb
libusb is a library that provides generic access to USB devices.  Once installed, rule files define the permissions for the FT232H USB breakout board.

```commandline
sudo apt install libusb-1.0-0
sudo nano /etc/udev/rules.d/11-ftdi.rules
```
Add the following lines to the /etc/udev/rules.d/11-ftdi.rules file:

```text
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6001", GROUP="plugdev", MODE="0666"  
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6011", GROUP="plugdev", MODE="0666"  
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6010", GROUP="plugdev", MODE="0666"  
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6014", GROUP="plugdev", MODE="0666"  
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6015", GROUP="plugdev", MODE="0666"
```

#### Install Python packages into your virtual environment
```commandline
pip install pyftdi
pip install Adafruit-blinka
```

#### Set environment variable in your project

BLINKA_FT232H=1

This can be set in your project's environment or in your Python code.

```python
import os
os.environ["BLINKA_FT232H"] = "1"
```


#### Test the FT232H USB breakout board
1. Connect the FT232H USB breakout board to your computer.
2. Run test.py to see that the board is attached and your environment is setup correctly.

### What's next

From this point, you can use the FT232H USB breakout board in your Python project.
Install and import the required Python packages for whatever you have attached to the breakout board.
See the test_display.py file for an example of how to use the FT232H USB breakout board with an LED display.