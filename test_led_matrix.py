# this tests the FT232H and the IS31FL3741 LED driver

from board import I2C
import adafruit_is31fl3741
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
from webcolors import name_to_rgb


def create_color_int(r: int, g: int, b: int) -> int:
    return (r << 16) | (g << 8) | b


def get_color(color: str) -> int:
    rgb = name_to_rgb(color)
    return create_color_int(rgb.red, rgb.green, rgb.blue)


def create_matrix() -> Adafruit_RGBMatrixQT:
    i2c = I2C()
    new_matrix = Adafruit_RGBMatrixQT(i2c, allocate=adafruit_is31fl3741.PREFER_BUFFER)
    new_matrix.set_led_scaling(0xFF)
    new_matrix.global_current = 0xFF
    new_matrix.enable = True
    new_matrix.fill(0)
    return new_matrix


matrix = create_matrix()

# Define the coordinates for the eyes and the mouth of the smiley face
eyes = [(5, 3), (8, 3)]
mouth = [(4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 6)]

for eye in eyes:
    matrix.pixel(eye[0], eye[1], get_color("yellow"))

for mouth_pixel in mouth:
    matrix.pixel(mouth_pixel[0], mouth_pixel[1], get_color("yellow"))

matrix.show()
