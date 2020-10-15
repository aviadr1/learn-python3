#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/02_sqlalchemy_orm.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # SQLAlchemy
# > SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
# 
# We're going to show how to create a database, add some data and do basic queries.
# more complex queriex, doing migrations and database admin, are outside the scope of this lesson

# ## Create a new database from scratch
# Lets create a new database from scratch. we will
# 1. Create classes to define a schema
# 2. Map the scheme to a database
# 3. add objects to the database
# 4. run queries
# 
# > NOTE: we will use an in-memory database, but running with a file based one or a remote database would be just as easy

# ### 1. Create a database session

# In[1]:


from sqlalchemy import create_engine
#engine = create_engine('sqlite:///example.db', echo=True)
engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine('sqlite:///:memory:')
conn = engine.connect()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


# ### 2. Helper functions to print SQL queries and SQL results 

# In[2]:


from IPython.display import display
import pandas as pd
import sqlalchemy

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
    #sql(query)


# ### 3.  creating a schema base

# In[3]:


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy_explore

### the basic base class for SQLAlchemy schema objects
# Base = declarative_base(bind=engine)

### base class including utils like an __repr__ method
### see https://pypi.org/project/sqlalchemy-explore/
Base = declarative_base(cls=sqlalchemy_explore.ReflectiveMixin)


# ### 4. Create the schema

# In[4]:


from sqlalchemy import Column, DateTime, ForeignKey, Integer, NVARCHAR, Numeric, Sequence
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    FirstName = Column(NVARCHAR(40), nullable=False)
    LastName = Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    Phone = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    
class Item(Base):
    __tablename__ = 'items'
    
    ItemId = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    Name = Column(NVARCHAR(40), nullable=False)
    Price = Column(Numeric, nullable=False)

class Purchase(Base):
    __tablename__ = 'purchases'
    
    PurchaseId = Column(Integer, Sequence('purchase_id_seq'), primary_key=True)
    ItemId = Column(ForeignKey('items.ItemId'), nullable=False, index=True)
    CustomerId = Column(ForeignKey('customers.CustomerId'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False)
    
    item = relationship('Item')
    customer = relationship('Customer')


# In[5]:


Purchase.ItemId.name


# ### 5. Create tables in the database to conform with the schema

# In[6]:


Base.metadata.create_all(engine)


# ### 6. Create a customer

# In[7]:


moshe = Customer(
    FirstName='Moshe', 
    LastName='Cohen', 
    Address='Alenbi 99, Tel Aviv', 
    Phone="053-5556789", 
    Email='moshe@cohen.com')

session.add(moshe)
session.commit()


# ### 7. run queries

# #### Using SQLAlchemy expression language

# In[8]:


from sqlalchemy import select 

customers_query = select([Customer.FirstName, Customer.Email])
results = conn.execute(customers_query)

print()
for row in results:
    print(row)

print()
print(type(row)) # rows are of type sqlalchemy.engine.result.RowProxy


# > Our handy `display_results` function uses `pandas` library to display the results as a table

# In[9]:


display_results(customers_query)


# #### Using SQLAlchemy ORM Object Relation Manager

# In[10]:


results = session.query(Customer)

print()
for customer in results:
    print(customer)
    
print()
print(type(customer))


# ## Reflect an existing database
# 
# When we have an existing database, and would like to start accessing this database using SQLAlchemy, we need to have classes that represent the database. 
# 
# Being good lazy programmers, we often don't want to write these classes by hand, and would like a helpful start.
# We're going to show how to create such classes from an existing database.
# 
# we will do it in two methods
# 1. use the automap class in SQLAlchemy to create dynamic classes (without source) for the db
# 2. use the `sqlacodegen` module [1] to generate source code for classes
# 
# [1]: https://pypi.org/project/sqlacodegen/
# 
# ### Chinook sample DB
# Let's download a sample database called [Chinook](http://www.sqlitetutorial.net/sqlite-sample-database/) 
# ![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)
# 
# there's a file in the `notebooks` directory called `download_chinook.py` with simple code to download this zip to the current directory. 

# > lets run `download_chinook.download` now

# In[11]:


# run this code to get the chinook database
import download_chinook
download_chinook.download()


# > Now lets connect to the database and create an `engine` variable

# In[12]:


import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')


# > lets get the list of table names from the database

# In[13]:


engine.table_names()


# ### using automap to refelect a db
# 
# We use the `automap` extension to __dynamically__ create classes for each table __at runtime__. 
# 
# - __advantage__: automap is faily easy to use, and it comes bundled in SQLAlchemy without a need for installing additional modules
# - __disadvantage__: There is no way to see the _code_ for these automap classes. we need to use the classes without seeing the code for it

# 
# > first, lets define a helper function called `automap_database()` that generates classes for us

# In[14]:


def automap_database(engine):
    ### useful: extract classes from the chinook database
    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine)

    ## we need to do this once
    from sqlalchemy.ext.automap import automap_base

    # produce a set of mappings from this MetaData.
    Base = automap_base(metadata=metadata)

    # calling prepare() just sets up mapped classes and relationships.
    Base.prepare()
    return Base


