import os

do_conversion = True

word_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# First open the file
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]

    calibration_values = []

    for line in lines:
        first_char = ""
        last_char = ""
        first_pos = 1e10
        last_pos = 0

        for i, char in enumerate(line):
            if char.isdigit():
                first_char = char
                first_pos = i
                break

        for i, char in enumerate(line[::-1]):
            if char.isdigit():
                last_char = char
                last_pos = len(line) - i - 1
                break

        if do_conversion:
            for word in word_num.keys():
                if line.find(word) < first_pos and line.find(word) >= 0:
                    first_char = word_num[word]
                    first_pos = line.find(word)

            for word in word_num.keys():
                rfind = line.rfind(word)
                valid = rfind > last_pos and rfind >= 0
                if valid:
                    last_char = word_num[word]
                    last_pos = rfind

        # print(f"{line} => {first_char}{last_char}")

        calibration_values.append(int(f"{first_char}{last_char}"))

    print(sum(calibration_values))
