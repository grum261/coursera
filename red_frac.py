
# coding: utf-8

# In[1]:


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


# In[2]:


inputs = [int(input()) for i in range(2)]

print(*list(map(lambda x: x // gcd(*inputs), inputs)))
