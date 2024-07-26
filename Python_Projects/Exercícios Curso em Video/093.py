# Write a program that manages the performance of a football player. The program will read the player's name and
# how many matches he played. After will read the goals' quantity done in each match. At the end, all of this will be
# kept in a dictionary, including the total of goals done in the championship.

player = {'name': input('PLAYER NAME> '),
          'played matches': int(input('PLAYED MATCHES> '))}

total_goals = []
for i in range(player['played matches']):
    total_goals.append(int(input(f'Goals done in {i+1}°match> ')))
player['goals'] = total_goals

print('\n===== PLAYER TABLE =====')
for k, v in player.items():
    print(f'{k}: {v}')
print()
for i in range(player['played matches']):
    print(f'In the {i+1}° match did {player['goals'][i]}')

input() #wait