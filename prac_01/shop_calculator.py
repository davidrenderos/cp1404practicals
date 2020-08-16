total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items!\nNumber of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price *= .9

print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
