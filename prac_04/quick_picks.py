import random


def main():
    list_of_numbers = []

    number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        sub_list_of_numbers = []
        for j in range(5):
            sub_list_of_numbers.append(random.randint(1, 45))
        list_of_numbers.append(sub_list_of_numbers)
    print(sorted(list_of_numbers))


main()
