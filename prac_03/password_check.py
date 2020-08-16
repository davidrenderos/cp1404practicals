def main():

	min_length, password = get_password()
	while len(password) < min_length:
		print("Password not long enough")
		password = input("Enter password: ")
	else:
		print_password(password)


def print_password(password):
	for _ in password:
		print("*", end='')


def get_password():
	min_length = 6
	password = input("Enter password: ")
	return min_length, password


main()
