
# coding: utf-8

# In[22]:


days = 0
nights = 0
h, a, b = [int(input()) for i in range(3)]
while a * days - b * nights <= h:
    if a * days - b * (nights - 1) == h:
        if days != 0:
            print(days)
            break
    elif a * days - b * (nights - 1) > h:
        if days != 0:
            print(days)
            break
    else:
        pass
    days += 1
    nights += 1
