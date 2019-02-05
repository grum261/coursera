
# coding: utf-8

# In[29]:


series = []
a, b = [int(input()) for i in [0, 1]]
if a < b:
    for i in range(a, b + 1):
        series.append(i)
else:
    for i in range(b, a + 1):
        series.append(i)
    series.reverse()


# In[31]:


print(*series)
