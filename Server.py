from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route('/V1/<int:location>')
def temperature(location):
    return render_template('index.html', temperature=api.temperature(location), location=api.place(location), windSpeed=api.windSpeed(location))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')