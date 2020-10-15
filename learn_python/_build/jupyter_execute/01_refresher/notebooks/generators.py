#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/generators.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# In[1]:


range(10**12)


# In[2]:


x = (2**i for i in range(10**12))


# In[3]:


next(x)


# In[4]:


def infinity():
    x = 0 
    while True:
        return x
        x +=1
        
z = infinity()


# In[5]:


z = infinity()


# In[6]:


def infinity():
    x = 0 
    while True:
        yield x
        x +=1


# In[7]:


z = infinity()
z


# In[8]:


next(z)


# In[9]:


z2 = infinity()


# In[10]:


next(z)


# In[11]:


next(z2)


# In[12]:


import random
def make_random_stream(n):
    for i in range(n):
        yield random.randint(0, 100)


# In[13]:


list(make_random_stream(10))


# In[14]:


z = make_random_stream(100000000000000)


# In[15]:


z


# In[16]:


def make_reader(f):
    pass

for line in make_reader(open('spam.txt')):
    print(line)


# In[36]:


from copy import deepcopy


# In[37]:


a = [[1],[2],[3] ]
b = a[:]


# In[38]:


a[0][0] = 10


# In[39]:


a


# In[40]:


b


# In[41]:


b = deepcopy(a)


# In[42]:


a[0][0] = 100


# In[43]:


a


# In[44]:


b


# In[ ]:




