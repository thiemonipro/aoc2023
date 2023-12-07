adj = lambda x, y: (
    (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (x, y + 1), (x, y - 1))

def is_symbol(data: str) -> bool:
    return not data.isdigit() and data != "."


def calculate_p1(lines: list[str]) -> int:
    total = 0
    symbols = [(x, y) for x in range(len(lines[0])) for y in range(len(lines)) if is_symbol(lines[y][x])]

    for y, line in enumerate(lines):
        digits = []
        for x, character in enumerate(line):
            if character.isdigit():
                digits.append(character)

            if not character.isdigit() or x == len(line) - 1:
                number = "".join(digits)
                digits = []

                for i in range(len(number)):
                    n_x = x - i - 1
                    adj_cells = adj(n_x, y)
                    if any(cell in symbols for cell in adj_cells):
                        total += int(number)
                        break
    return total


def parse_lines_to_numbers(lines: list[str]) -> dict:
    numbers = {}
    for y, line in enumerate(lines):
        digits = []
        for x, character in enumerate(line):
            if character.isdigit():
                digits.append(character)

            if not character.isdigit() or x == len(line) - 1:
                number = "".join(digits)
                digits = []
                for i in range(len(number)):
                    curr_x = x - i
                    if x != len(line) - 1:
                        curr_x = curr_x - 1
                    numbers[(curr_x, y)] = int(number)
    return numbers


def calculate_p2(lines: list[str]) -> int:
    symbols = [(x, y) for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == "*"]
    numbers = parse_lines_to_numbers(lines)
    total = 0

    for x, y in symbols:
        gear_numbers = []

        for i in [-1, 0, 1]:
            curr_y = y + i
            mhs = numbers.get((x, curr_y), None)

            if mhs:
                gear_numbers.append(mhs)
            else:
                lhs = numbers.get((x - 1, curr_y), None)
                if lhs: gear_numbers.append(lhs)

                rhs = numbers.get((x + 1, curr_y), None)
                if rhs: gear_numbers.append(rhs)

        if len(gear_numbers) == 2:
            total += gear_numbers[0] * gear_numbers[1]

    return total


with open("data/day_3.txt") as file:
    puzzle_lines = [line.strip() for line in file.readlines()]

print(calculate_p1(puzzle_lines))
print(calculate_p2(puzzle_lines))
