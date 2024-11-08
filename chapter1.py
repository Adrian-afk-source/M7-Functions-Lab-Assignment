# Adrian Garcia
# 11/5/24
# This code picks a random greeting or if it's anoid then it'll say a bad message to the user.



import random

def say_my_name(name):
    

    if random.choice([True, False]):
        print(f"Hello, {name}! It's nice to see you.")
    else:
        print(f"What do you want, {name}?!")

say_my_name("Adrian") 

# Problem 3

import random

def lets_see(number):
    return 10 <= number <= 50

def multiply_if():
    numbers = [random.randint(1, 100) for _ in range(10)]
    updated_numbers = [
        num * 5 if lets_see(num) else num
        for num in numbers
    ]
    
    return updated_numbers

#Problem 4

def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element) 

unique_list.sort()

return unique_list

test_list = [1, 3, 3, 3, 6, 2, 3, 5]
print(unique_elements(test_list))