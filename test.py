# Test FT232H

from pyftdi.ftdi import Ftdi
Ftdi().open_from_url('ftdi:///?')

