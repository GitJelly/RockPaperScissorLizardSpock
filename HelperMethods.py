import requests


def my_print_helper():
    print("Hello")


def get_computer_move():
    id = 0
    PARAMS = {"player": id}
    r = requests.get('https://codechallenge.boohma.com/random', PARAMS)
    return r.json()


def get_movename_given_moveid(id):

    if id == 1:
        move_name = "rock"
    elif id == 2:
        move_name = "paper"
    elif id == 3:
        move_name = "scissor"
    elif id == 4:
        move_name = "lizard"
    else:
        move_name = "spock"

    # json_tosend = {"id": id, "name": move_name}
    return move_name


def get_result(player_choice, computer_move):

    precedence_mapping = {"rock": {"scissor", "lizard"}, "paper": {"rock", "spock"}, "scissor": {"paper", "lizard"},
                          "lizard": {"spock", "paper"}, "spock": {"scissor", "rock"}}

    print("player_choice: ", player_choice)
    print("computer_move: ", computer_move)

    is_mapping_present = computer_move in precedence_mapping[player_choice]

    if player_choice == computer_move:
        game_outcome = "tie"
    elif is_mapping_present:
        game_outcome = "win"
    else:
        game_outcome = "loose"

    fin_response = {"results": game_outcome, "player": player_choice, "computer": computer_move}
    return fin_response


# def get_move_from_id(id):
