"""
# Exercise 11: Remove empty strings from the list of strings
list1 = ["Mike","","Emma","","Kelly","Brad"]

result = list(filter(None,list1))
print(result)

# Exercise 12: Remove Duplicates from list
list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

unique_elements_set = set(list_with_duplicates)
unique_list = list(unique_elements_set)
print(f"Original list: {list_with_duplicates}")
print(f"List with unique elements: {unique_list}")

# Exercise 14: List Comprehension for Numbers
""" 
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

numbers_list = [number for number in my_list if (isinstance(number,int))]
print(numbers_list)