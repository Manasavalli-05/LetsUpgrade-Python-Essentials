#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Question 1


iplist=[]
sub_list=[1,1,5]
try:
     while True:
         iplist.append(int(input()))
except:
     pass
e=0
flag=0
for i in range(0,len(iplist)):
    if sub_list[e]==iplist[i]:
         e+=1
    if e==3:
          flag=1
          e=0
if flag==1:
    print("It's a match")
else:
    print("It's Gone")


    
#Question 2


def Prime(x):  
    if (x>1):
        for i in range(2,x):
            if(x%i==0):
                return False
        else:
            return True
    else:
        return False
fltrObj=filter(Prime, range(2500))           
print(list(fltrObj))

#Question 3

capital=lambda x: x.title()
list1=["hey this is sai","I am in mumbai"]
print(list(map(capital,list1)))


# In[ ]:





# In[ ]:




