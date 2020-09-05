#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Question 1

n = int(input("Enter altitude of plane:"))

if n==1000:
    print("Safe to land")
elif n==4500:
    print("Bring down to 1000")
elif n==6500:
     print("Turn Around")
        

#Question 

lower = 1
upper = 200

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower, upper+1):

    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)


# In[ ]:




