
# coding: utf-8

# In[58]:


print(', '.join([str(n)
                 for n in range(10, 100) if 2 * (n // 10) * (n % 10) == n]))
