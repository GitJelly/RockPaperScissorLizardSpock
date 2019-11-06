from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin
from HelperMethods import *

app = Flask(__name__)
CORS(app)


@app.route('/choice', methods=['GET'])
@cross_origin()
# Queries a service for random number. Returns JSON with ID: random number and name: Move Mapped with ID
def return_json_of_choice():
    computer_move_json = get_computer_move()                # query service for a random number , A JSON is returned
    computer_move = computer_move_json['random_number']
    computer_move = computer_move % 5 + 1      # Normalizing Random number [1-100]  to [1-5], adding '1' to avoid '0'

    move_name = get_movename_given_moveid(computer_move)   # getting move name mapping from Normalized Random number/id

    id_name_dictionary = {"id": computer_move, "name": move_name}

    return jsonify(id_name_dictionary)


@app.route('/choices', methods=['GET'])
@cross_origin()
# Returns a JSON with an array of JSONs inside
def return_json_of_choices():
    to_ret = ([{"id": 1, "name": "rock"}, {"id": 2, "name": "paper"}, {"id": 3, "name": "scissors"},
               {"id": 4, "name": "lizard"}, {"id": 5, "name": "spock"}])
    return jsonify(to_ret)


@app.route('/play', methods=['POST'])
@cross_origin()
# Returns a JSON with winner information
# The JSON looks: {"results": game_outcome, "player": player_choice, "computer": computer_move}
def move_outcome():
    my_json = get_computer_move()                       # getting a random move JSON

    computer_move = my_json['random_number']            # extacting random number from the JSON
    print("computer_move: ", computer_move)
    computer_move = computer_move % 5 + 1  # Normalizing Random number [1-100]  to [1-5], adding '1' to avoid '0'

    data = request.get_data()
    data = request.data

    data_to_string = data.decode("utf8")
    player_choice = json.loads(data_to_string)    # Converting a string to JSON to easy read the values
    player_choice = player_choice.get("player")

    player_move_name = get_movename_given_moveid(player_choice)
    computer_move_name = get_movename_given_moveid(computer_move)

    fin_response = get_result(player_move_name, computer_move_name)  # Calling with helper result function with move
    # info

    return jsonify(fin_response)            # converting dictionary to JSON


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
