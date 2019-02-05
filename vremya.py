
# coding: utf-8

# In[1]:


def vremya(h, m, s):
    return s + (h*60 + m)*60


# In[5]:


h1, m1, s1, h2, m2, s2 = [int(input()) for i in range(6)]

print(vremya(h2, m2, s2) - vremya(h1, m1, s1))
