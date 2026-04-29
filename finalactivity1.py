#FINAL ACTIVITY 1

#PART 1: IDENTIFY AND CREATE

#1. A TUPLE OF 5 FAVORITE FRUITS
from asyncio import tasks


favorite_fruits = ("Mango", "Banana", "Apple", "Grapes", "Pineapple")
print ("tuple of 5 favorite fruits: ", favorite_fruits)

#2 A LIST OF 5 DAILY TASKS
daily_tasks = ["Wake up", "Brush teeth", "Eat breakfast", "Attend online class", "Walk at night"]
print ("list of 5 daily tasks: ", daily_tasks)

#3 A SET OF UNIQUE NUMBERS
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print ("set of unique numbers: ", unique_numbers)

#4 A DICTIONARY 
student = {
    "name": "Jamella",
    "age": 18,
    "course": "BSIT"
}
print ("dictionary of student information: ", student)

#PART 2:MANIPULATION
       #LIST TASKS
#ADD A NEW TASK

daily_tasks.append("exercise")
print ("\nAdding a new taks: ", daily_tasks)

#REMOVE A TASK
daily_tasks.remove("Attend online class")
print ("\nRemoving a task: ",  daily_tasks)

daily_tasks.sort()  #SORT THE TASKS
print ("\nSorting the tasks: ", daily_tasks)

# ----- TUPLE TASK -----
# Try to change one value (this will cause an error because tuples are immutable)
try:
    favorite_fruits[0] = "pineapple"
except TypeError as e:
    print("\nTuple Error:", e)
    print("Explanation: Tuples cannot be changed after creation (immutable).")


# ----- SET TASKS -----
# Add a number
unique_numbers.add(6)
print("\nAfter adding a number:", unique_numbers)

# Remove a number
unique_numbers.remove(2)
print("After removing a number:", unique_numbers)

# Show how duplicates are removed
numbers_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers_list)
print("Converted to set (duplicates removed):", set(numbers_list))


# ----- DICTIONARY TASKS -----
# Add a new key "grade"
student["grade"] = "1.5"
print("\nAfter adding grade:", student)

# Update age
student["age"] = 18
print("After updating age:", student)

# Print all keys and values
print("\nAll keys:", student.keys())
print("All values:", student.values())

# Print key-value pairs
print("\nDictionary items:")
for key, value in student.items():
    print(key, ":", value)






