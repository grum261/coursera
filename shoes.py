
# coding: utf-8

# In[14]:


n = int(input())
tests = list(map(int, input().split()))


# In[15]:


count = 0
for test in sorted(tests):
    if test >= n:
        count += 1
        n = test + 3


# In[17]:


print(count)
