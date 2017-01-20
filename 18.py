from PIL import Image, ImageChops, ImageStat
import re

delta_file = open("deltas", "rb")
# img1 = open("deltas.png", "wb")
# img2 = open("deltas2.png", "wb")
my_string = ''

with open("deltas", "r") as delta_file:
    for line in delta_file:
        # img1.write(bytes.fromhex(line[:54]))
        line_bytes = str(bytes.fromhex(line[:54]))
        # img2.write(bytes.fromhex(line[56:-1]))
        match = re.findall(r'([A-Z]+)', line_bytes)
        print(match)
        if match:
            match_string = ''.join()
            my_string = '{}{}'.format(my_string, match)
print(my_string)

# img1.close()
# img2.close()

# img1 = Image.open("test.png")
# img1.show()
# img2 = Image.open("deltas2.png")