# > next, lets use the `automap_database()` function and see which classes were generated

# In[15]:


# create dynamic classes for every table using automap 
AutoMapBase = automap_database(engine)

# which classes were generated?
print('Generated the following classes:')
print('\t', ', '.join(AutoMapBase.classes.keys()))

# Let's prepare an ORM session so we can query the database based on these classes
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


# > Lastly, lets use one of these classes, see what columns it has and use it to query the database 

# In[16]:


# lets get the Album class for the albums table
Album = AutoMapBase.classes['albums']

# what columns are available in this class?
print('columns for Album class:')
print('\t', Album.__table__.columns) # 'albums.AlbumId', 'albums.Title', 'albums.ArtistId'

# lets get the first album and print it out
first_album = session.query(Album).first()
print()
print('first album:', type(first_album))
print('\t', first_album.AlbumId, first_album.Title, first_album.ArtistId)


# ### using sqlacodegen to generate classes with source code
# 
# > first, we need to install the `sqlacodegen` module

# In[17]:


pip install sqlacodegen


# > now, lets run it

# In[18]:


get_ipython().system('sqlacodegen sqlite:///chinook.db --tables albums,artists,customers,employees,genres,invoice_items,invoices,tracks')


# > We can now copy-paste the generated source for these classes into our code so we can start using it   

# In[19]:


from sqlalchemy import Column, DateTime, ForeignKey, Integer, NVARCHAR, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Artist(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Employee(Base):
    __tablename__ = 'employees'

    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(NVARCHAR(20), nullable=False)
    FirstName = Column(NVARCHAR(20), nullable=False)
    Title = Column(NVARCHAR(30))
    ReportsTo = Column(ForeignKey('employees.EmployeeId'), index=True)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60))

    parent = relationship('Employee', remote_side=[EmployeeId])


class Genre(Base):
    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class MediaType(Base):
    __tablename__ = 'media_types'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Album(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(NVARCHAR(160), nullable=False)
    ArtistId = Column(ForeignKey('artists.ArtistId'), nullable=False, index=True)

    artist = relationship('Artist')


class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(NVARCHAR(40), nullable=False)
    LastName = Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    SupportRepId = Column(ForeignKey('employees.EmployeeId'), index=True)

    employee = relationship('Employee')


class Invoice(Base):
    __tablename__ = 'invoices'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(ForeignKey('customers.CustomerId'), nullable=False, index=True)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(NVARCHAR(70))
    BillingCity = Column(NVARCHAR(40))
    BillingState = Column(NVARCHAR(40))
    BillingCountry = Column(NVARCHAR(40))
    BillingPostalCode = Column(NVARCHAR(10))
    Total = Column(Numeric(10, 2), nullable=False)

    customer = relationship('Customer')


class Track(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(200), nullable=False)
    AlbumId = Column(ForeignKey('albums.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('media_types.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('genres.GenreId'), index=True)
    Composer = Column(NVARCHAR(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    album = relationship('Album')
    genre = relationship('Genre')
    media_type = relationship('MediaType')


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(ForeignKey('invoices.InvoiceId'), nullable=False, index=True)
    TrackId = Column(ForeignKey('tracks.TrackId'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    invoice = relationship('Invoice')
    track = relationship('Track')


# > lets create a new engine and new orm session to use with this metadata (it is different from the automap metadata)

# In[20]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')
conn = engine.connect()
metadata.reflect(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


# > lets make a simple query

# In[21]:


# lets get the first album and print it out
first_track = session.query(Track).first()
print(type(first_track))
print('Song:', first_track.Name, '| Album:', first_track.album.Title, '| Artist:', first_track.album.artist.Name)


# # Further reading
# - [Toward Data Science' SQLAlchemy tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
# - [SQLAlchemy Object Relational Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
# - [SQLAlchemy Expression Language Tutorial](https://docs.sqlalchemy.org/en/13/core/tutorial.html)
# - [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
# - [sqlalchemy-explore](https://pypi.org/project/sqlalchemy-explore/)
# - Sample databases
#   - https://github.com/jpwhite3/northwind-SQLite3
#   - https://github.com/arjunchndr/Analyzing-Chinook-Database-using-SQL-and-Python

# In[ ]:




