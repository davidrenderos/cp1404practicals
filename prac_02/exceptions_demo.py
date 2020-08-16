"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator needs to be a whole value!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

# When will a ValueError occur?
# A: This will occur when a valid integer is not entered.

# When will a ZeroDivisionError occur?
# A: This will occur when the denominator is 0.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# A: Completed by using a for loop to only accept numbers other than 0.
