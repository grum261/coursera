
# coding: utf-8

# In[10]:


a, b, c = [float(input()) for i in range(3)]

disc = b**2 - 4*a*c
if disc == 0:
    x = -b/2*a
    print(x)
elif disc > 0:
        x1, x2 = (-b + disc**0.5)/2*a, (-b - disc**0.5)/2*a
        print(*sorted((x1, x2)))
else:
    None
