import requests
from Constant import *


# Debug/Test message
def my_print_helper():
    print("Hello")


# Getting from an external REST service
def get_computer_move():
    id = 0
    PARAMS = {"player": id}
    url = URL_RANDOM_NUMBER_SERVICE             # URL from Constant file

    try:
        r = requests.get(url, PARAMS)
        return r.json()
    except requests.exceptions.RequestException as e:
        print(e)


# Uses dictionary mapping to get the movename
def get_movename_given_moveid(id):
    if id < 1 or id > 5:
        raise ValueError("Invalid id received:", id, " please try again")

    id_to_name_mapping = DICTIONARY_MAPPING_ID_TO_NAME    # Referencing from Constant File
    return id_to_name_mapping[id]


# Checks winning condition and returns a dixtionary response
def get_result(player_choice, computer_move):
    precedence_mapping = WINNER_KEY_LOOSERSET_AS_VALUE_DICTIONARY    # referencing from constant file

    # precedence_mapping: Is a dictionary that has keys of all possible/valid player moves
    #        The value of each key is a set of moves that have low precedence over the key or that loose over key

    is_mapping_present = computer_move in precedence_mapping[player_choice]

    # RESULT LOGIC: Check from mappingTable that if the player move set contains the computerMove
    #               If yes it contains -> player wins
    #               If NOT it implies that the computer won
    #               If Both make the same move then its a TIE
    if player_choice == computer_move:
        game_outcome = "tie"
    elif is_mapping_present:
        game_outcome = "win"
    else:
        game_outcome = "loose"

    fin_response = {"results": game_outcome, "player": player_choice, "computer": computer_move}
    return fin_response


