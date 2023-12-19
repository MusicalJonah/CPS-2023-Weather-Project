from flask import Flask, render_template
import api

app = Flask(__name__)

@app.route('/V1/<int:location>')
def temperature(location):
    return render_template('V1_Template.html', temperature=api.temperature(location), place=api.place(location))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')