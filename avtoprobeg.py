
# coding: utf-8

# In[36]:


def days(n, m):
    return int((m - 1 + n) / n)


n, m = [int(input()) for i in range(2)]

print(days(n, m))
