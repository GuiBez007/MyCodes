# I can make a dictionary if I want to organize the colors in names
c = '\033['
for i in range(9):
    print('{}3{}mHello!{}m'.format(c, i, c), end='')
    print(' {}30;4{}m!olleH{}m'.format(c, i, c))

# Format> \033[m     ->    \033[<num;num;num>m

# \033[ {(0/1/4/7); (30/31/32/33...); (40/41/42/43...)} m
#          font          color           background