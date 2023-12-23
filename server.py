from flask import Flask, render_template
import os
import logging
import api

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

@app.route('/<int:location>')
def weather(location):
    try:
        temperature, windSpeed, pressure, humidity, condition, image, location = api.weather(location)
        return render_template('index.html', temperature=temperature, windSpeed=windSpeed, pressure=pressure, humidity=humidity, condition=condition, image=image, location=location)
    except Exception as e:
        app.logger.error(f"Error occurred when fetching weather for location {location}: {e}")
        return "An error occurred. Please try again later.", 500

@app.route('/favicon.ico')
def favicon():
    return render_template('favicon.ico')

if __name__ == '__main__':
    app.run(host='0.0.0.0')