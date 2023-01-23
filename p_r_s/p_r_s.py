import random


def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors: )')
    game_options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(game_options)
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices
