from flask import Flask
from flask import jsonify
from flask import render_template
import mmh3
import time
import unicornhathd

API_PATH_PREFIX = 'api'
NUM_HASH_FUNCTIONS = 6
COLOR_BIT_SET = (255, 0, 0)
COLOR_BIT_WRITING = (0, 255, 0)
COLOR_BIT_QUERYING = (0, 0, 255) 
NUM_TRANSITIONS = 4

unicornhathd.rotation(90)
unicornhathd.brightness(0.6)
unicornhd_width, unicornhd_height = unicornhathd.get_shape()
unicornhathd.off()

NUM_LEDS = unicornhd_width * unicornhd_height

try:
    #for y in range(u_height):
    #    for x in range(u_width):
    #        unicornhathd.set_pixel(x, y, 255, 0, 0)

    unicornhathd.set_pixel(0, 0, 255, 0, 0)
    unicornhathd.set_pixel(15, 15, 0, 0, 255)
    unicornhathd.show()

    while True:
        continue

except KeyboardInterrupt:
    unicornhathd.off()
