from urllib.request import urlopen
import re

number_array = []
number = 32278
try:
    for i in range(400):
        response = urlopen('http://pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(number))
        response_string = response.read()
        match = re.search(r'[0-9]+', str(response_string))
        number = match.group()
        number_array.append(match.group())
except:
    pass
finally:
    print(number_array)
    print(response_string)
