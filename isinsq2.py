
# coding: utf-8

# In[16]:


def insquare(x, y, d=2):
    return abs(x) + abs(y) <= d/2


# In[26]:


inputs = [float(input()) for i in range(2)]

if insquare(*inputs) is True:
    print('YES')
else:
    print('NO')
