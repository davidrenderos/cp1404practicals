def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input("Is your name {}? (y/n) ".format(name))
        if choice == "y":
            email = input("Email: ")
        else:
            name = input("Name: ")

def get_name(email):
    name = email
    return name


main()