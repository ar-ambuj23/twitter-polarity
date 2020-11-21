from flask import Flask, jsonify, Response, request
from sentiment import polarityByCount, polarityByDay, trendingHashtags
from woe import woe_map

import json
import datetime

app = Flask(__name__)

def process_request(args):
    search_params = dict()
    search_params['hashtag'] = '#' + args['hashtag']
    search_params['count'] = int(args['count'])
    search_params['loc'] = woe_map[args['loc']]['name']
    return search_params

@app.route('/home/<country>')
def getTrendingHashtags(country):
    woeid = woe_map[country]['woe']
    loc = woe_map[country]['name']
    trends = trendingHashtags(woeid=woeid, loc=loc)
    return jsonify(trends)

@app.route('/polarityByCount', methods = ['GET','POST'])
def getPolarityByCount():
    # print("In request: ByCount")
    args = request.args
    search_params = process_request(args)
    # print(search_params)
    result = polarityByCount(**search_params)
    return jsonify(result)
    #return Response(json.dumps(result, default=default),  mimetype='application/json')

@app.route('/polarityByDay', methods = ['GET','POST'])
def getPolarityByDay():
    # print("In request: ByDay")
    args = request.args
    search_params = process_request(args)
    # print(search_params)
    result = polarityByDay(**search_params)
    return jsonify(result)
    #return Response(json.dumps(result, default=default),  mimetype='application/json')

def default(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8000, debug=True)