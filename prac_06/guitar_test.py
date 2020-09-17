from prac_06.guitar import Guitar
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    current_age = CURRENT_YEAR - guitar.year
    another_guitar = Guitar("Another Guitar", 2013, 2000)
    another_current_age = CURRENT_YEAR - another_guitar.year

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, current_age, Guitar.get_age(guitar)))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, another_current_age,
                                                      Guitar.get_age(another_guitar)))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, Guitar.is_vintage(guitar)))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, False, Guitar.is_vintage(another_guitar)))


main()
