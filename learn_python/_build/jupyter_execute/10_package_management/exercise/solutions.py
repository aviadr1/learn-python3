#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/10_package_management/exercise/solutions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # using new modules without polluting your system
# 
# in this exercize we're going to use `pipenv` to try out some new modules without polluting your environment

# ## start a new project called cute-python
# 
# make a new folder called cute-python

# In[1]:


# useful: current directory
import os
os.path.realpath('.')


# In[2]:


if not os.path.exists('cute-python'):
    os.mkdir('cute-python')
os.chdir('cute-python')
os.path.realpath('.')


# ## function that downloads image from web
# 
# > remember to use `pipenv` for this step
# 
# we want to download a particular image from the web: <br>
# ```https://inews.co.uk/wp-content/uploads/2018/03/Nobody-expects-the-Spanish-Inquisition_.jpg```
# 
# why not use an awesome library to perform our HTTP download for us?
# lets see if this library is indeed so awesome without affecting our whole system.
# 
# 1. use `pipenv` to install the `requests` library for the `cute-python` project
# 2. use the [requests](https://2.python-requests.org/en/master/) library to write a function that downloads the image file mentioned above to a file called `cute-python.jpg`
#    > hint: you're looking for the `requests.get()` function, <br>
#    > you need to write the _content_ to a binary file opened like this `open('cute-python.jpg', "wb")`

# In[3]:


# run this in the shell:
"""
>> pipenv install requests
"""


# In[4]:


code = """
import requests
def download():
    url = 'https://inews.co.uk/wp-content/uploads/2018/03/Nobody-expects-the-Spanish-Inquisition_.jpg'
    with open('cute-python.jpg', 'wb') as file:
        r = requests.get(url, allow_redirects=True)
        file.write(r.content)

if __name__ == '__main__':
    download()
"""
with open('download.py', 'w') as codefile:
    codefile.write(code)


# In[5]:


# run this in the shell
"""
>> pipenv shell
(cute-python) >> python download.py
"""


# # lets also show the file
# here's some code based on `matplotlib` and `pillow` modules that can show the image
# ```
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# plt.imshow(mpimg.imread('cute-python.jpg'))
# plt.show()
# ```
# 
# 1. lets use pipenv to get these two modules for our project
# 2. lets add this code to a file called `show.py` and run it
# 

# In[6]:


# run this in the shell
"""
>> pipenv install pillow matplotlib
"""


# In[7]:


code = """
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.imshow(mpimg.imread('cute-python.jpg'))
plt.show()
"""
with open('show.py', 'w') as codefile:
    codefile.write(code)


# In[8]:


# run this in the shell
"""
>> pipenv run python show.py
"""


# # what are our project's dependencies?
# 
# 1. what libraries we actuall care about did we install
# 2. what sub-dependencies were installed in addition?

# In[9]:


get_ipython().system('pipenv graph')


# 
