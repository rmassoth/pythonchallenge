import re
import zipfile

my_zipfile = zipfile.ZipFile('channel.zip')

comments = []
number = 90052

while number:
    filename = '{}.txt'.format(number)
    contents = my_zipfile.read(filename)
    comment = my_zipfile.getinfo(filename)
    comments.append(comment.comment.decode("utf-8"))
    number_search = re.search(r'[^nothing is ][0-9]+', contents.decode('utf-8'))

    if number_search:
        number = number_search.group(0)
    else:
        number = None
        print(''.join(comments))