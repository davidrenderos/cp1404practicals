"""
 fill it with at least 15 floats of any values between -200 and +200.
"""
import random
import csv

out_file = open("temps_input.txt", 'w')
out_file_writer = csv.writer(out_file)

number_of_scores = int(input("Enter number on scores: "))
for row in range(1, number_of_scores + 1):
    random_score = (random.uniform(-200, 200))
    out_file_writer.writerow("{}".format(random_score).split(', '))
out_file.close()
