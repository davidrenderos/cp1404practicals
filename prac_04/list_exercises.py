usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []
count = 1
number = int(input("Number {}: ".format(count)))
numbers.append(number)
while number > 0:
    count += 1
    number = int(input("Number {}: ".format(count)))
    numbers.append(number)
else:
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
