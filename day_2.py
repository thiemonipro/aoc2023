from functools import reduce

p1_max_amounts = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def calculate_p1(games: list[str], max_amounts: dict):
    total = 0
    for line in games:
        game, draws = line.split(":")

        digits = []
        valid_run = True
        for index, character in enumerate(draws):
            if character.isdigit():
                digits.append(character)
            else:
                amount = "".join(digits)
                digits = []
                if not amount: continue

                for color, max_amount in max_amounts.items():
                    if draws[index + 1:].startswith(color):
                        if int(amount) > max_amount:
                            valid_run = False
        if valid_run:
            game_id = game.split(" ")[1]
            total += int(game_id)
    return total


def calculate_p2(games: list) -> int:
    total = 0
    for line in games:
        game, draws = line.split(":")

        max_amounts = {}
        digits = []
        for index, character in enumerate(draws):
            if character.isdigit():
                digits.append(character)
            else:
                amount = "".join(digits)
                digits = []
                if not amount: continue

                amount = int(amount)
                for color in ["red", "green", "blue"]:
                    if draws[index + 1:].startswith(color):
                        if amount > max_amounts.get(color, 0): max_amounts[color] = amount
        total += reduce((lambda x, y: x * y), max_amounts.values())
    return total


with open("data/day_2.txt") as file:
    games = file.readlines()

print(calculate_p1(games, p1_max_amounts))
print(calculate_p2(games))
