"""
A tuple is a collection data type that is ordered and immutable
It is like a list, except this cannot be changed once created
"""
myTuple = ("Max", 20, True, False, "Boston", 3.5)
print(myTuple)

"""
The parenthesis are optional
"""
myTupleWithoutParenthesis = "Max", 20, True, False, "Boston", 3.5
print(myTupleWithoutParenthesis)

"""
If you put only one item into a tuple then it will be recognised as a string
"""
tupleOrString = ("Max")
print(type(tupleOrString))

"""
But if you put a comma at the end then it becomes a tuple
"""
tupleOrString = ("Max",)
print(type(tupleOrString))

"""
You can also use the built in function to turn an iterable data type (such as a list) into a tuple
"""
myList = ["Max", 20, True, False, "Boston", 3.5]
print(type(myList))
tupleOrList = tuple(myList)
print(type(tupleOrList))

"""
To access an element in the tuple, you need to use the index
"""
print(myTuple[3])
print(type(myTuple[3]))

"""
A tuple is immutable, therefore the below code will bring an error:
    myTuple[0] = "Something Else"        
"""

"""
One can iterate on a tuple
"""
for i in myTuple:
    print(f"{type(i)}: {i}")

"""
One can also look if an element exists in a tuple
"""
if "Max" in myTuple:
    print("Max is in tuple")
else:
    print("Max not in the list")

if "James" in myTuple:
    print("James is in tuple")
else:
    print("James not in tuple")

"""
For this section we'll use a tuple with letters in it
"""
lettersTuple = ("a", "e", "b", "a", "d", "e", "a", "b", "a", "e", "d", "a", "c", "a");

"""
To get the number of elements in a tuple, just use the len function
"""
print(len(lettersTuple))

"""
To get the number of times an element appears in a tuple, we use the count() method
"""
print(f"The letter `a` appears {lettersTuple.count('a')} times in the lettersTuple")
print(f"The letter `b` appears {lettersTuple.count('b')} times in the lettersTuple")
print(f"The letter `c` appears {lettersTuple.count('c')} times in the lettersTuple")
print(f"The letter `d` appears {lettersTuple.count('d')} times in the lettersTuple")
print(f"The letter `e` appears {lettersTuple.count('e')} times in the lettersTuple")

"""
To get the first occurance of an element in a tuple, you use the index() function
"""
print(lettersTuple.index("d"))

"""
You can convert a tuple into a list using the list() function
"""
lettersList = list(lettersTuple)
print(f"lettersTuple is of type {type(lettersTuple)}")
print(f"lettersList is of type {type(lettersList)}")

"""
This next section will use a numbers tuple
"""
numbersTuple = (1,2,3,4,5,6,7,8,9,10)

"""
We can extract ony a section of a tuple using the slice method []
"""
print(f"The full tuple has elements: {numbersTuple}")
print(f"Sliced from the 2nd index to the end we get: {numbersTuple[2::]}")
print(f"The first elements till the 4th index are {numbersTuple[::4]}")
print(f"The tuples between index 1 and 5 are {numbersTuple[1:5]}")
print(f"The second last element in our tuple is {numbersTuple[-2]}")
print(f"Yoy can reverse the order of the tupple using topple[::-1], the reversed toople is:\n{numbersTuple[::-1]}")

"""
You can unpack a tuple, but th enumber of new variables must match the number of elements in the tuple
"""
myTuple = ("Max", 20, True, False, "Boston", 3.5)
name, age, criminalRecord, marriageStatus, city, score = myTuple
print(f"My name is {name}.\nI am {age} years old.\nDo I have a criminal record? {criminalRecord}\nAm I married? {marriageStatus}\nFinally, I scored a GPA of {score}")


