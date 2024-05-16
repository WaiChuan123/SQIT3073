# Create a dictionary of student information
student = {
    "name": "Carmen",
    "age": int(23),
    "major": "Computer Science",
    "grades": {
        "math": 95,
        "english": 88,
        "history": 92
    }
}

# Access dictionary values by keys
student_name = student["name"]
student_age = student["age"]

# Modify dictionary values
student["age"] = 21
student["grades"]["math"] = 97

# Add a new key-value pair
student["gender"] = "Female"

# Check if a key exists in the dictionary
has_major = "major" in student
has_height = "height" in student

# Get the list of keys and values
keys = list(student.keys()) 
values = list(student.values()) 

# Iterate through the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key-value pair using pop
removed_grades = student.pop("grades")

# Print the updated dictionary
print("\nStudent Information after removing 'grades':")
for key, value in student.items():
    print(f"{key}: {value}")

# Update the dictionary with a new set of grades
new_grades = {"physics": 90, "chemistry": 85,}
student["grades"] = new_grades

# Print the dictionary after updating grades
print("\nStudent Information with updated grades:")
for key, value in student.items():
    print(f"{key}: {value}")
