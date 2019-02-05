
# coding: utf-8

# In[2]:


n, m, k = [int(input()) for i in range(3)]


# In[3]:


if n * m >= k and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")
