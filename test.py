import os

os.environ["BLINKA_FT232H"] = "1"

# Test FT232H devices are enumerated correctly
from pyftdi.ftdi import Ftdi
Ftdi().open_from_url('ftdi:///?')

# Output should be something like:

# Available interfaces:
#  ftdi://ftdi:232h:1/1  (￿￿￿￿￿￿)



