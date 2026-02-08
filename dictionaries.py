"""
This is a collection datatype that is unordered, mutable, and with value-key pairs
"""
myDict = {"name": "Max", "sex": "Male", "age": 28, "city": "New York"}
print(myDict)

myDict = dict(name="Mary", sex="Female", age=27, city="Boston")
print(myDict)

name = myDict["name"]
print(name)

print(f"{myDict['name']} is {myDict['age']} years old and lives in {myDict['city']}")

"""
To delete an item, there are several options.
1. del
"""
del myDict["name"]
print(myDict)

"""
2. the pop() method
"""
myDict.pop("age")
print(myDict)

"""
3. the popitem() method. This deletes the last pair in the dictionary
"""
myDict.popitem()
print(myDict)

"""
To check if a key exists, one may use:
1. An IF statement
"""
if "job" in myDict:
    print("There is a job key in the dictionary")
else:
    print("There is no job key in the dictionary")

"""
2. You may use the try except:
"""
try: 
    print(myDict["job"])
except:
    print("There is no job key in the dictionary")

myDict = dict(name="Mary", sex="Female", age=27, city="Boston")

"""
To loop through a dictionary, you may use:
1. the for loop
"""
for key in myDict:
    print(f"{key}: {myDict[key]}")

"""
If you only need the keys, you may use the key() function
"""
for key in myDict.keys():
    print(key)

print("---------------------------------------------------")

"""
If you only need the values, you may use the values() function
"""
for value in myDict.values():
    print(value)

print("---------------------------------------------------")

"""
You may also deconstruct the dictionary like so 
"""
for key, value in myDict.items():
    print(f"{key} === {value}")

"""
Copying a dictionary
The method below works, but when you modify the copy, the original gets modified too!
"""
myDictCopy = myDict
print(myDictCopy)
print(myDict)

myDictCopy.popitem()
print(myDictCopy)
print(myDict)

myDictCopy["email"] = "email@example.com"
print(myDictCopy)
print(myDict)

"""
The other, safer way is by using the copy() method
"""
print("---------------------------------------------------")
myDictCopy = myDict.copy()
print(f"Copy: {myDictCopy}")
print(f"Original: {myDict}")

myDictCopy.popitem()
print(f"Copy: {myDictCopy}")
print(f"Original: {myDict}")

myDictCopy["email"] = "email@example.com"
print(f"Copy: {myDictCopy}")


"""
The other, is by using the dict() function
"""
print("---------------------------------------------------")
myDictCopy = dict(myDict)
print(f"Copy: {myDictCopy}")
print(f"Original: {myDict}")

myDictCopy.popitem()
print(f"Copy: {myDictCopy}")
print(f"Original: {myDict}")

myDictCopy["email"] = "email@example.com"

"""
Merging two dictionaries
"""
print("---------------------------------------------------")
maxDict = {"name": "Max", "sex": "Male", "age": 28, "city": "New York"}
maryDict= dict(name="Mary", job="SWE", married=False, city="Boston", email="mary@example.com")
maxDict.update(maryDict)
print(maxDict)

"""
You can use any immutable data type as the key1. 
1. Using tuples
"""
print("---------------------------------------------------")
myTuple = (6,7)
myDict = {myTuple: 13}
print(myDict)
