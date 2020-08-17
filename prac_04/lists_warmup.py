numbers = [3, 1, 4, 1, 5, 9, 2]

# returns the number 3. c
print(numbers[0])

# returns the number 2. c
print(numbers[-1])

# returns the number 1 in the 4th spot. c
print(numbers[3])

# returns the number 2.         A = [3, 1, 4, 1, 5, 9].
print(numbers[:-1])

# returns the number 1 in the 4th spot. c
print(numbers[3:4])

# returns Boolean True. c
print(5 in numbers)

# returns Boolean False. c
print(7 in numbers)

# returns Boolean False. c
print("3" in numbers)

# returns the list [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]. c
print(numbers + [6, 5, 3])

# first element to 'ten'.
numbers[0] = 'ten'

# last element to -1.
numbers[-1] = 1

# all except first two.
print(numbers[2:])

# check if 9 in numbers.
print(9 in numbers)
