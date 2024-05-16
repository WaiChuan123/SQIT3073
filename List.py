# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the list
print("Original list:", numbers)

# Access elements by index
second_element = numbers[1]
print("The second element is:", second_element)

# Slice the list to get a subset
subset = numbers[3:5]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[2] = 10
print("Modified list:", numbers)

# Append an element to the end of the list
numbers.append(6)
print("List after appending 6:", numbers)

# Remove an element by value
numbers.remove(2)
print("List after removing 2:", numbers)

# Find the index of an element
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

# Check if an element is in the list
contains_7 = 7 in numbers
print("Does the list contain 7?", contains_7)

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

# Create a list of strings
fruits = ["apple", "banana", "cherry", "durian"]

# Print the second element of the fruits list
print("Second fruit in the list:", fruits[1])

# Extend the fruits list with another list
more_fruits = ["grape", "kiwi"]
fruits.extend(more_fruits)
print("Extended fruits list:", fruits)

# Insert an element at a specific index
fruits.insert(2, "orange")
print("Fruits list after insertion:", fruits)

# Remove the last element from the list
last_fruit = fruits.pop()
print("Removed last fruit:", last_fruit)
print("Updated fruits list after popping:", fruits)
