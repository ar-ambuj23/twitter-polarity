from flask import Flask, jsonify, Response
from sentiment import perDayPolarity
import json
import datetime

app = Flask(__name__)

@app.route('/polarity', methods = ['GET','POST'])
def getPolarity():
    hashtag = 'trump'
    loc = 'USA'
    result = perDayPolarity(hashtag, loc)
    print(result)
    return Response(json.dumps(result, default=default),  mimetype='application/json')

def default(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8000)