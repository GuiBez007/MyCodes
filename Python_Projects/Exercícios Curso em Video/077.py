# Create a tuple with various words and show for each word what's its vowel.

vowels = ('a', 'e', 'i', 'o', 'u')
words = (
        "LEARNING",
        "PROGRAMING",
        "LANGUAGE",
        "PYTHON",
        "COURSE",
        "FREE",
        "STUDY",
        "PRACTICE",
        "WORK",
        "SHOP",
        "PROGRAMMER",
        "FUTURE"
        )

for word in words:
        print(f'In {word} has vowels ', end='')
        for letter in word:
                if letter.lower() in vowels:
                        print(f'{letter.lower()} ', end='')
        print()

input() #wait