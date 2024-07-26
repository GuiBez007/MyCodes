# Write a program that has a function named vote() that will receive as parameter the born year of a person,
# returning a literal value indicating if the person has the vote DENIED, OPTIONAL or MANDATORY in elections.

def vote(year):
    from datetime import date
    global result
    result = date.today().year - year
    return result


# main()
born_year = int(input('Inform your born year> '))
result = 0

if vote(born_year) > 17:
    print(f'With {result} your vote is\033[31m MANDATORY!')
elif vote(born_year) > 15:
    print(f'With {result} your vote is\033[33m OPTIONAL!')
else: print(f'With {result} your vote is\033[32m DENIED!')

input() #wait