"""x = "python is awesome"
print(x)

x = "python"
y = "is"
z = "awesome"
print(x, y, z)
"""
"""x = "awesome"
def myfunc():
    print("python is " + x)
myfunc()"""

"""x = "awesome"
def myfunc():
    x = "good"
    print("python is " + x)
myfunc()
print("python is " + x)"""

"""x = "awesome"
def myfunc():
    global x
     x = "good"
    print("python is " + x)
myfunc()
#print("python is " + x)"""

#Find the type of the variable
"""x = 2
print(type(x))
y = 2.10
print(type(y))
z = "python"
print(type(z))
w = True
print(type(w))
e = False
print(type(e))"""

# for pick any one random no. 
"""import random
print(random.randrange(1,5))"""

"""x = 5
x = float(x)"""

"""tuple1 = ("apple", "mango", "kiwi")
tuple2 = (1, 2, 3)
tuple3 = (True, False, True, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))"""

#show tuple item 
"""tuple1 = ("apple", "mango", "kiwi")
print(tuple1[0])"""

#show tuple range  from range to end
"""tuple1 = ("apple", "mango", "kiwi", "banana", "gauva")
print(tuple1[2:])"""

#show tuple range start to last range
"""tuple1 = ("apple", "mango", "kiwi", "banana", "gauva")
print(tuple1[:4])"""

#show last item of tuple
"""tuple1 = ("apple", "mango", "kiwi", "banana", "gauva")
print(tuple1[-1])"""

"""thislist = ["apple", "banana", "kiwi"]
thislist[1] = "orange"
print(thislist)

thislist1 = ["apple", "banana", "kiwi"]
thislist1.append("orange")
print(thislist1)

thislist2 = ["apple", "banana", "kiwi"]
thislist2.insert(0, "orange")
print(thislist2)"""

# thislist = ["apple", "mango", "kiwi"]
# thislist2 = ["nuts", "peanuts", "sandwich"]
# thislist.extend(thislist2)
# print(thislist)

#POP is used for removed the item
#pop(0) for first position element remove
"""thislist = ["apple", "mango", "kiwi", "mango", "mang"]
thislist.pop()
print(thislist)"""

"""thislist = ["apple", "mango", "kiwi",]
del thislist[0]
print(thislist)

thislist2 = ["nuts", "peanuts", "sandwich"]
thislist2.clear()
print(thislist2)"""

"""thislist = ["apple", "kiwi", "mango", "this"]
for x in thislist:
    print(thislist)
    
    
for x in range(2,12):
    print(x)"""


from wsgiref.simple_server import sys_version


print(sys_version)
