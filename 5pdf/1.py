import random
odd_numbers = random.sample(range(1, 100, 2), 5)
even_numbers = random.sample(range(2, 100, 2), 4)
odd_numbers[2] = even_numbers
print("Modified list after replacing third element with even numbers:", odd_numbers)
flattened_list = []
for i in odd_numbers:
    if type(i)==list:
        for sub_item in i:
            flattened_list.append(sub_item)
    else:
        flattened_list.append(i)
print("Flattened list:", flattened_list)
flattened_list.sort()
print("Sorted list:", flattened_list)
