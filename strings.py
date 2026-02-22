"""
A string is an immutable, ordered text representation
"""
string1 = "I am in double quotes"
print(string1)

string2 = 'I am in single quotes, it is more common to use single quotes'
print(string2)

string3 = """
I am in triple double quotes.
This may be used in preformatted text,
kind of like pre in css+html

If you use the '\' escape \
Then the next text will be in the same line \
No new line will be created
"""
print(string3)

print("***********************************")

myString = "Hello World"
indexOfChar = 3
char = myString[indexOfChar]
print(f"The character of index {indexOfChar} in {myString} is {char}")

"""
Strings are immutable, therefore, doing something like:
    myString[indexOfChar] = 'x'
Will cause an error.
"""

"""
You may get a substring using:
    string[startIndex: endIndex] // endIndex is not included
    string[:endIndex] // starts from the start of the string to the endIndex, endIndex not included
    string[startIndex:] // starts at startIndex and goes all the way to the end of the string
"""

subString = myString[2:4]
print(subString)

subString = myString[:4]
print(subString)

subString = myString[2:]
print(subString)

"""
Strings are iterable too!
"""
for i in myString:
    print(f"**********************************\n{i}")

"""
You may use conditionals to find if a character or substring is in a string
"""
if "H" in myString:
    print("H is in the string")
else:
    print("H not in string")

if "Hel" in myString:
    print("Hel in string")
else:
    print("Hel not in string")

"""
Common string manipulation functions
"""
myString = "    Hello World     "
print(myString)

myString = myString.strip()
print(myString)



