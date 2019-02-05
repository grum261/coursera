
# coding: utf-8

# In[31]:


from math import sqrt

a, b, c = [float(input()) for i in range(3)]


# In[32]:


p = (a + b + c)/2
s = sqrt((p*(p - a)*(p - b)*(p - c)))
print(s)
