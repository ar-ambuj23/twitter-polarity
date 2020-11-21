from flask import Flask, jsonify, Response
from sentiment import polarityByCount, polarityByDay

import json
import datetime

app = Flask(__name__)

@app.route('/polarityByCount', methods = ['GET','POST'])
def getPolarityByCount():
    hashtag = '#trump'
    count = 100
    loc = 'USA'
    result = polarityByCount(hashtag, count, loc)
    return Response(json.dumps(result, default=default),  mimetype='application/json')

@app.route('/polarityByDay', methods = ['GET','POST'])
def getPolarityByDay():
    hashtag = '#trump'
    count = 100
    loc = 'USA'
    result = polarityByDay(hashtag, count, loc)
    return Response(json.dumps(result, default=default),  mimetype='application/json')

def default(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8000, debug=True)