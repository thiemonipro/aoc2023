def calculate(data: list[str], day_2: bool) -> int:
    total = 0

    for line in data:
        digits = []
        for index, character in enumerate(line):
            if character.isdigit():
                digits.append(character)
                continue
            if day_2:
                for value, name in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
                                             start=1):
                    if line[index:].startswith(name):
                        digits.append(str(value))
        total += int(digits[0] + digits[-1])
    return total


with open("data/day_1.txt") as file:
    puzzle_lines = file.readlines()

print(f"day 1: p1 = {calculate(puzzle_lines, day_2=False)}")
print(f"day 1: p2 = {calculate(puzzle_lines, day_2=True)}")
