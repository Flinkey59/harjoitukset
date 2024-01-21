import random

players = []

for a in range(8):
    user_input = input(f'Please provide player #{a+1}: ')
    players.append(user_input)

print('-------------')

for b in range(4):
    print(f'Team {b+1}: ')

    for c in range(2):
        d = random.choice(players)
        print(f'{d}')
        players.remove(d)

    print('-------------')