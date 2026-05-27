fruits = ["apple", "banana", "mango"]
print("Original List:")
print(fruits)
print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])
fruits[1] = "orange"             #change
print("\nAfter Changing:")
print(fruits)
fruits.append("grapes")           #append
print("\nAfter append():")
print(fruits)
fruits.insert(1, "pineapple")     #insert
print("\nAfter insert():")
print(fruits)
fruits.extend(["kiwi", "papaya"])  #extnd
print("\nAfter extend():")
print(fruits)
fruits.remove("apple")            #remove
print("\nAfter remove():")
print(fruits)
fruits.pop(2)                     #pop
print("\nAfter pop():")
print(fruits)
print("\nList Slicing:")          #slicing
print(fruits[1:4])
print("\nLength of List:")       #length
print(len(fruits))
fruits.sort()                    #sorting
print("\nAfter sort():")
print(fruits)
fruits.sort(reverse=True)       #reverse sorting
print(fruits)
fruits.reverse()
print("\nAfter reverse():")
print(fruits)
print("\nLooping Through List:")     #loop
for fruit in fruits:
    print(fruit)
new_fruits = fruits.copy()       #copy
print("\nCopied List:")
print(new_fruits)
numbers = [[1, 2], [3, 4]]       #nested list
print("\nNested List:")
print(numbers)
print(numbers[1][0])
list1 = [1, 2]             #concatination
list2 = [3, 4]
result = list1 + list2
print("\nConcatenated List:")
print(result)
print("\nRepeated List:")    #repeating
print(list1 * 3)

# List comprehension
squares = [x*x for x in range(5)]
print("\nList Comprehension:")
print(squares)

# Clearing list
temp = [10, 20, 30]
temp.clear()
print("\nAfter clear():")
print(temp)

#delete
data = [100, 200, 300]
del data
print("\nEntire list deleted successfully")