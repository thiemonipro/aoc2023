def score_card(wins: int):
    if wins == 0:
        return 0
    else:
        return 1 * pow(2, wins - 1)

# TODO: we could try to modify the code and adding caching here to speed up the scoring
def count_card_creation(card_winnings, number):
    total = 0
    created_cards = card_winnings.get(number, [])
    total += len(created_cards)
    for card in created_cards:
        total += count_card_creation(card_winnings, card)
    return total


def calculate_p1(cards: list[str]) -> int:
    total = 0
    for card in cards:
        game = card.split(":")[1]
        numbers, winning_numbers = game.split("|")
        numbers = set(number for number in numbers.split(" ") if number.isdigit())
        winning_numbers = set(number for number in winning_numbers.split(" ") if number.isdigit())
        your_winning_numbers = numbers.intersection(winning_numbers)
        score = score_card(len(your_winning_numbers))
        total += score

    return total


# TODO: smells like recursion
def calculate_p2(cards: list[str]) -> int:
    total = 0
    card_winnings = {}
    for index, card in enumerate(cards):
        game = card.split(":")[1]
        numbers, winning_numbers = game.split("|")
        numbers = set(number for number in numbers.split(" ") if number.isdigit())
        winning_numbers = set(number for number in winning_numbers.split(" ") if number.isdigit())
        your_winning_numbers = numbers.intersection(winning_numbers)
        card_winnings[index] = [index + i + 1 for i in range(len(your_winning_numbers))]

    for number in card_winnings.keys():
        total += count_card_creation(card_winnings, number)

    return total + len(cards)


with open("data/day_4.txt") as file:
    cards = [line.strip() for line in file.readlines()]

print(calculate_p1(cards))
print(calculate_p2(cards))
