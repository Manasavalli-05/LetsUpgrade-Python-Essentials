#!/usr/bin/env python
# coding: utf-8

# In[1]:


                 # 1 List and its default functions

#1len()

a = ["hi","hello","welcome"]
print("length of list a =",len(a))

#2Min()

a,b = ["c++","Java","Python"],[56,90,28,49]
print("minimum value in a =", min(a))
print("minimum value in b =", min(b))

#3Max()

a = ["path","Instance","class","variable"]
print("Max value in a =", max(a))
a = [1,2,3,4]
b = [1,2,3,4,5]
print("Max value is :",max (a,b))

#4Range()

list1=["hi","hello","welcome"]
print("given list:",list1)
list2=list(range(5))
list1.extend(list2)
print("extended list",list1)

#5list()

a = {"I", "am", "a","set"}
print(list(a))

a = ("i","am","a","tuple")
print(list(a))


             # 2 Dictionary and its default functions 

#1Clear()

d = {1: "one", 2:"two"}

d.clear()
print('d=', d)

#2Copy()

original = {1:'one', 2:'two'}
new = original.copy()

print('Original:', original)
print('New:', new)

#3Values()

sales = {"apple":2, "orange":3, "grapes":4}

values = sales.values()
print("Original items:", values)

del[sales["apple"]]
print("Updated items:", values)

#4Items()

sales = {"Hi":2, "Hello":3, "Welcome":4}

items = sales.items()
print("Original items:", items)

del[sales["Hello"]]
print("Updated items:", items)

#5Pop()

Fruits ={'Mango': 4, 'Apple':6, 'Gua':7}

element = Fruits.pop('Gua')
print("The popped element is:", element)
print("The dictionary is:",Fruits)


                    # 3 Sets and its Default Functions

#1Add()

vowels = {'a','e','i','u'}

vowels.add('o')
print('Vowels are:',vowels)

vowels.add('a')
print('Vowels are:', vowels)

#2Clear()

vowels = {'a','e','i','o','u'}
print('vowels (before clear):', vowels)

vowels.clear()
print('Vowels (after clear):', vowels)

#3Remove()

language = {'English','French','German'}

language.remove('German')

print("Updated language set:", language)

#4Pop()

A = {'a','b','c','d'}

print('Return value is', A.pop())
print('A = ', A)

#5Difference()

A = {'a','b','c','d'}
B = {'g','b','c'}

print(A.difference(B))

print(B.difference(A))


                # 4 Tuple and explore default methods

#1Count()

my_tuple = ('a','p','p','l','e')

print(my_tuple.count('p'))

#2Index()

Cars = ("Audi","Benz","Honda","Jaguar")

print(Cars.index("Benz"))


                     # 5 String and explore default methods

#1Capitalize()

string = "+ is an operator."

new_string = string.capitalize()

print('Old String:', string)
print('New String:', new_string)

#2Center()

string ='This is a Assignment'

new_string = string.center(24)

print("Centered string:", new_string)

#3Format()

print("The number is:{:d}".format(123))

print("The float number is:{:f}".format(123.345678))

print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))

#4Rjust()

string = "cat"
width = 5

print(string.rjust(width))

#5Ljust()

string = "Tiger"
width = 5

print(string.ljust(width))
                                



# In[ ]:




