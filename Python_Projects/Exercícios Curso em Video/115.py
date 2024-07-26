# We're going to see how we can access our archives from pc.

from usefulCeV.ex115.interface import *
from usefulCeV.ex115.archive import *

file = 'registeredPeople.txt'
if fileExist(file):
    print('File exists!')
else: createFile(file)

while True:
    mold('MAIN MENU')
    options()
    verification()

input() #wait