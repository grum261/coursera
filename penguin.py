
# coding: utf-8

# In[2]:


peng = [
  '   _~_    ',
  '  (o o)   ',
  ' /  V  \\  ',
  '/(  _  )\\ ',
  '  ^^ ^^   '
]

request = int(input())
for i in peng:
    print(request * i, sep=' ')
