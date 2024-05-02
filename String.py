# Define a string variable
message = "Hello World."

# Print the string
print(message)

# Access individual characters in the string
second_character = message[1]
print("The second character is:", second_character)

# Find the length of the string
length = len(message)
print("The length of the string is:", length)



#
# Get user input for their favorite food
favorite_food = input("What's your favorite food? ")
#
#



# Concatenate (combine) two strings
custom_greeting = "Hello! I hope you enjoy " + favorite_food + " today!"
print(custom_greeting)

# Use string methods
uppercase_message = custom_greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_world = "World" in custom_greeting
print("Does the message contain 'World'? ", contains_world)

# Replace part of the string
new_message = message.replace("World", favorite_food)
print("Updated message:", new_message)

# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my