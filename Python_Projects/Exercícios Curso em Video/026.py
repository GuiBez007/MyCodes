# Write a code that reads a phrase and print how many 'a' has and when or where this 'a' is

phrase = input('Type a phrase here: ').strip()
print('This phrase has {} "a", where the first is in index {} and the last in index {}'\
      .format(phrase.count('a'), phrase.find('a'), phrase.rfind('a')))

input() #wait