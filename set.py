#ACTIVITY 1: REMOVE DUPLICATE
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

#ACTIVITY 2: ADD AND REMOVE 
fruits = {"apple", "banana", "orange"}
fruits.add("grape")
fruits.remove("banana")
print(fruits)

#ACTIVITY 3: SET OPERATIONS
a = {1, 2, 3}
b = {3, 4, 5}
#Union
print("union:", a | b)

#Intersection
print("intersection:", a & b)

#ACTIVITY 4: (CHALLENGE): COMMON STUDENTS
#GIVEN
classA = {"John", "Ana", "Mark"}
classB = {"Ana", "Mark", "Lisa"}

#STUDENTS IN BOTH CLASSES
common_students = classA & classB
print("Common students:", common_students)

# ALL STUDENTS
all_students = classA | classB
print("All students:", all_students)

