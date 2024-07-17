# this tests the FT232H and the IS31FL3741 LED driver
# pip install adafruit-circuitpython-bme280
# pip install adafruit-circuitpython-is31fl3741

import os
from board import I2C
import adafruit_is31fl3741
from adafruit_is31fl3741.adafruit_rgbmatrixqt import Adafruit_RGBMatrixQT
from webcolors import name_to_rgb

COLOR = "purple"

os.environ["BLINKA_FT232H"] = "1"


def loop_intensity(led_matrix):
    while True:
        # Increase intensity from 0 to 255
        for intensity in range(8, 64, 8):
            led_matrix.global_current = intensity
            led_matrix.show()
            # time.sleep(0.01)  # Adjust the sleep time as needed

        # Decrease intensity from 255 to 0
        for intensity in range(64, 8, -8):
            led_matrix.global_current = intensity
            led_matrix.show()
            # time.sleep(0.01)  # Adjust the sleep time as needed


def create_color_int(r: int, g: int, b: int) -> int:
    return (r << 16) | (g << 8) | b


def get_color(color: str) -> int:
    rgb = name_to_rgb(color)
    return create_color_int(rgb.red, rgb.green, rgb.blue)


def create_matrix() -> Adafruit_RGBMatrixQT:
    i2c = I2C()
    new_matrix = Adafruit_RGBMatrixQT(i2c, allocate=adafruit_is31fl3741.PREFER_BUFFER)
    new_matrix.set_led_scaling(0xFF)
    new_matrix.global_current = 0
    new_matrix.enable = True
    new_matrix.fill(0)
    return new_matrix


def create_face_matrix():
    led_matrix = create_matrix()
    # Define the coordinates for the eyes and the mouth of the smiley face
    eyes = [(5, 3), (8, 3)]
    mouth = [(4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 6)]
    for eye in eyes:
        led_matrix.pixel(eye[0], eye[1], get_color(COLOR))
    for mouth_pixel in mouth:
        led_matrix.pixel(mouth_pixel[0], mouth_pixel[1], get_color(COLOR))
    return led_matrix


def create_gradient_matrix(led_matrix, start_color_int, end_color_int, width, height):
    # Convert integer colors back to RGB components
    start_color_rgb = ((start_color_int >> 16) & 0xFF, (start_color_int >> 8) & 0xFF, start_color_int & 0xFF)
    end_color_rgb = ((end_color_int >> 16) & 0xFF, (end_color_int >> 8) & 0xFF, end_color_int & 0xFF)

    # Calculate the step change for each color component
    step_change = [(end_color_rgb[i] - start_color_rgb[i]) / (width - 1) for i in range(3)]

    for x in range(width):
        # Calculate the color for the current column
        current_color = [int(start_color_rgb[i] + (step_change[i] * x)) for i in range(3)]
        color_int = create_color_int(*current_color)

        # Apply the color to each pixel in the current column
        for y in range(height):
            led_matrix.pixel(x, y, color_int)


# Define the start (orange) and end (purple) colors
orange = name_to_rgb("darkorange")
purple = name_to_rgb("purple")

# Convert RGB tuples to integers
start_color_int = create_color_int(purple.red, purple.green, purple.blue)
end_color_int = create_color_int(orange.red, orange.green, orange.blue)

# Assuming `matrix` is your Adafruit_RGBMatrixQT object
matrix = create_matrix()
create_gradient_matrix(matrix, start_color_int, end_color_int, 16, 9)
matrix.global_current = 64
matrix.show()
