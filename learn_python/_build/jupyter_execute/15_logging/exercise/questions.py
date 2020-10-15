#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/15_logging/exercise/questions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # setup
# 1. import the logging module
# 2. call `.basicConfig()`
# 3. setup autoreload to help reloading .py files from disk

# In[1]:


### useful: please run this
import logging
logging.basicConfig()

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Basic
# 1. import 
# 1. Create a new python file named `ex1.py` which should:
#     1. Import the logging module
#     2. create a logger instance named `__name__`
#     3. Create a function called `say_something()` that logs a ‘warning’ message with the text: `"This a warning message!"`.
# 2. use the file
#    1. `import ex1`
#    2. call `ex1.say_something()`
# 
# 

# In[2]:





# In[2]:


### useful: run your ex1.py
import ex1
ex1.say_something()


# # Log level
# 
# 1. Create a new python file named ‘ex2.py‘ which should:
#     1. Import the logging module
#     2. create a logger instance named `__name__`
#     2. set the logger's level to `logging.DEBUG`
#     3. create a function called `say_something()` which logs an ‘info’ message with the text: “This an informative message!”.
# 2. use this file
#    1. import ex2
#    1. call `ex2.say_something()`

# In[4]:





# In[3]:


### useful: run your ex2.py
import ex2
ex2.say_something()


# # Configuration
# 1. setup
#    1. change the level of ex2's logger to DEBUG
#    2. call `ex2.say_something()` - this should write the usual output 
#    <br><br>
#    
# 1. Review this basic YAML configuration, and see that you understand how it will:
#    1. set a simple format that is the same as the default format
#    2. set a handler that logs to console
#    3. connect the root logger to the console handler, with level WARNING
#    4. modify the level for the ex2 logger to ERROR
#       ```
#       version: 1
#       disable_existing_loggers: False
#       formatters:
#         simple:
#           format: '%(levelname)s:%(name)s:%(message)s'
#       handlers:
#         console:
#           class: logging.StreamHandler
#           formatter: simple
#           stream: ext://sys.stderr
#       loggers:
#         ex2:
#           level: ERROR
#       root:
#         level: WARNING
#         handlers: [console]
#       ``` 
#       <br><br>
# 2. load this configuration
#    1. import the `yaml` module
#    2. use `yaml.load()` to read this configuration into a `dict` object
#    3. import logging.config module
#    4. use `logging.config.dictConfig()` function to load the configuration from your dict <br>
#    <br><br>
#    
# 3. execute `ex2.say_something()` again. this time there should not be any output. 
#    why?
# 
# 
# 

# In[6]:





# # Format #1
# 
# Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this
# `2019-12-26 03:07:04,560 | WARNING | ex1 | this is a warning message`
# 
# 
# hints:
# - Read the [LogRecord](https://docs.python.org/3/library/logging.html#logrecord-attributes) documentaion, which shows the attributes available for formatting
# 

# In[9]:





# # Format #2
# Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this: 
# 
# `2019-12-26 03:10:19,852 :: WARNING :: Module ex1 :: Line No 6 :: this is a warning message`

# In[11]:





# # file handler
# 
# - Use YAML configuration to
#   1. set the levels of both `ex1` and `ex2` loggers to DEBUG
#   2. setup file logging for `ex2` logger so that it writes to `ex2.log`
#   
# - test this by calling 
#   ```python
#   ex1.say_something()
#   ex2.say_something()
#   ```
#   and reading `ex2.log`
# 

# In[25]:





# In[18]:





# In[ ]:




