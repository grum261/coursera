
# coding: utf-8

# In[48]:


def move(n, start=1, finish=3):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print(n, start, finish)
        move(n - 1, temp, finish)


# In[50]:


x = int(input())
move(x)
