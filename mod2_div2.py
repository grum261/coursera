
# coding: utf-8

# In[37]:


import itertools

inputs = [int(input()) for i in range(3)]


# In[43]:


if tuple(map(lambda x: x % 2,
             inputs)) in list(itertools.product(range(2), repeat=3))[1:7]:
    print('YES')
else:
    print('NO')
