"""
This is a mudule with a collection of tools for handling iterators
iterators are data types that can be iterated upon.
product, permutations, combinations, accumulate,
groupby, and infinite iterators
"""
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator

"""
This section is about product function
This function, when used with lists gives
the cartesian product of the lists
"""
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))

# Repeat
a = [1,2]
b = [3]
prod = product(a,b, repeat = 2)
print(list(prod))

"""
This section is about permutations
A permutation returns all possible orderings of
a the elements, where the order of appearance of
the elements matters
"""
a = [1,2,3]
perm = permutations(a)
print(list(perm))

# Declare the length of the permutations
perm = permutations(a, 2)
print(list(perm))

"""
This section is about combinations
A combination return all the possible orderings
of the elements, where the order of appearance of
the elements does NOT matter
"""
a = [1,2,3,4]
# Unlike permutations(), combinations() requires a second argument for length
comb = combinations(a,2)
print(list(comb))

"""
If you want the combinations to also repeat the element itself
then, you may use the function combinations_with_replacement
"""
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

"""
This section is about the accumulate function
This functions returns the accumulated sums
"""
a = [1,2,3,4]
accum = accumulate(a)
print(a)
print(list(accum))

# You may use the operator function to specify the action
mul_accum = accumulate(a, func=operator.mul)
print("Multiplication operator")
print(list(mul_accum))
a = [2,3,6,3,7,2]
max_accum = accumulate(a, func=max)
print(a)
print("Max value")
print(list(max_accum))

"""
This section is about the groupby function
This is an iterator that returns keys and groups from an iterable
"""
def smaller_than_3(x):
    return x < 3

a = [1,2,3,4,5,6,7,8,9]
group_object = groupby(a, key=smaller_than_3)

for key, value in group_object:
    print(key, list(value))

persons = [
            {'name': 'Tim', 'age': 25},
            {'name': 'Dan', 'age': 25},
            {'name': 'Lisa', 'age': 28},
            {'name': 'Claire', 'age': 28},
            {'name': 'Erick', 'age': 24}
          ]

persons_grouped_by_age = groupby(persons, key=lambda x: x['age'])
for key, value in persons_grouped_by_age:
    print(key, list(value))

