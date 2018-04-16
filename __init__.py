from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zipId']
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=5e8a3fe9d9856e45c4b70d1c9ce27c54')
	json_object = r.json()
	temp = float(json_object['main']['temp'])
	#return str(temp)
	return render_template('temperature.html', temp=temp)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
