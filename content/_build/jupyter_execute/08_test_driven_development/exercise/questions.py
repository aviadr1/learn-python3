#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/08_test_driven_development/exercise/questions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # Unit testing a contact list
# 
# The code sample below has `Contact` class that contains both a `Person` and an `Address` class, and finally, a `Notebook` class that contains multiple contacts.
# 
# Can you use `pytest` and `unittest.mock` modules to write tests for these classes and fix the bugs in this code

# In[1]:


### useful: This is the code you should test

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def __repr__(self):
        return f"Address({self.city!r}, {self.street!r})"

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email

    def __repr__(self):
        return f"Person({self.name!r}, {self.email!r})"
        
class Contact:
    def __init__(self, street, city, name, email, **kwargs):
        self.person = Person(name, email)
        self.address = Address(street, city)
    
    def __str__(self):
        return f"""        {self.person.name}:
            {self.person.email}
            address:
                {self.address.city}
                {self.address.street}
        """
        
class Notebook:
    def __init__(self):
        self.contacts = dict()

    def add(self, street, city, name, email):
        self.contacts[name] = Contact(name, email, city, street)

    def remove(name):
        self.contacts.remove(name)
        
    def __str__(self):
        results = []
        for name, contact in self.contacts.items():
            results.append(str(contact))
            results.append("")
        return '\n'.join(results)


# In[43]:





# In[2]:


### useful: run the tests you wrote
import ipytest

# enable pytest's assertions and ipytest's magics
ipytest.config(rewrite_asserts=True, magics=True)

# set the filename
__file__ = 'ex 08 - solutions.ipynb'

# execute the tests via pytest, arguments are passed to pytest
ipytest.run('-qq')


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# solutions
# ```
# 
