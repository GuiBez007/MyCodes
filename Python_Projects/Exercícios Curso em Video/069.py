# Write a code that reads the age and sex of various people. For each person registered, the program will must
# ask if user wants to continue or not. At the end, show:
# - How many people has more than 18 years old
# - How many men was registered
# - How many women has under 20 years old

count = 1
men = women_u20 = adults = 0
print('===== REGISTER =====')
while True:
    print('PERSON {}: '.format(count))
    age = int(input('Age: '))
    sex = input('Sex[M/F]:').strip().upper()

    if sex == 'M':
        men += 1
    elif sex == 'F' and age < 20:
        women_u20 += 1
    if age > 18:
        adults += 1

    option = input('To continue[Y/N]: ').strip().upper()
    if option == 'N':
        break
    print()
    count += 1

print('There are {} adults in this group where {} are men and {} are women under 20 years old.'\
      .format(adults, men, women_u20))

input() #wait