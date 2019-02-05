
# coding: utf-8

# In[29]:


p = int(input())
x = int(input())
y = int(input())

n = 0
while x < y:
   x = x + (int((p * 0.01 * x) * 100)) / 100
   n += 1
print(n)
