import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        list_of_numbers = []
        for j in range(NUMBERS_PER_LINE):
            number = (random.randint(MINIMUM, MAXIMUM))
            list_of_numbers.append(number)
        print(list_of_numbers)


main()
