# FINAL ASSIGNMENT #1

# ----------------------
# LIST OPERATIONS
# ----------------------
print("LIST OPERATIONS")
my_list = ["apple", "banana", "cherry"]
print("Original list:", my_list)

# Add 1 new item
my_list.append("orange")
print("After adding one item:", my_list)

# Remove 1 item
my_list.remove("banana")
print("After removing one item:", my_list)

# Sort the list
my_list.sort()
print("After sorting:", my_list)


# ----------------------
# TUPLE OPERATIONS
# ----------------------
print("\nTUPLE OPERATIONS")
my_tuple = (1, 2, 3, 4)
print("Original tuple:", my_tuple)

# Try modifying one element
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

# Explanation
print("Explanation: Tuples cannot be changed because they are immutable.")


# ----------------------
# SET OPERATIONS
# ----------------------
print("\nSET OPERATIONS")
my_set = {10, 20, 30}
print("Original set:", my_set)

# Add a value
my_set.add(40)
print("After adding a value:", my_set)

# Remove a value
my_set.remove(20)
print("After removing a value:", my_set)

# Print updated set
print("Updated set:", my_set)


# ----------------------
# DICTIONARY OPERATIONS
# ----------------------
print("\nDICTIONARY OPERATIONS")
student = {
    "name": "Jamella",
    "age": 17,
    "course": "ICT"
}
print("Original dictionary:", student)

# Add a new key "grade"
student["grade"] = "A"
print("After adding grade:", student)

# Update age
student["age"] = 18
print("After updating age:", student)

# Print all keys
print("All keys:", student.keys())
