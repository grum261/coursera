
# coding: utf-8

# In[1]:


x1, y1, x2, y2 = [int(input()) for i in range(4)]

print('YES') if abs(x1 - x2) == abs(y1 - y2) \
             and x1 <= x2 and y1 <= y2 else print('NO')
