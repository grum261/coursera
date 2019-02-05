
# coding: utf-8

# In[29]:


def lagr(n, k=0):
    n1 = int(n ** 0.5)
    if n1 ** 2 == n:
        print(n1, end='')
        return int(n1 ** 2)
    while n1 >= 1:
        s = n1 ** 2
        if k + 1 <= 3:
            s += lagr(n - n1 ** 2, k + 1)
        if s == n:
            print(' ', n1, sep='', end='')
            return int(s)
        n1 -= 1
    return 0


# In[33]:


n = int(input())
lagr(n)
