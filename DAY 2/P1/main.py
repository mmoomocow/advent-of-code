import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    lines = [line.strip() for line in lines]

    # Sample line: 
    # Game 1: 1 blue, 8 green; 14 green, 15 blue; 3 green, 9 blue; 8 green, 8 blue, 1 red; 1 red, 9 green, 10 blue

    # List of valid game IDs to be filtered later. IDs are 1 - 100
    # List begins filled with all possible IDs
    valid_games = [i for i in range(1, len(lines) + 1)]


    for game in lines:
        invalid_game = False
        # Split the game ID from the data
        game_id, data = game.split(":")
        # Remove the "Game " from the game ID
        game_id = game_id[5:]

        # If the game is already invalid, don't bother checking the rest of the draws
        if int(game_id) not in valid_games:
            continue

        # Split the data into the different draws
        draws = data.split(";")

        for draw in draws:

            # If the game is already invalid, don't bother checking the rest of the draws
            if int(game_id) not in valid_games:
                break

            results = draw.split(",")

            red, green, blue = 0, 0, 0

            for result in results:

                # Get the last word in the result
                word = result.split()[-1]

                if word == "red":
                    red += int(result.split()[0])
                elif word == "green":
                    green += int(result.split()[0])
                elif word == "blue":
                    blue += int(result.split()[0])
            
            # Red invalid if > 12
            # Green invalid if > 13
            # Blue invalid if > 14
            # Total invalid if > 39

            red_invalid = red > 12
            green_invalid = green > 13
            blue_invalid = blue > 14
            total_invalid = red + green + blue > 39
            draw_invalid = red_invalid or green_invalid or blue_invalid or total_invalid

            if draw_invalid:
                # This game is invalid
                invalid_game = True
                if int(game_id) in valid_games:
                    valid_games.remove(int(game_id))
                break
            # Print game, draw and results
            print(f"Game: {game_id} invalid? {invalid_game}       Results: {red} red, {green} green, {blue} blue")

    print(f"Found {len(valid_games)} valid games.")
    print(valid_games)
    print(f"Sum of valid games is {sum(valid_games)}")


