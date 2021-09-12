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
    # TODO
    return

def toggle_leds(leds, transition_color, new_color):
    # TODO
    return

def query_led_status(led):
    # TODO
    return

def set_led_status(leds):
    # TODO
    return

def add_to_filter(element):
    # TODO
    return

def exists_in_filter(element):
    # TODO
    return

def reset_filter():
    # TODO
    return

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
