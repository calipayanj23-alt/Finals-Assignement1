#ACTIVITY: ACCESS ELEMENTS
colors = ("red", "green", "blue")
print("First color:", colors[0])
print("Last color:", colors[-1])

#ACTIVITY 2: SLICING
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # Output: (20, 30, 40)

#ACTIVITY 3: TUPLE METHODS
nums = (1, 2, 2, 3, 2,)

#count how many times 2 appears
print("Count of 2:", nums.count(2))
      
#find index of 3
print("Index of 3:", nums.index(3))

#ACTIVITY 4: TUPLE PACKING AND UNPACKING
point = (5, 10)
x, y = point

print("x:", x)
print("y:", y)

#ACTIVITY 5: (*CHALLENGE) COMBINE TUPLES
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2 *2
print("Combined tuple:", combined)