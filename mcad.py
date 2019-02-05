
# coding: utf-8

# In[21]:


v, t = [int(input()) for i in range(2)]

assert v in range(-1001, 1001) and t > 0

print(((v * t) % 109 + 109) % 109)
