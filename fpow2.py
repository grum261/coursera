
# coding: utf-8

# In[1]:


def fpow2(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1./x
    p = fpow2(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


# In[6]:


a = float(input())
n = int(input())

print(fpow2(a, n))
