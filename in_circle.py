
# coding: utf-8

# In[22]:


def isinc(x, y, xc, yc, r):
    return True if (x - xc)**2 + (y - yc)**2 <= r**2 else False


def ipic(x, y, xc, yc, r):
    return isinc(x, y, xc, yc, r)


# In[16]:


x, y, xc, yc, r = [float(input()) for i in range(5)]

if ipic(x, y, xc, yc, r) is True:
    print('YES')
else:
    print('NO')
