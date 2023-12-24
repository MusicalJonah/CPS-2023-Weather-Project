from flask import Flask, render_template
import os
import logging
from logging.handlers import RotatingFileHandler
import api

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

# Set up Werkzeug logging
werkzeug_logger = logging.getLogger('werkzeug')
handler = RotatingFileHandler('access.log', maxBytes=10000, backupCount=1)
werkzeug_logger.addHandler(handler)
werkzeug_logger.setLevel(logging.INFO)

@app.route('/<int:location>')
def weather(location):
    try:
        temperature, windSpeed, pressure, humidity, condition, image, location = api.weather(location)
        return render_template('index.html', temperature=temperature, windSpeed=windSpeed, pressure=pressure, humidity=humidity, condition=condition, image=image, location=location)
    except Exception as e:
        app.logger.error(f"Error occurred when fetching weather for location {location}: {e}")
        return "An error occurred. Please try again later.", 500