
# coding: utf-8


# In[28]:


n = int(input())
i = 2
while i <= n and n % i != 0:
        i += 1
else:
    print(i)
