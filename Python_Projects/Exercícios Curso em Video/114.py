# Create a code that tests if the website pudim is accessible or not.

import urllib.request
try:
    website = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('The website is INACCESSIBLE!')
else:
    print('The website is ACCESSIBLE!')

input() #wait