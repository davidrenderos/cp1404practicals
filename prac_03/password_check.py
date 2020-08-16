MIN_LENGTH = 6

password = input("Enter password: ")
while len(password) < MIN_LENGTH:
	print("Password not long enough")
	password = input("Enter password: ")
else:
	for char in password:
		print("*", end='')
