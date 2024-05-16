# Create a tuple
fruits = ("apple", "banana", "cherry", "date", "melon", "durian")


# Access elements by index
first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[5]

# Iterate through the tuple
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Check if an element is in the tuple
contains_cherry = "cherry" in fruits

# Find the length of the tuple
num_fruits = len(fruits)

# Concatenate two tuples
more_fruits = ("grape", "kiwi")
all_fruits = fruits + more_fruits

# Nested tuple
nested_tuple = ("red", ("green", "blue"))

# Print the results
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Last fruit:", last_fruit)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of fruits:", num_fruits)
print("All fruits:", all_fruits)
print("Nested tuple:", nested_tuple)

# Accessing elements in a nested tuple
nested_color = nested_tuple[1][0]
print("Nested color:", nested_color)

# Creating a tuple from a list
colors_list = ["red", "green", "blue"]
colors_tuple = tuple(colors_list)
print("Tuple from list:", colors_tuple)
