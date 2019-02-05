
# coding: utf-8

# In[2]:


a, b, c, d = [int(input()) for i in range(4)]


# In[24]:


if (a == c + 1 or a == c - 1 or a == c) \
   and (b == d + 1 or b == d - 1 or b == d):
    print("YES")
else:
    print("NO")
