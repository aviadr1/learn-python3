#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/sqlalchemy_orm-questions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # Chinook sample database using SQLAlchemy
# 
# in this exercise we're going to experiment with the [Chinook sample DB](http://www.sqlitetutorial.net/sqlite-sample-database/). while using SQLAlchemy module
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


# # Helper methods
# 
# the helper methods below will help 

# In[2]:


### useful: functions for displaying results from sql queries using pandas
from IPython.display import display
import pandas as pd

def sql(query):
    print()
    print(query)
    print()

def get_results(query):
    global engine
    q = query.statement if isinstance(query, sqlalchemy.orm.query.Query) else query
    return pd.read_sql(q, engine)

def display_results(query):
    df = get_results(query)
    display(df)
    sql(query)


# # 1. open the database
# 1. open  the database using `sqlalchemy` module interface. create an engine object in a variable named `engine`
# 2. call the `connect()` method to obtain a connection and place in a variable named `cur`

# In[3]:





# > now run the code below to to run reflecton on the database, prepare classes that map to the database and create an orm session

# In[4]:


### useful: extract classes from the chinook database
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

## we need to do this once
from sqlalchemy.ext.automap import automap_base

# produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# also prepare an orm session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


# # 2. table names
# print out all the table names

# In[5]:





# # 3. Tracks
# print out the first three tracks in the `tracks` table

# In[6]:





# # 4. Albums from Tracks
# print out the track name and albums title of the first 20 tracks in the `tracks` table
# 
# 

# In[7]:





# # 5. Tracks sold
# 
# 1. print out the first 10 track sales from the `invoice_items` table
# 2. for these first 10 sales, print what are the names of the track sold, and the quantity sold
# 

# In[8]:





# # 6. Top tracks sold
# 
# print the names of top 10 tracks sold, and how many they times they were sold

# In[9]:





# # 7. top selling artists
# Who are the top 10 highest selling artists?
# 
# > _hint: you need to join the invoice_items, tracks, albums and artists tables_
# 

# In[10]:




