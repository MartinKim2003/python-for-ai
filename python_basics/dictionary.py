# {}
# Dictionaries store data in key-value pairs
# Update and overwrite information
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["name"]
person["name"] = "Dave" # Dave instead of Alice

person["licence"] = True # new key value added in the end
del person["licence"] # to delete license key value from the dictionary

""""""
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})
""""""
# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"