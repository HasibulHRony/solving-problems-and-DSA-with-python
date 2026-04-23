#suppose there is a list of some number values. Find the maximum value from it.

#solution:
numbers = [88, 73, 55, 64, 92, 78, 88]

max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print("The maximum number of this list is: ", max_number)