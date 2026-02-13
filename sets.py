"""
A set is a data collection that's unordered, mutable, but does not allow duplicates
"""
mySet = {1, 2, 3, 4, 5}

print(mySet)

"""
If we put multiple duplicate elements in the set, only one of the elements is shown
"""
mySetWithDuplicates = {1, 2, 3, 2, 3, 2, 4, 2, 5 ,4, 1}

print(mySetWithDuplicates)

"""
A string in a set will be 'exploded' and duplicates removed
"""
stingSet = set("Hello World")
print(stingSet)

"""
You may add elements to a set using the .add method like so, since it is mutable
"""
mySet.add(6)
mySet.add(7)
mySet.add(8)
mySet.add(9)
print(mySet)

"""
You may remove an element from a set using the .remove() method.
The element must be in the set, otherwise you will get an error
"""
mySet.remove(7)
print(mySet)

"""
You may also remove an element from the set using the .discard() method. 
This method does not throw an error if an element does not exist in the set
"""
mySet.discard(23)
print(mySet)

"""
You may remove all the elements in a set using the clear() method
"""
setToBeCleared = {1,2,3,4,5,6,7,8,9}
print(setToBeCleared)
setToBeCleared.clear()
print(setToBeCleared)

"""
A set is iterable
"""
for i in mySet:
    print(i)

if 3 in mySet:
    print("3 is in set")
    mySet.remove(3)

if 3 in mySet:
    print("3 not in set")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
"""
Union and Intersection
"""
odd = {1,3,5,7,9}
even = {0,2,4,6,8}
prime = {2,3,5,7}

print(odd)
print(even)

unionized = odd.union(even)
print(unionized)

"""
Intersection will only show the elements that are in both sets
"""
intesectionized = odd.intersection(prime)
print(intesectionized)

"""
The difference of sets will bring all the elements that are in the 
first set that are not in the second set
"""
setA = {1,2,3,4,5,6,7,8,9,13,14,15,16,17,18}
setB = {1,2,3,5,6,7,8,9,11,12,13,14,15,20,21}
diffA_B = setA.difference(setB)
print(diffA_B)

diffB_A = setB.difference(setA)
print(diffB_A)

"""
symmetric_difference will show all the elements that are not in both sets
"""
symDiff = setA.symmetric_difference(setB)
print(symDiff)

"""
If you want to also trnasform the original set, you may use update()
"""
setA.update(setB)
print(setA)

"""
intersection_update will update the original set keeping only the elements that are in both sets
"""

print("++++++++++++++++++++++++++++++++++++++++")

"""
A frozen_set is a collection data type too.
It is similar to set, except it is immutable
"""
frozen = frozenset([1,2,3,4,5,6,7])

