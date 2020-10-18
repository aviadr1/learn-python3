#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/generic_functions_closures.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# In[1]:


def generic_func(*args, **kwargs):
    print('the positional args are:', args)
    print('the keyword args are:', kwargs)
    


# In[2]:


generic_func()


# In[3]:


generic_func("one", "two", "three", blah=1, moshe=2, test=[1,2,3])


# In[4]:


len([1,2,3], [1,2,3])


# In[7]:


print(1,2,3,4,5,6,7,8,1,2,34,25,4,5432,5432,5432,5432,5432)


# In[15]:


def test():
    class ToldYou:
        pass
    import math
    x = 10
    def inner():
        print('in inner func')
    return inner
    


# In[23]:


def make_str_factory(s):
    
    def str_factory():
        return s
    
    return str_factory
    


# In[30]:


smiley_factory = make_str_factory('😊')
hello_factory = make_str_factory('hello')


# In[38]:


smiley_factory.__closure__


# In[31]:


dir(smiley_factory)


# In[26]:


hello_factory()


# In[27]:


class Factory:
    def __init__(self, value):
        self.value = value
        
    def make(self):
        return self.value


# In[29]:


smiley_factory = Factory('😊')
smiley_factory.make()


# In[ ]:




