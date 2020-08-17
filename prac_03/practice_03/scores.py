"""
CP1404/CP5632 - Practical
Complete program to determine score status
"""
import random


def main():
    number_of_scores = int(input("Enter number on scores: "))
    for i in range(1, number_of_scores + 1):
        random_score = (random.randint(1, 100))
        print("{} is {}".format(random_score, result(random_score)))


def result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
