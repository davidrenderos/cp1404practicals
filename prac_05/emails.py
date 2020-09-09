def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input("Is your name {}? (y/n) ".format(name))
        if choice.lower() != "y":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")


def get_name(email):
    rid_symbol = email.split('@')[0]
    name_parts = rid_symbol.split('.')
    name = " ".join(name_parts).title()
    return name


main()