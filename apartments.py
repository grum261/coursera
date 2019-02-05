
# coding: utf-8

# In[6]:


x, y = [int(input()) for i in [0, 1]]


# In[7]:


print('YES') if y % (y - x + 1) == 0 else print('NO')
