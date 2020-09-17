from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars_to_add = Guitar(name, year, cost)
        guitars.append(guitars_to_add)
        print(guitars_to_add, "added.")
        name = input("Name: ")
    guitars.sort()
    print("These are my Guitars!")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".
              format(i + 1, guitar, vintage_string))


main()