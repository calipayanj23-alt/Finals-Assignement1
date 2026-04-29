# 1: BASIC LIST ACTIVITIES

#ACTIVITY 1: CREATE A LIST
fruits = ["apple", "banana", "cherry"]
print(fruits)

#ACTIVITY 2: Access item
#Task: Access the first item and last item in the list
print("First item:", fruits[0])
print("Last item:", fruits[-1])

#ACTIVITY 3: LIST LENGTH
#task: print how many items are in the list
colors = ["red", "blue", "green", "yellow"]
print("Number of colors:", len(colors))

# 2: MODIFY A LIST

#ACTIVITY 4: CHANGE ITEM 
#task: Replace "banana" with "orange"
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print("Updated fruits:", fruits)

#ACTIVITY 5: ADD ITEM
#task: add "mangi" and insert "grape" at index 1
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.insert(1, "grape")
print(" after adding items:", fruits)

#Activity 6: REMOVE ITEM
#task: remove "banana" and remove the last item
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
fruits.pop() #remove last item
print(" after removing items:", fruits)

# 3: LOOPING THROUGH A LIST

#ACTIVITY 7: FOR LOOP
#task: print each item
animals = ["dog", "cat", "bird"]
print(animals)
for animal in animals:
    print(animal)

#ACTIVITY 8: WITH IDEX
#task: print index and value
numbers = [10, 20, 30, 40]
print("index and value:")
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

# 4: LIST OPERATIONS

#ACTIVITY 9: CHECK IF ITEMS EXISTS
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banana is in the list")
else:
    print("banana is not in the list")

#ACTIVITY 10: SORTING
numbers = [5, 2, 9, 1]
numbers.sort()
print("Ascending order:", numbers)
numbers.sort(reverse=True)
print("Descending order:", numbers)

#ACTIVITY 11: COPY A LIST
list1 = ["a", "b", "c"]
list2 = list1.copy()
print("Original list:", list1)
print("Copied list:", list2)