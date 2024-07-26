#Write a program that reads an anglo and print his seno, cosseno and tangent

from math import sin, cos, tan, radians
##I needed to import radians to use these mathematic functions

anglo = float(input('Type a anglo: '))
print('His seno is {:.2f}, cosseno {:.2f} and tangent is {:.2f}'\
      .format(sin(radians(anglo)), cos(radians(anglo)), tan(radians(anglo))))

input() #wait
