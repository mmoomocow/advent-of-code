import os


# First open the file
with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]

    sum_calibrations = 0

    # print(lines)

    for line in lines:
        # Create a list of all the characters in the line
        chars = list(line)

        # Remove the non-int characters
        chars = [char for char in chars if char.isdigit()]

        # Switch case. Len = 0, len = 1, len > 1
        if len(chars) == 0:
            pass
        elif len(chars) == 1:
            calibration_value = f"{chars[0]}{chars[0]}"
            sum_calibrations += int(calibration_value)

        else:
            calibration_value = f"{chars[0]}{chars[-1]}"
            sum_calibrations += int(calibration_value)

    print(sum_calibrations)
