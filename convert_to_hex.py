

with open("deltas", "r") as delta:
    for line in delta:
        print(line.to_hex())