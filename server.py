from flask import Flask, render_template
import api
app = Flask(__name__)

@app.route('/<int:location>')
def weather(location):
    temperature, windSpeed, pressure, humidity, condition, image, location = api.weather(location)
    return render_template('index.html', temperature=temperature, windSpeed=windSpeed, pressure=pressure, humidity=humidity, condition=condition, image=image, location=location)

@app.route('/style.css')
def styles():
    return render_template('style.css')

@app.route('/index.css')
def index():
    return render_template('index.css')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')