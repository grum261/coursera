
# coding: utf-8

# In[27]:


s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
intersection = list(set(s1).intersection(s2))
intersection.sort()
print(*intersection)
