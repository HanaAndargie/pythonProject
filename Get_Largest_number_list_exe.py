#Gets Largest Number in list

numbers = [4,3,9,7,6]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

#Get Smallest Number in list
numbers = [4,3,9,7,6,-1]
small_number = numbers[0]
for number in numbers:
    if number < small_number:
        small_number = number
print(small_number)

