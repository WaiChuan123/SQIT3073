# Create a set
fruits = {"apple", "banana", "cherry", "date"}

# Add an element to the set
fruits.add("grape")

# Remove an element from the set
fruits.remove("cherry")

# Check if an element is in the set
contains_banana = "banana" in fruits
contains_orange = "orange" in fruits

# Iterate through the set
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Create another set
citrus_fruits = {"orange", "lemon", "lime"}

# Perform set operations
union_fruits_citrus = fruits.union(citrus_fruits)  # combines all unique elements from both sets
intersection_fruits_citrus = fruits.intersection(citrus_fruits)  # gets common elements between sets
difference_fruits_citrus = fruits.difference(citrus_fruits)  # gets elements in 'fruits' but not in 'citrus_fruits'

# Print the results
print("Contains 'banana'? ", contains_banana)
print("Contains 'orange'? ", contains_orange)
print("Union of fruits and citrus fruits:", union_fruits_citrus)
print("Intersection of fruits and citrus fruits:", intersection_fruits_citrus)
print("Difference between fruits and citrus fruits:", difference_fruits_citrus)

# Adding elements using update method
fruits.update(["pear", "melon"])
print("Fruits after update:", fruits)

# Removing elements using discard method
fruits.discard("apple")
print("Fruits after discarding 'apple':", fruits)

# Clearing the set
fruits.clear()
print("Fruits after clearing:", fruits)
