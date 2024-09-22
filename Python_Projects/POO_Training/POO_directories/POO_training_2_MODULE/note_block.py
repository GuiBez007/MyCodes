def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        a = open(name, 'wt+')
    else:
        count = 0
        for line in a:
            count += 1
            if 'guilherme' in line:
                print(count)
    finally:
        a.close()


def writeFile(name):
    try:
        a = open(name, 'wt')
    except:
        print('ERROR!')
    finally:
        a.close()