"""
A lambda is an anonymous one-line function
"""
from functools import reduce
add10 = lambda x: x + 10 
print(add10(19))

"""
lambda functions may also take up multiple arguments
"""
mult = lambda x,y: x * y
print(mult(2,4))

"""
Lambdas are mostly used for functions that are to be called only once
They may also be used as an argument to other higher functions
"""
points2D = [(1,2), (15,1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)

# Sort by sum
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)

"""
Lambdas may also be used with the map() function
map(func, sequence)
"""
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(a)
print(list(b))

"""
You may achieve the same thing as above using the
list comprehension method as below
"""
c = [x*2 for x in a]
print(c)


"""
Lamndas also come in handy with the filter function
filter(func, seq)
filter method returns all the elements whose value evaluate to true
"""
d = filter(lambda x: x%2, a)
print(list(d))

"""
The above may also be achieved using the list comprehension method
"""
d = [x for x in a if x%2]
print(d)


"""
Lambdas may also be used with the reduce function
reduce(func, seq)
"""
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
