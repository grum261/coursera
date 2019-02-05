
# coding: utf-8

# In[9]:


def isinsq(x, y):
    return True if abs(x) <= 1 and abs(y) <= 1 else False


def IsPointInSquare(x, y):
    return isinsq(x, y)


# In[10]:


inputs = [float(input()) for i in range(2)]
x, y = inputs[0], inputs[1]


# In[11]:


if IsPointInSquare(x, y) is True:
    print('YES')
else:
    print('NO')
