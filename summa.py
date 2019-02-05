
# coding: utf-8

# In[1]:


def summ(a, b):
    if a == 0:
        return b
    return summ(a - 1, b + 1)


# In[6]:


x, y = [int(input()) for i in range(2)]

print(summ(x, y))
