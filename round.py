
# coding: utf-8

# In[3]:


import math

x = float(input())
y = (x * 10) % 10
if y < 5:
    print(int(x))
if y >= 5:
    print(math.ceil(x))
