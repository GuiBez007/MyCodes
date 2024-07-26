# Write a code that reads the name, age and sex of 4 people. At the end, show:
# the average age of the group, what's the name of the oldest man and how many women has under 20 years old.

n = 4
_sum = 0
oldest_age = 0
young_women = 0

for i in range(n):
    print('----- {}°PERSON -----'.format(i+1))
    name = input('Name: '.format(i+1))
    age = int(input('Age: '))
    sex = input('Sex [M/F]: ')
    print()

    _sum += age

    if sex in 'Mm':
        if age > oldest_age:
            oldest_age = age
            oldest_man = name

    elif sex in 'Ff':
        if age < 20:
            young_women += 1

print('The average age of group is {:.2f}, \n'
      'the oldest man\'s name is {} being his age {} and\n'
      'there are in total {} women under 20 years old!'.format(_sum/n, oldest_man, oldest_age, young_women))

input() #wait
