"""
This is a container data structure that groups and stores multiple items in a single unit
allowing for organization retrival and iteration
Counter, namedtuple, orderedDict, defaultDict, deque
"""
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

my_collection = "abbccabbccabbccabccabccabccabcc"
my_counter = Counter(my_collection)
print(my_counter.values())

"""
To get the most common item in a collection
"""
print(my_counter.most_common(1))

"""
Below we'll get 2 of the most common types
Gives a list of tupples
"""
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0][1])
print(list(my_counter.elements()))

"""
This section is on namedtules
This is a data type similar to struct
"""
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x)
print(pt.y)

"""
This section is on OrderedDict
They are just like dict exccept they remember the 
order they were originally in.
"""
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

"""
This section is about defaultDict
It is similar to the normal dict, except,
it will have a default value if the key has not been set yet
"""
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict["b"] = 2
print(default_dict)
print(default_dict[5])


"""
This section is about deque
This is a double-ended queue
You can add elements both at the end or at the start
"""
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)

