#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/02_closures_and_decorators/variadic_functions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # `print()` accepts variable number of positional arguments
# Have you noticed that the `print` function can accept any number of positional arguments?

# In[1]:


print(1,2,3)
print() # empty line
print(1,2,3,4,5,6,7,8,8,10)


# # What about our functions?
# 
# But our functions seem to accept *exactly* the same number of parameters as given in the function

# In[2]:


def blah(x,y):
    print(x,y)

blah(1,2)     # OK
# blah()      # ERROR: blah() missing 2 required positional arguments: 'x' and 'y'
# blah(1)     # ERROR: blah() missing 1 required positional argument: 'y'
# blah(1,2,3) # ERROR: blah() takes 2 positional arguments but 3 were given


# # variable number of positional arguments
# 
# ```
# def variadic_func1(*args):
#     pass
# ```
# if we prepend the `*` character before a name of a parameter (usually this parameter is called `*args`), then that parameter will receive all the _extra_ positional parameters.

# In[3]:


def variadic_func1(*args):
    print(type(args)) # args is a variable of type tuple
    print(args) # prints the tuple
    print(*args) # equals print(args[0], args[1], args[2], ..., args[-2], args[-1])

variadic_func1(1,2,3,4,5,6,7,"goodbye")


# # variable number of keyword arguments
# 
# have you noticed that `dict()` function can receive variable number of keyword arguments

# In[4]:


dict(
    did_you_notice="that",
    i_can="add as many",
    keyword_arguments="as I want",
    to_the_call="of this function?"
)


# we can achieve the same result too!
# ```python
# def variadic_func2(**kwargs):
#     pass 
# ```
# if we prepend the `**` character before a name of a parameter (usually this parameter is called `**kwargs`), then that parameter will receive all the extra keyword parameters.

# In[5]:


def variadic_func2(**kwargs):
    print(type(kwargs)) # kwargs is of type `dict`
    print(kwargs)       # prints the dictionary
    # print(**kwargs)   # we will demonstrate this in a different way

variadic_func2(a=1,b=2,c=3,trolololo=10)


# when used inside calling a function, the `*` and `**` operators are called the unpacking operators.
# 
# they can be used like this

# In[6]:


params = {
    'username': "jamesbond",
    'password': "007",
    'company': "mi6"
}

def connect(username, password, company):
    print(username, password, company)

# take all the key/value pairs from the `params` dict
# and use them as keyword arguments for the connect function
connect(**params) # this actually calls connect(username="jamesbond", password="007", company="mi6")


# # putting it all together
# 
# a function that receives both `*args` and `**kwargs` parameters is a fully variadic function that can receive any number of arguments, and keyword parameters of any name
# 
# ```python
# def variadic_function(*args, **kwargs):
#     pass
# ```
# 

# In[7]:


def variadic_function(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)

variadic_function(1,2,3, a=4, b=5, c=6)


# In[ ]:




