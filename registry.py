capitals = {
    'United States': 'Washington D.C.',
    'China': 'Beijing',
    'France': 'Paris',
    'United Kingdom': 'London',
    'Germany': 'Berlin',
    'Russia': 'Moscow',
    'Finland': 'Helsinki',
    'Portugal': 'Lisbon',
    'Spain': 'Madrid',
    'Italy': 'Rome',
}

while True: 
    print('Provide the name of one of the following nations: ')
    for nation_and_capital in capitals:
        print(f'{nation_and_capital}, {capitals[nation_and_capital]}')
    user_input = input('------------------\n: ')
    if user_input not in capitals:
        print('Provided country is not listed, try again')
    else:
        new_capital = input('Provide a new name for the capital: ')
        capitals[user_input] = new_capital
        
        break
print(f'The new capital of {user_input} is now {capitals[user_input]}')