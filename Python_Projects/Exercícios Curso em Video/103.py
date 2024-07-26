# Write a program that has a function called token(), that receives two optional parameters: the player name and how
# many goals he got. The program must be able to show player token, even that some data didn't have be informed correctly.

def token(name=' ', goals=' '):
    if len(name) < 3:
        name = '<unknown>'
    if not goals.isnumeric():
        goals = 0
    return f'The player {name} did {goals} goals in this game!'


# main()
name = input('Type your name> ').strip()
goals = input('Inform how many goals you did> ').strip()
print(token(name, goals))

input() #wait