"""
CP1404/CP5632 - Practical
Complete program to determine score status
"""
import random
import csv


def main():

    out_file = open("results.txt", 'w')
    out_file_writer = csv.writer(out_file)

    number_of_scores = int(input("Enter number on scores: "))
    for row in range(1, number_of_scores + 1):
        random_score = (random.randint(1, 100))
        # print("{} is {}".format(random_score, result(random_score), file=out_file))
        # print("{} is {}".format(random_score, result(random_score)))
        out_file_writer.writerow("{} is {}".format(random_score, result(random_score)).split(', '))
    out_file.close()


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
