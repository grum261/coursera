
# coding: utf-8

# In[8]:


n = int(input())
s = [i for i in range(10**(n - 1), 10**n) if i % 2 == 1]
s.reverse()
print(*s)
