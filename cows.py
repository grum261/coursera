
# coding: utf-8

# In[7]:


n = int(input())


# In[8]:


if n in range(10, 20) or n % 10 in [0, 5, 6, 7, 8, 9]:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
