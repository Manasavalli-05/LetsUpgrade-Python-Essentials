#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1

def prime1(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True

import unittest
import prime
class TestPrime(unittest.TestCase):
    def checknotprime(self):
        num=4
        res=prime.prime1(num)
        self.assertEqual(res,False)
    def checkprime(self):
        num=17 
        res=prime.prime1(num)
        self.assertEqual(res,True)
if __name__==__main__:        
    unittest.main()
    
    
#Question 2

def armstrong(lst):
    for num in lst:
        length=len(str(num))
        sum1=0
        temp=num
        while(temp!=0):
            rem=temp%10
            sum1=sum1+pow(rem,length)
            temp=temp//10
        if(sum1==num):
            yield num
lst=list(range(1000))
print(list(armstrong(lst)))


# In[ ]:





# In[ ]:




