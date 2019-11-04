from flask import Flask, jsonify, request
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/choice', methods=['GET'])
@cross_origin()
def returnJSONOFCHOICE():
    # r = urllib.request.urlopen('https://codechallenge.boohma.com/random')  # -> good
    id = 0
    PARAMS = {"player": id}
    r = requests.get('https://codechallenge.boohma.com/random', PARAMS)
    # randjson = r.
    # mystr = randjson.decode("utf8")
    # myjson = json.loads(mystr)
    myjson = r.json()
    computermove = myjson['random_number']
    computermove = computermove % 5 + 1
    id = computermove

    if id == 1:
        movename = "rock"
    elif id == 2:
        movename = "paper"
    elif id == 3:
        movename = "scissor"
    elif id == 4:
        movename = "lizard"
    else:
        movename = "spock"

    jsontosend = {"id": computermove, "name": movename}

    return jsontosend


@app.route('/choices', methods=['GET'])
@cross_origin()
def returnJSONOFCHOICES():
    toret = ([{"id": 1, "name": "rock"}, {"id": 2, "name": "paper"}, {"id": 3, "name": "scissors"},
                    {"id": 4, "name": "lizard"}, {"id": 5, "name": "spock"}])
    return jsonify(toret)


@app.route('/play', methods=['POST'])
@cross_origin()
def moveoutcome():
    id = 0
    PARAMS = {"player": id}
    r = requests.get('https://codechallenge.boohma.com/random', PARAMS)
    # r = request.urlopen('https://codechallenge.boohma.com/random')  #-> good
    # randjson = r.read()
    # mystr = randjson.decode("utf8")

    # myjson = json.loads(mystr)
    myjson = r.json()
    computermove = myjson['random_number']
    computermove = computermove % 5
    data = request.get_data()
    data = request.data

    datatostring = data.decode("utf8")

    playerchoice = json.loads(datatostring)

    playerchoice = playerchoice.get("player")

    if playerchoice < computermove:
        gameoutcome = "loose"
    elif playerchoice > computermove:
        gameoutcome = "win"
    else:
        gameoutcome = "tie"

    finresponse = {"results": gameoutcome, "player": playerchoice, "computer": computermove}

    return jsonify(finresponse)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
