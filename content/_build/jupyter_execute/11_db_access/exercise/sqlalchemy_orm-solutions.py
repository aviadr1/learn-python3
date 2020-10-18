#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/sqlalchemy_orm-solutions.ipynb" target="_blank">
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

# In[13]:


import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')
cur = engine.connect()


# > now run the code below to to run reflecton on the database, prepare classes that map to the database and create an orm session

# In[14]:


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

# In[19]:


engine.table_names()


# # 3. Tracks
# print out the first three tracks in the `tracks` table

# In[26]:


from sqlalchemy import select 
tracks = Base.classes['tracks']

# using expressions
query = select([tracks]).limit(3)
display_results(query)


# In[38]:


# using orm
results = session.query(tracks).limit(3)
display_results(results)


# # 4. Albums from Tracks
# print out the track name and albums title of the first 20 tracks in the `tracks` table
# 
# 

# In[37]:


from sqlalchemy import join
albums = Base.classes['albums']

# using expression language
query = select([tracks.Name, albums]).select_from(join(tracks, albums)).limit(20)
display_results(query)


# In[ ]:



# using orm
results = session.query(tracks.Name, albums).select_from(tracks).join(albums).limit(20)
display_results(results)


# # 5. Tracks sold
# 
# 1. print out the first 10 track sales from the `invoice_items` table
# 2. for these first 10 sales, print what are the names of the track sold, and the quantity sold
# 

# In[41]:


items = Base.classes['invoice_items']

# print out the first 10 track sales from the invoice_items table
query = select([items]).limit(10)
display_results(query)

# for these first 10 sales, print what are the names of the track sold, and the quantity sold
query = select([tracks.Name, items.Quantity]).select_from(join(items, tracks)).limit(10)
display_results(query)    


# In[42]:


# orm
result = session.query(tracks.Name, items.Quantity).select_from(items).join(tracks).limit(10)
display_results(result)


# # 6. Top tracks sold
# 
# print the names of top 10 tracks sold, and how many they times they were sold

# In[44]:


from sqlalchemy import func, column

query = select([tracks.Name, func.sum(items.Quantity).label('sold')])             .select_from(join(tracks, items))             .group_by(tracks.TrackId)             .order_by(column('sold').desc())             .limit(10)

display_results(query)


# In[49]:


# orm
results = session.query(tracks.Name, func.sum(items.Quantity).label('sold'))             .select_from(tracks)             .join(items)             .group_by(tracks.TrackId)             .order_by(column('sold').desc())             .limit(10)

display_results(results)


# # 7. top selling artists
# Who are the top 10 highest selling artists?
# 
# > _hint: you need to join the invoice_items, tracks, albums and artists tables_
# 

# In[51]:


artists = Base.classes['artists']

# solution using sqlalchemy expressions
query = select([artists.Name, func.sum(items.Quantity).label('sold')])     .select_from(join(items, tracks).join(albums).join(artists))     .group_by(artists.ArtistId)     .order_by(column('sold').desc())     .limit(10)
display_results(query)


# In[52]:



# solution using sqlalchemy orm
query = session.query(func.sum(items.Quantity).label('sold'), artists.Name.label('Artist'))     .select_from(items)     .join(tracks)     .join(albums)     .join(artists)     .group_by(artists.ArtistId)     .order_by(column('sold').desc())     .limit(10)
display_results(query)


# In[ ]:




