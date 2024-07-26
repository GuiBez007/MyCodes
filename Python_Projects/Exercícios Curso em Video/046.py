# Write a code that shows in the screen a descend count for a BOOM of fireworks, going 10 to 0 with a pause of 1 sec

from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
    if i == 1:
        print('BOOM!')

input() #wait