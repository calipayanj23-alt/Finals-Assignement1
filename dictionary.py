#ACTIVITY 1: FILL IN THE BLANKS
student = {
    "name": "Ana",
    "age": 20,
    "course" : "IT"
}

print(student["name"])

#ACTIVITY 2: ADD AND UPDATE
student = { "name": "Ana", "age": 20, "course": "IT" }
#add grade
student ["grade"] = 95

#update age
student ["age"] = 21

print(student)

#ACTIVITY 3: LOOPING THROUGH DICTIONARY
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
for key in car:
    print(key, ":", car[key])

#ACTIVITY 4: (CHALLENGE) MINI PHONEBOOK
phonebook = {
    "Ana": "09123456789",
    "Mark": "09876543210",
    "Lisa": "09555555555"
}

print("Name:", "Ana")
print("Phone number:", phonebook["Ana"])