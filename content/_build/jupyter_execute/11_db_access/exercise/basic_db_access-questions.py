#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/basic_db_access-questions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # Chinook sample SQLite database
# 
# in this exercise we're going to experiment with the [Chinook sample DB](http://www.sqlitetutorial.net/sqlite-sample-database/).
# 
# ![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)
# 
# First, run the code below to download the database locally

# In[1]:


### useful: download and extract chinook sample DB
import urllib.request
import zipfile
from functools import partial
import os

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall()
assert os.path.exists('chinook.db')


# # 1. open the database
# 1. connect to the database using the `sqlite3` or `pyodbc` module interface. place the connection object in a variable named `conn`
# 2. create a cursor object and put it in the variable `cur`

# In[ ]:





# # 2. table names
# run an SQL to print out all the table names and their schema

# In[ ]:





# # 3. Tracks
# print out the first three tracks in the `tracks` table

# In[ ]:





# # 4. Albums from Tracks
# print out the track name and albums title of the first 20 tracks in the `tracks` table
# 
# 

# In[ ]:





# # 5. Tracks sold
# 
# 1. print out the first 10 track sales from the `invoice_items` table
# 2. for these first 10 sales, print what are the names of the track sold, and the quantity sold
# 

# In[ ]:





# # 6. Top tracks sold
# 
# print the names of top 10 tracks sold, and how many they times they were sold

# In[ ]:





# # 7. top selling artists
# Who are the top 10 highest selling artists?
# 
# > _hint: you need to join the invoice_items, tracks, albums and artists tables_
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# basic_db_access-solutions
# sqlalchemy_orm-questions
# sqlalchemy_orm-solutions
# ```
# 
