#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1

import math
class Cone:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def volume(self):
        print("The volume of the cone is",(1/3 *math.pi*self.height*(self.radius**2)))
    def surface_area(self):
        print("The base of the cone is",(math.pi*(self.radius**2)))
        print("The side of the cone is",(math.pi*self.radius*math.sqrt(self.radius**2+self.height**2)))
obj1=Cone(3,4)
obj1.volume()
obj1.surface_area()


#Question 2


class Bank:
    balance=0
    def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.balance=balance
    def deposit(self,money):
        self.balance=self.balance+money
        print("Money deposited is",money)
        print("The amount after deposit is",self.balance)
    def withdraw(self,money):
        if(money>self.balance):
            print("Entered amount is invalid, as balance is",self.balance)
        else:
            self.balance-=money
            print("The balance amount after withdrawal is",self.balance)
obj1 = Bank("Sharukh",78000)
print("The amount in the account is:",obj1.balance)
money = int(input("Enter  amount to be deposited:"))
obj1.deposit(money)
money = int(input("Enter  amount to be withdrawn:"))
obj1.withdraw(money)


# In[ ]:




