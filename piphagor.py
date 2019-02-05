
# coding: utf-8

# In[179]:


def length(x=[], y=[]):
    from math import sqrt
    inputs = [float(input()) for i in range(1, 5)]
    x = dict(zip([1, 2], inputs[::2]))
    y = dict(zip([1, 2], inputs[1::2]))
    return sqrt(pow(x[2] - x[1], 2) + pow(y[2] - y[1], 2))


# In[182]:


print(length())
