
# coding: utf-8

# In[105]:


inputs = [int(input()) for i in range(3)]


# In[110]:


count = 0
for i in range(3):
    if inputs[i] == inputs[i - 1]:
        count += 1
    else:
        continue


# In[112]:


print(2) if count == 1 else print(count)
