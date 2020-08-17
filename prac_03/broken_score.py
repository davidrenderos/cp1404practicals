"""
CP1404/CP5632 - Practical
Complete program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(result(score))


def result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


random_score = (random.randint(1, 100))
print(result(random_score))


main()
