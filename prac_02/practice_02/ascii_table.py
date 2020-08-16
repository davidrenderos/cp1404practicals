LOWER = 33
UPPER = 127

char = input("Enter a Character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between {} and {}: ").format(LOWER, UPPER))
while number < LOWER or number > UPPER:
    print("Number must be higher than {} and lower than {}".format(LOWER, UPPER))
    number = int(input("Enter a number between {} and {}: ").format(LOWER, UPPER))
print("The character for {} is {}".format(number, chr(number)))

for i in range(LOWER, UPPER + 1):
    print("{:>3}  {}".format(i, chr(i)))

columns = int(input("How many columns do you want to print?"))





