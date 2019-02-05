
# coding: utf-8

# In[7]:


sec = int(input())

print('{0:02d}:{1:02d}:{2:02d}'.format((sec // 3600) % 24,
                                       (sec // 60) % 60, sec % 60))
