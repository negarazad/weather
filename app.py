from flask import Flask, render_template, request
import requests

app = Flask(name)
API_KEY = 'YOUR_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    return render_template('weather.html', weather=weather_data)

if name == 'main':
    app.run(debug=True)
