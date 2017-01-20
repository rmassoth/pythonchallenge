import urllib.request
import re, http.cookiejar, bz2

number_array = []
number = 12345
bzip_string = ''
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
try:
    for i in range(1000):
        response = opener.open('http://pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(number))
        response_string = response.read()
        for x in cj:
            bzip_string = '{}{}'.format(bzip_string, x.value)
        match = re.search(r'busynothing is ([0-9]+)', str(response_string))
        number = match.group(1)

except:
    print("something happened!")
finally:
    bz2_string = urllib.parse.unquote_to_bytes(bzip_string.replace("+", " "))
    print(bz2_string)
    print(bz2.decompress(bz2_string))
