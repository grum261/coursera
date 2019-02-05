
# coding: utf-8

# In[3]:


a, b, c = [int(input()) for i in range(3)]

a *= c
b *= c

while b >= 100:
    b -= 100
    a += 1
print(a, b)
