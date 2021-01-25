#!/usr/bin/env python
# coding: utf-8

# ## Python Assignment-5

# In[1]:


# computing the division of two numbers and checking for exceptions
def compute(a,b):
    try:
        a/b
    except:
        print("This tends to infinite so please change the denominator")
    else:
        print(a/b)
        


# In[2]:


# Using the example given in the assignment
compute(5,0)


# In[3]:


# Using another example
compute(5,4)


# In[4]:


# Taken the input as mentioned
subjects=["Americans ","Indians"]

verbs=["play","watch"]

objects=["Baseball","Cricket"]


# In[5]:


# Printing the desired output
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i +" " + j +" " + k)

