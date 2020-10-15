#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/basic_db_access-solutions.ipynb" target="_blank">
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

# In[2]:


import sqlite3
db="chinook.db"
conn = sqlite3.connect(db)
cur = conn.cursor()


# # 2. table names
# run an SQL to print out all the table names and their schema

# In[3]:


rs = cur.execute(
    """
    SELECT name, sql FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """)
    
for name, sql, *args in rs:
    print(name)
    print(sql)
    print()


# # 3. Tracks
# print out the first three tracks in the `tracks` table

# In[4]:


rs = cur.execute(
    """
    SELECT * 
    FROM tracks
    LIMIT 3;
    """)

for row in rs:
    print(row)


# # 4. Albums from Tracks
# print out the track name and albums title of the first 20 tracks in the `tracks` table
# 
# 

# In[5]:


rs = cur.execute(
    """
    SELECT tracks.Name, albums.*
    FROM tracks
    JOIN albums ON tracks.AlbumId == albums.AlbumId
    LIMIT 20
    ;
    """)

for row in rs:
    print(row)


# # 5. Tracks sold
# 
# 1. print out the first 10 track sales from the `invoice_items` table
# 2. for these first 10 sales, print what are the names of the track sold, and the quantity sold
# 

# In[6]:


# print out the first 10 track sales from the invoice_items table
rs = cur.execute(
    """
    SELECT *
    FROM invoice_items
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)
    
print()

# what are the names of the tracks sold in the first 10 invoices?
rs = cur.execute(
    """
    SELECT tracks.Name, invoice_items.Quantity
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId 
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)


# # 6. Top tracks sold
# 
# print the names of top 10 tracks sold, and how many they times they were sold

# In[7]:


rs = cur.execute(
    """
    SELECT tracks.Name, SUM(Quantity) AS sold
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId 
    GROUP BY invoice_items.TrackId
    ORDER BY sold DESC    
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)


# # 7. top selling artists
# Who are the top 10 highest selling artists?
# 
# > _hint: you need to join the invoice_items, tracks, albums and artists tables_
# 

# In[8]:


rs = cur.execute(
    """
    SELECT artists.Name, SUM(Quantity) AS sold
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId
    JOIN albums ON tracks.AlbumId == albums.AlbumId
    JOIN artists ON albums.ArtistId == artists.ArtistId
    GROUP BY artists.ArtistId
    ORDER BY sold DESC    
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)


# In[ ]:





# In[ ]:





# In[ ]:




