#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/reduce.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# In[1]:


import functools


# In[2]:


mysum = functools.partial(functools.reduce, lambda x, y: x+y)
mysum([1,2,3,2,1])


# In[3]:


mymax = functools.partial(functools.reduce, lambda x, y: x if x>=y else y)
mymax([1,2,3,2,1])


# In[4]:


myaverage = lambda list_ : mysum(list_) / len(list_)
myaverage([1,2,3])


# In[ ]:




