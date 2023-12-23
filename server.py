from flask import Flask, render_template
import api
app = Flask(__name__)

@app.route('/<int:location>')
def weather(location):
    temperature, windSpeed, pressure, humidity, condition, image, location = api.weather(location)
    return render_template('index.html', temperature=temperature, windSpeed=windSpeed, pressure=pressure, humidity=humidity, condition=condition, image=image, location=location)

@app.route('/favicon.ico')
def favicon():
    return render_template('favicon.ico')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')