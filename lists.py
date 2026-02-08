myList = ["banana", "banana", "cherry", "banana", "banana", "apple"]
print(myList)

myList2 = [5, True, "banana", "apple", "banana"]
print(myList2)

item = myList[-1]
print(item)

for i in myList:
    print(i)

if "banana" in myList:
    print("Yes")
else:
    print("No")

if "mango" in myList:
    print("mango in list")
else:
    print("mango NOT in list")

length = len(myList)
print(length)

myList.append("mango")

if "mango" in myList:
    print("mango in list")
else:
    print("mango NOT in list")

length = len(myList)
print(length)

print(myList)

myList.insert(1, "blueberry")
print(myList)

item = myList.pop();
print(item)

print(myList)

item = myList.remove("banana");
print(item)
print(myList)

myList.reverse()
print(myList)

newList = sorted(myList)
print(newList)

multipleList = ["lemon"] * 5
print(multipleList)

bigList = myList + myList2 + newList + multipleList
print(bigList)

length = len(bigList)
print(length)

concatedBigList = bigList[::3]
print(concatedBigList)

print(len(concatedBigList))

# List Comprehension
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
squaredNumbers = [number * number for number in numbers]
print(squaredNumbers)

