# Write a program that reads the entire person's name and print: her name in upper, in lower, how many letters
# there are and how many letters in her first name

name = input('Type your name here: ').strip()
print('The informed name has {} letters in total \nThere are {} letters in the first name\nThe phrase in upper: {}\
      \nThe phrase in lower: {}'. format(len(name) - name.count(' '), len((name.split())[0]), name.upper(), name.lower()))

input() #wait