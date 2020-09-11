#!/usr/bin/env python
# coding: utf-8

# In[5]:



#Question 1


def get_input(fibonacci):
    def inp_func():
        n=int(input("Enter a number"))
        fibonacci(n)
    return inp_func
@get_input
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
fibonacci()



#Question 2


try:
    file=open("ex.txt",r)
    file.write("nwelcome to the world")
except:
    print("The file cannot be written.... sorry:")
    
    
    
    


# In[ ]:




