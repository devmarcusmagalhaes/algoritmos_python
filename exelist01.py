# Exercise 1: Perform Basic List Operations
my_list = [10, 20, 30, 40, 50]

print(my_list)
print(f"Third item: {my_list[2]}")
print(f"Length of t he list: {len(my_list)}")

# Exercise 2: Perform List Manipulation
print(f"Initial list: {my_list}")
my_list[1] = 200
print(f"After changing second element: {my_list}")
my_list.append(600)
print(f"List after appending 600: {my_list}")
my_list.insert(2,300)
print(f"List after inserting 300 at index 2:{my_list}")
my_list.remove(600)
print(f"List after removing 600 (by value): {my_list}")
del my_list[0]
print(f"List after removing element at index 0: {my_list}")

# Exercise 3: Sum and average of all numbers in a list
sum = 0
for x in my_list:
    sum += x
print(f"Sum: {sum}")
average = sum / len(my_list)
print(f"Average: {average}")

# Exercise 4: Reverse a list
list1 = [100,200,300,400,500]
list1.reverse()
print(list1)

# Exercise 5: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
result = []

for number in numbers:
    result.append(number * number)
print(result)

# Exercise 6: Find Maximum and Minimum
data = [8, 2, 15, 1, 9]
largest = max(data)
smallest = min(data)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

# Exercise 7: Count Occurrences
sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
football_count = sports.count('Football')
print(f"Count: {football_count}")

# Exercise 8: Sort a list of numbers
numbers = [5, 2, 8, 1, 9]
print(f"Original list: {numbers}")
numbers.sort()
print(f"Sorted list: {numbers}")

# Exercise 9: Create a copy of a list
list1 = [10,20,30]
list2 = list1.copy() # ou list1[:]
list1.append(40)
print(list1)
print(list2)

# Exercise 10: Combine two lists
list_a = [1, 2]
list_b = [3, 4]

list_plus = list_a + list_b
print(f"{list_plus}")

temp_list = [1,2]
temp_list.extend(list_b)
print(f"{temp_list}")

unpacking_list = [*list_a,*list_b]
print(f"{unpacking_list}")

