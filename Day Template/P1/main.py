import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]


    # Presumably we will need to iterate over each line
    for game in lines:
        print("I'm a template!")