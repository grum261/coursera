
# coding: utf-8

# In[4]:


series = []
number = int(input())
while number != 0:
    try:
        series.append(number)
        number = int(input())
    except:
        break

print(sum(series))
