
# coding: utf-8

# In[8]:


def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1


# In[11]:


n = int(input())

print(sign(n))
