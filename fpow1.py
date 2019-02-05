
# coding: utf-8

# In[45]:


def fpow1(a, n):
    if n == 0:
        return 1
    p = fpow1(a*a, n // 2)
    if n % 2:
        p *= a
    return p

x = float(input())
y = int(input())

print(fpow1(x, y))
