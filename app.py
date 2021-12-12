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

app = Flask(__name__)

unicornhathd.rotation(90)
unicornhathd.brightness(0.6)
unicornhd_width, unicornhd_height = unicornhathd.get_shape()
unicornhathd.off()

NUM_LEDS = unicornhd_width * unicornhd_height

def get_led_position(led):
    return (led % unicornhd_height, led // unicornhd_width)

def toggle_leds(leds, transition_color, new_color):
    orig_colors = []

    for led in leds:
        # TODO can we unpack led into x, y
        orig_colors.append(unicornhathd.get_pixel(led[0], led[1]))

    for n in range(NUM_TRANSITIONS):
        for l in range(len(leds)):
            this_led = leds[l]
            unicornhathd.set_pixel(this_led[0], this_led[1], transition_color[0], transition_color[1], transition_color[2])

        unicornhathd.show()
        time.sleep(0.3)

        for l in range(len(leds)):
            this_led = leds[l]
            this_orig_color = orig_colors[l]
            unicornhathd.set_pixel(this_led[0], this_led[1], new_color[0], new_color[1], new_color[2])
            unicornhathd.show()

def query_led_status(led):
    pos = get_led_position(led)

    # TODO can we unpack pos
    r, g, b = unicornhathd.get_pixel(pos[0], pos[1])
    toggle_leds([pos], COLOR_BIT_QUERYING, (r, g, b))

    return not (r == 0 and g == 0 and b == 0)

def set_led_status(leds):
    # TODO
    return

def add_to_filter(element):
    # TODO
    return

def exists_in_filter(element):
    for n in range(NUM_HASH_FUNCTIONS):
        led = mmh3.hash(element, n) % NUM_LEDS
        print(str(led))

        if (query_led_status(led) == False):
            return False

    return True

def reset_filter():
    for n in range(2):
        for x in range(unicornhd_width):
            for y in range(unicornhd_height):
                unicornhathd.set_pixel(x, y, 0, 0, 255)

        unicornhathd.show()
        time.sleep(0.3)
        unicornhathd.off()
        time.sleep(0.3)

    return True

@app.route(f'/{API_PATH_PREFIX}/add/<element>', methods=['POST'])
def add(element):
    return jsonify({ 'result': add_to_filter(element) }), 201

@app.route(f'/{API_PATH_PREFIX}/exists/<element>')
def exists(element):
    return jsonify({ 'result': exists_in_filter(element) })

@app.route(f'/{API_PATH_PREFIX}/reset', methods=['POST'])
def reset():
    return jsonify({ 'result': reset_filter() })

@app.route('/')
def homepage():
    return render_template('homepage.html')

