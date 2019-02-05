
# coding: utf-8

# In[261]:


def lengths(x, y):
    from math import sqrt
    assert x, y in range(-30001, 30001)
    return [sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2) for i in range(3)]


# In[262]:


inputs = [int(input()) for i in range(6)]
x = list(inputs[:6:2])
y = list(inputs[1:7:2])
P = lengths(x, y)[0] + lengths(x, y)[1] + lengths(x, y)[2]
print(round(P, 6))
