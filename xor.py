
# coding: utf-8

# In[85]:


from itertools import combinations


# In[112]:


def xor(x, y):
    return 1 if (x, y) in list(filter(lambda x: 0 < sum(x) < 2,
                                      combinations([0, 1, 0, 1], 2))) else 0


# In[116]:


print(xor(*list(int(input()) for i in [0, 1])))
