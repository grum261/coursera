
# coding: utf-8

# In[18]:


r = []
a, b, c, d, e = [int(input()) for i in range(5)]
for x in range(1000):
    if x != e:
        r.append((a*x**3 + b*x**2 + c*x + d)/(x - e))
print(r.count(0))
