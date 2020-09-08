#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Armstrong number

def armstrong(num):
    n=len(str(num))
    temp=num
    sum1=0
    while(temp!=0):
        rem=temp%10
        sum1=sum1+pow(rem,n)
        temp=temp//10
    if(sum1==num):
        return True
 
for i in range(1042000,7062648265):
        if armstrong(i):
            print("The first armstrong number is", i)
            break

