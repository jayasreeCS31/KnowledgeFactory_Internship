# TUPLE
fruits = ("apple", "banana", "mango")
print("Tuple:")
print(fruits)
print("\nAccessing Tuple:")
print(fruits[0])
print("\nLooping Tuple:")
for fruit in fruits:
    print(fruit)

# SET
numbers = {1, 2, 3, 4}
print("\nSet:")
print(numbers)
numbers.add(5)
print("\nAfter Adding:")
print(numbers)
numbers.remove(3)
print("\nAfter Removing:")
print(numbers)
print("\nLooping Set:")
for num in numbers:
    print(num)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print("\nUnion:")
print(a | b)
print("\nIntersection:")
print(a & b)
print("\nDifference:")
print(a - b)