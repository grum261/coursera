
# coding: utf-8

# In[1]:


import itertools


# In[20]:


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
a = list(itertools.chain(s1, s2))
a.sort()
print(*a)
