from PIL import Image, ImageChops, ImageStat
import re
from time import sleep
from io import BytesIO
import binascii

# # gets the lines that are different between right and left
# with open("deltas", "r") as delta_file, open("deltas_missing.txt", "w") as deltas_file:
#     lines = delta_file.readlines()
#     last_line = 0
#     for current_line in lines:
#         for check_line in range(last_line, len(lines)):
#             if current_line[56:109] == lines[check_line][:53]:
#                 deltas_file.write(str(check_line))
#                 deltas_file.write('\n')
#                 last_line = check_line + 1
#                 break


# with open("deltas.txt", "r") as delta_file, open("deltas", "r") as delta, open("hidden.png", "wb") as hidden_file:
#     lines = delta_file.readlines()
#     img_lines = delta.readlines()
#     last_line = 0
#     for line in lines:
#          hidden_file.write(bytes.fromhex(img_lines[int(line)][:53]))

with open("real_deltas.txt", "r") as delta_file, open("deltas", "r") as delta, open("real_real_deltas.txt", "w") as hidden_file:
    lines = delta_file.readlines()
    img_lines = delta.readlines()
    last_line = 0
    skips = 0
    count = 1
    for line in lines:
        if line[0] != '1':
            skips += 1
            hidden_file.write(str(count))
            hidden_file.write('\n')

        else:
            skips += 1
        count+=1




# my_string = ''
# chunk_type = b'\x00\x00\x00\x00'

# with open("deltas2_middle.png", "rb") as delta_file, open("out.png", "wb") as out:
#     header = delta_file.read(8)
#     out.write(header)
#     while chunk_type != b'IEND':
#         chunk_size = delta_file.read(4)
#         chunk_size_int = int.from_bytes(chunk_size, byteorder='big', signed=False)
#         chunk_type = delta_file.read(4)
#         content = delta_file.read(chunk_size_int)
#         crc = delta_file.read(4)
#         new_crc = binascii.crc32(chunk_type+content).to_bytes(4, byteorder='big')
#         print("chunk size:", chunk_size_int)
#         print("chunk type:", chunk_type)
#         print("chunk crc:", new_crc)
#         sleep(1)
#         out.write(chunk_size)
#         out.write(chunk_type)
#         out.write(content)
#         out.write(new_crc)


# with open("deltas2.png", "rb") as delta_file:
#     my_string = delta_file.read()
#     my_chunk = re.findall(b'([A-Z][A-Z][A-Z][a-zA-Z])', my_string)
#     print(my_chunk)


# img1.close()
# img2.close()

# img1 = Image.open("test.png")
# img1.show()
# img2 = Image.open("deltas2.png")
