
# coding: utf-8

# In[43]:


print(*list(map(lambda x: 1 if x == 0 else x*fact(x - 1),
                [i for i in range(int(input()) + 1)])))
