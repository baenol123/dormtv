from flask import Flask, request, jsonify
from crawler import get_meal
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/getmeal', methods = ['POST'])
def getmeal():
    req = request.get_json()
    print(req)
    meal = get_meal(req["code"], req["ymd"], req["weekday"])
    print("----------")
    print(meal)
    print("----------")
    return jsonify(meal)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3012')
