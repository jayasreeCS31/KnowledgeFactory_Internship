numbers = [x for x in range(1, 11)]
print("List:")
print(numbers)
even = [x for x in range(1, 11) if x % 2 == 0]    #even
print("\nEven Numbers:")
print(even)
squares = [x*x for x in range(1, 6)]               #square
print("\nSquares:")
print(squares)
letters = {char for char in "banana"}               #set
print("\nSet Comprehension:")
print(letters)
square_dict = {x: x*x for x in range(1, 6)}          #dic
print("\nDictionary Comprehension:")
print(square_dict)
result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]     #ifelse
print("\nIf Else Comprehension:")
print(result)