from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '57670bd466msh428457352101b22p197e35jsnff03294b700c'
API_URL = 'https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert')
def convert():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    response = requests.get(API_URL, headers={
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'currency-conversion-and-exchange-rates.p.rapidapi.com'
    })
    data = response.json()
    rate = data['rates'][to_currency] / data['rates'][from_currency]
    return jsonify(rate=rate)

if __name__ == '__main__':
    app.run()