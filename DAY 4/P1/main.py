import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]

    # Sample line:
    # Card   1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 123: 65 12  1  2 15 |  5  7  8  9 10 11 12 13 14 15

    sum_points = 0

    # Presumably we will need to iterate over each line
    for line in lines:
        # Get card number by removing "Card" and ":" and stripping whitespace
        card_number = int(line.split(":")[0].replace("Card", "").strip())

        # Get numbers we have
        numbers = []
        num_str = line.split(":")[1].split("|")[0].strip()

        for num in num_str.split(" "):
            if num != "":
                numbers.append(int(num))

        # Get winning numbers and strip leading space
        # For single digit values there is an extra space in the input
        winning_numbers = []
        winning_num_str = line.split(":")[1].split("|")[1].strip()
        for num in winning_num_str.split(" "):
            # Skip empty strings
            if num != "":
                winning_numbers.append(int(num))

        # Find number of winning numbers
        num_winning_numbers = 0
        for num in winning_numbers:
            if num in numbers:
                num_winning_numbers += 1

        # Calculate point value
        # The first match is one point, then each match after the first doubles the point value of the card
        # So, 4 matches would be 8 points
        if num_winning_numbers == 0:
            point_value = 0
        else:
            point_value = 2 ** (num_winning_numbers - 1)

        print(
            f"Card {card_number}: {num_winning_numbers} winning numbers making {point_value} points"
        )

        # Add to sum
        sum_points += point_value

    print(sum_points)
