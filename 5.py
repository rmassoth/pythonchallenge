from urllib.request import urlopen
import pickle

response = urlopen('http://pythonchallenge.com/pc/def/banner.p')
# data = pickle.load(open("banner.p", "rb"))
data = pickle.load(response)
for string in data:
    print(''.join([e[0] * e[1] for e in string]))