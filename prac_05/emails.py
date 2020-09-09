def main():
    get_email()


def get_email():
    emails = {}
    email = input("Email: ")
    get_name(email)
    while email != "":
        email = input("Email: ")
        get_name(email)


def get_name(email):
    choice = input("Is your name ? (y/n) ").lower()
    if choice == "y":
        return email
    else:
        name = input("Name: ")


main()
