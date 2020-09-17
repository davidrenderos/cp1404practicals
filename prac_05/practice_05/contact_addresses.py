def main():
    MENU = "(A)dd\n(C)hange\n(P)rint\n(Q)uit "
    friends_addresses = {}
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            name = input("Name: ")
            address = input("Address: ")
            friends_addresses[name] = address
        elif choice == "C":
            pass
        elif choice == "P":
            print(friends_addresses)
        else:
            print("???")
        print(MENU)
        choice = input(">>> ").upper()
    print("Cyah!")


main()
