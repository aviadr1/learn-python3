#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/14_pandas/pandas_a_quick_tour.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# In[1]:


x=0


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('diamonds.csv')


# In[4]:


type(df)


# In[5]:


# df.head() 
df.head(10) 


# In[6]:


df.tail()


# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df['carat'].head()


# In[10]:


df[['carat', 'price']].head()
# df[  ['carat', 'price']  ].head()


# In[11]:


df.iloc[0]


# In[12]:


# df.iloc[0]['carat']
df.iloc[0][['carat', 'price']]


# In[13]:


df.iloc[:10]


# In[14]:


df.iloc[ [0, 2, 1, 0] ]


# In[15]:


row0 = df.iloc[0]
row0


# In[16]:


row0['price']


# In[17]:


row0.iloc[1]


# In[18]:


row0.loc['price']


# In[19]:


carats = df.set_index('carat')
carats.head()


# In[20]:


carats.loc[0.21]


# In[21]:


carats.info()


# In[22]:


carats.reset_index()


# In[23]:


df.head()


# In[24]:


df.head() *2


# In[25]:


(df['carat'] + 1).head()


# In[26]:


df['expensive'] = df['price'] > 1000
df.head()


# In[27]:


df.tail()


# In[28]:


def is_large(row):
    vol = row['x'] * row['y'] * row['z']
    if vol > 20:
        return "big"

    else:
        return "small"


# In[29]:


df['volume_label'] = df.apply(is_large, axis=1)
df.head()


# In[30]:


df['expensive'].replace({True: 'yes!', False: 'no...'})


# In[31]:


def depth_as_inch(row):
    inch = row['depth'] / 3
    row.drop('depth')
    return row

df.apply(depth_as_inch, axis=1)


# In[32]:


df['carat'] + 1


# In[33]:


df


# In[34]:


df.groupby('cut').mean()


# In[35]:


df.groupby('cut')[['price', 'carat']].mean()


# In[36]:


clarity_cut = df.groupby(['cut', 'clarity'])[['price', 'carat']].mean()
clarity_cut.head()


# In[37]:


clarity_cut['price'].sort_values(ascending = False)


# In[38]:


df['cut'].value_counts()


# In[39]:


df['cut'].unique()


# In[40]:


df.head()


# In[41]:


df.plot.scatter(x='x', y='y')


# In[42]:


df.plot.scatter(x='carat', y='price')


# In[43]:


df.groupby('cut')['price'].mean().plot.bar()


# In[44]:



df['cut'] = df['cut'].astype(pd.CategoricalDtype(['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], ordered=True))


# In[45]:


df.info()


# In[46]:


df.groupby('cut')['price'].mean().plot.bar()


# In[47]:


df.groupby('cut')['price'].mean().sort_values().plot.bar()


# In[48]:


mask = df['cut'] == "Ideal"
df[mask].head()


# In[49]:


mask = (df['cut'] == "Ideal") & (df['color'] == 'J')
df[mask].head()


# In[50]:


df[   (df['cut'] == "Ideal") & (df['color'] == 'J')  ].head()


# In[51]:


df[df['price'] > 1000].head()


# In[52]:


df.loc[[90, 91]]


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# edm_us_adult_census_income/questions
# ```
# 
