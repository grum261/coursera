
# coding: utf-8

# In[2]:


s1, s2 = ((int(input()) + int(input()) - 1) % 2 for _ in range(2))
print('YES' if s1 == s2 else 'NO')
