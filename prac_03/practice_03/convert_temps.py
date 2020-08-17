import random


def main():
    in_file = open("temps_input.txt", 'r')
    out_file = open("temps_output.txt", 'w')
    for row in in_file:
        result = fahrenheit_to_celsius(float(row))
        print(result, file=out_file)
    in_file.close()
    out_file.close()


def create_input():
    out_file = open("temps_input.txt", 'w')
    for row in range(15):
        temperature = (random.uniform(-200, 200))
        print(temperature, file=out_file)
    out_file.close()


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
