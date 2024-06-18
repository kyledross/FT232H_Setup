# check to see if environment variable is set
import os
if "BLINKA_FT232H" in os.environ:
    print("BLINKA_FT232H is set to", os.environ["BLINKA_FT232H"])
else:
    print("BLINKA_FT232H is not set")


# Test FT232H devices are enumerated correctly
from pyftdi.ftdi import Ftdi
Ftdi().open_from_url('ftdi:///?')

# Output should be something like:

# Available interfaces:
#  ftdi://ftdi:232h:1/1  (￿￿￿￿￿￿)



