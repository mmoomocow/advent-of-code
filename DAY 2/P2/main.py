import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]

    powers = []

    for game in lines:
        # Split the game ID from the data
        game_id, data = game.split(":")
        # Remove the "Game " from the game ID
        game_id = game_id[5:]

        # Split the data into the different draws
        draws = data.split(";")

        # Minimum number of each color
        min_red, min_green, min_blue = 0, 0, 0

        for draw in draws:

            results = draw.split(",")

            red, green, blue = 0, 0, 0

            for result in results:

                word = result.split()[-1]

                if word == "red":
                    red += int(result.split()[0])

                    if red > min_red:
                        min_red = red
                elif word == "green":
                    green += int(result.split()[0])

                    if green > min_green:
                        min_green = green
                elif word == "blue":
                    blue += int(result.split()[0])

                    if blue > min_blue:
                        min_blue = blue
            

        # Calculate the special power value
        power = min_red * min_green * min_blue
        powers.append(power)

        print(f"Game {game_id}: {min_red} red, {min_green} green, {min_blue} blue => {power}")


    print(f"Power sum is: {sum(powers)}")