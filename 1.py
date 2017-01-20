my_string = "map"
my_trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(my_string.translate(my_trans))