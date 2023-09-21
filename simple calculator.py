#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python program for simple calculator
#use function to add two numbers
def add(x , y):
    return x + y
#use function to subtract two numbers
def sub(x , y):
    return x - y
#use function to multiple two numbers
def mul(x , y):
    return x * y
#use function to division two numbers
def div(x , y):
    return x / y
print("choose the operation::\n\n"
        "1.ADD\n\n"
      
        "2.SUB\n\n"
      
        "3.MUL\n\n"
      
        "4.DIV\n")
#take input from the user

select=int(input("choose the operation from 1 , 2 , 3 , 4::"))

print("\n")

a=int(input("enter the first number::"))

print("\n")

b=int(input("enter the second number::"))

print("\n")

if select == 1:
    print(a, "+", b, "=", add(a , b))
    
elif select == 2:
    print(a, "-", b, "=", sub(a , b))
    
elif select == 3:
    print(a, "*", b, "=", mul(a , b))  
    
elif select == 4:
    print(a, "/", b, "=", div(a , b)) 
else:
    ("***WRONG INPUT***")   


# In[ ]:




