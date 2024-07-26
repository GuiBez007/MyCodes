# Upgrade challenge 93 so that it works with multiple players, including a performance details
# visualization system for each player.

players = []

while True:
    player = {'name': input('PLAYER NAME [S to STOP]> ').strip()}
    if player['name'] in 'Ss':
        break
    player['played matches'] = int(input('PLAYED MATCHES> '))

    total_goals = []
    for i in range(player['played matches']):
        total_goals.append(int(input(f'Goals done in {i+1}°match> ')))
    player['goals'] = total_goals
    players.append(player)
    print()

while True:
    print('\n========== PLAYERS TABLE ==========')
    print(f'{'NUM':<3}  {'NAME':<10}  {'GOALS':<11}  {'TOTAL':>3}')

    for i in range(len(players)):
        print(f'{str(i+1):<3}  {players[i]['name']:<10}  {str(players[i]['goals']):<11}  {str(sum(players[i]['goals'])):>3}')
    option = int(input('Choice a player to see more information: '))

    for i in range(players[option-1]['played matches']):
        print(f'In the {i+1}° match did {players[option-1]['goals'][i]}')

input() #wait