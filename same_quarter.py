
# coding: utf-8

# In[32]:


def sign(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1


# In[30]:


x1, y1, x2, y2 = [int(input()) for i in range(4)]


# In[31]:


if sign(x1) == sign(x2) and sign(y1) == sign(y2):
    print('YES')
else:
    print('NO')
