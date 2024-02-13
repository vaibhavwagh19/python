# string
x = "Hello World" 
x = str("Hello World") #Setting the Specific Data Type

#integer
x= 20
x = int(20)  #Setting the Specific Data Type

# float
x= 20.5
x = float(20.5)   #Setting the Specific Data Type

#complex - consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex number.
x = 1j
x = complex(1j)   #Setting the Specific Data Type

# list -  an ordered data structure with elements separated by a comma and enclosed within square brackets.
# List items are ordered, changeable, and allow duplicate values.
x = ["luffy","zoro","sanji"]
x = list(("apple", "banana", "cherry"))   #Setting the Specific Data Type

# tuple -  an immutable object, which means it cannot be changed, and we use it to represent fixed collections of items.
# A tuple is a collection which is ordered and unchangeable.
x = ("luffy","zoro","sanji")
x = tuple(("apple", "banana", "cherry"))   #Setting the Specific Data Type

# dictionary - a data structure, used to store values in key:value format.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
x = {"luffy":1,"zoro":2,"sanji":3}
x = dict(name="John", age=36)

# set - A set is a data collection type used in Python for storing multiple items in a single variable. 
# A set is a data type in Python that is used to store collections of data. Sets are unordered, unchangeable, and unindexed.
x = {"luffy,","zoro","sanji"}
x = set(("apple", "banana", "cherry"))  #Setting the Specific Data Type

# range - The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# syntax -> range(start, stop, step)
x = range(6)
x = range(6)   #Setting the Specific Data Type
 
# frozenset - The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
x = frozenset({"luffy","zoro","sanji"})
x = frozenset(("apple", "banana", "cherry"))   #Setting the Specific Data Type

# boolean - The bool() function allows you to evaluate any value, and give you True or False in return.
x = True
x = bool(5)    #Setting the Specific Data Type

# bytes - The bytes() function returns a bytes object.
# It can convert objects into bytes objects, or create empty bytes object of the specified size.
x = b"hello"
x = bytes(5)  #Setting the Specific Data Type

# bytearray - The bytearray() function returns a bytearray object.
# It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
x = bytearray(5)
x = bytearray(5)   #Setting the Specific Data Type

# memoryview - The memoryview() function returns a memory view object from a specified object.
x = memoryview(bytes(5))
x = memoryview(bytes(5))   #Setting the Specific Data Type

# nonetype
x = None
