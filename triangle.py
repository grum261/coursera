
# coding: utf-8

# In[1]:


a, b, c = [int(input()) for i in range(3)]

if c**2 + a**2 > b**2 or a**2 + b**2 > c**2 or c**2 + b**2 > a**2:
    print('acute')
elif c**2 + a**2 < b**2 or a**2 + b**2 < c**2 or c**2 + b**2 < a**2:
    print('obtuse')
elif c**2 + a**2 == b**2 or c**2 + b**2 == a**2 or a**2 + b**2 == c**2:
    print('rectangular')
else:
    print('impossible')
