
# coding: utf-8

# In[106]:


series = []
number = int(input())
while number != 0:
    series.append(number)
    number = int(input())
series.append(0)
series.reverse()
print(*series)
