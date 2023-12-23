from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route('/<int:location>')
def temperature(location):
    return render_template('index.html', temperature=api.temperature(location), location=api.place(location), windSpeed=api.windSpeed(location), pressure=api.pressure(location), humidity=api.humidity(location), condition=api.condition(location), image=api.image(location))

@app.route('/style.css')
def styles():
    return render_template('style.css')

@app.route('/index.css')
def index():
    return render_template('index.css')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')