with open('input.txt', 'r') as input_file:
    input_txt = input_file.read()


def game_round_value(opponent_move, player_move):
    o = opponent_move_value(opponent_move)
    p = player_move_value(player_move)
    if o == p:
        return 3
    if (o == 1 and p == 2) or (o == 2 and p == 3) or (o == 3 and p == 1):
        return 6
    return 0


def opponent_move_value(opponent_move):
    if opponent_move == 'A':
        return 1
    if opponent_move == 'B':
        return 2
    return 3


def player_move_value(player_move):
    if player_move == 'X':
        return 1
    if player_move == 'Y':
        return 2
    return 3


game_total = 0

for game_round in input_txt.split('\n'):
    if game_round:
        opponent_move, player_move = game_round.split(' ')
        round_value = player_move_value(player_move) + game_round_value(opponent_move, player_move)
        game_total += round_value

    
print('What would your total score be if everything goes exactly according to your strategy guide?')
print(f'The total score is {game_total}')


def game_round_value(opponent_move, round_outcome):
    o = opponent_move_value(opponent_move)
    if round_outcome == 'Y':
        return o + 3
    if round_outcome == 'Z':
        if o == 1:
            return 2 + 6
        if o == 2:
            return 3 + 6
        if o == 3:
            return 1 + 6
    if round_outcome == 'X':
        if o == 1:
            return 3
        if o == 2:
            return 1
        if o == 3:
            return 2


game_total = 0

for game_round in input_txt.split('\n'):
    if game_round:
        opponent_move, round_outcome = game_round.split(' ')
        game_total += game_round_value(opponent_move, round_outcome)


print('Following the Elf\'s instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?')
print(f'The total score is {game_total}')
