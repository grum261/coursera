
# coding: utf-8

# In[10]:


import itertools


# In[29]:


n, k = [int(input()) for i in range(2)]

print(len(list(itertools.combinations(range(n), k))))
