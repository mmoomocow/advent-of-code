import os


grid = []


def is_symbol(char):
    return (not char.isdigit()) and char != "."


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    # Now read the file
    lines = f.readlines()
    # And strip the newline characters (\n)
    grid = [line.strip() for line in lines]


offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1, 0),  (1, 1)
]

def test_offsets(x, y):
    for offset_x, offset_y in offsets:
        new_x, new_y = x + offset_x, y + offset_y
        char = ""
        try:
            char = grid[new_y][new_x]
        except IndexError:
            continue

        if is_symbol(grid[new_y][new_x]):
            return True
    else:
        return False


part_numbers = []


for y in range(len(grid)):
    x = 0
    while x < len(grid[y]):
        if not grid[y][x].isdigit():
            x += 1
            continue

        x2 = x + 1

        # Find the end of the number

        while x2 < len(grid[y]) and grid[y][x2].isdigit():
            x2 +=1
        # x2 is now at the end of the number

        # Test offsets of each position - if any are symbols, then it's a part number
        for x3 in range(x, x2):
            if test_offsets(x3, y):
                part_number = "".join(grid[y][x:x2])
                part_numbers.append(part_number)
                # print(f"Found part number {part_number} at {x + 1}, {y + 1} to {x2 + 1}, {y + 1}")
                break
        x = x2

print(sum(int(part_number) for part_number in part_numbers))