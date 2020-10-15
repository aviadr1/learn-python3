#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/13_complex_comprehensions/complex_comprehensions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # writing and understanding nested list comprehensions
# ![gif](https://i.stack.imgur.com/0GoV5.gif)
# 
# every once in a while, one wants to write a complex or a nested list comprehension.
# common examples are 
# 1. flattening a nested list, 
# 2. transforming a nested list
# 3. making a nested list out of a flattened one.
# 
# many people find nested list comprehensions hard to read/write at first.
# but there's a simple trick to it!
# 
# > if you can write your code using nested for loops, converting to nested list comprehensions is trivial
# 
# Here is how to convert nested for loop to nested list comprehension:
# 
# Here is how nested list comprehension works:
# 
#                 l a b c d e f
#                 ↓ ↓ ↓ ↓ ↓ ↓ ↓
#     In [1]: l = [ [ [ [ [ [ 1 ] ] ] ] ] ]
#     In [2]: for a in l:
#        ...:     for b in a:
#        ...:         for c in b:
#        ...:             for d in c:
#        ...:                 for e in d:
#        ...:                     for f in e:
#        ...:                         print(float(f))
#        ...:                         
#     1.0
#     
#     In [3]: [float(f)
#              for a in l
#        ...:     for b in a
#        ...:         for c in b
#        ...:             for d in c
#        ...:                 for e in d
#        ...:                     for f in e]
#     Out[3]: [1.0]
#     
#     #Which can be written in single line as
#     In [4]: [float(f) for a in l for b in a for c in b for d in c for e in d for f in e]
#     Out[4]: [1.0]
# 
# 
#   [1]: https://i.stack.imgur.com/0GoV5.gif

# In[1]:


prices = {
    "apple" : 14,
    "melon" : 5,
    "grapes" : 25,
    "banana" : 8
}

purchase = ['apple', 'apple', 'grapes']

# how much does it cost?
sum([prices[fruit] for fruit in purchase])


# ## Examples
# Lets see some examples

# ### create nested list
# I want to create a matrix which looks like below:
# ```
# matrix = [[0, 1, 2, 3, 4, 5]
#           [0, 1, 2, 3, 4, 5],
#           [0, 1, 2, 3, 4, 5],
#           [0, 1, 2, 3, 4, 5],
#           [0, 1, 2, 3, 4, 5]]
# ```

# In[2]:


from pprint import pprint

nrows = 5
ncols = 6

matrix = []
for i in range(nrows):
    row = []
    matrix.append(row)
    for j in range(ncols):
        row.append(j)

pprint(matrix)


# In[3]:


[[j for j in range(ncols)] for i in range(nrows)]


# ### flatten 2d list
# Suppose I want to flatten a given 2-D list:
# ```
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ```
# Expected Output: 
# ```
# flatten_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```

# In[4]:


matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]


# In[5]:


flatten_matrix = []
for row in matrix:
    for val in row:
        flatten_matrix.append(val)
        
pprint(flatten_matrix)


# In[6]:


[val for row in matrix for val in row]


# ### flatten 2d list with condition
# 
# Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:
# ```
# planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
# ```
# Expected Output: 
# ```
# flatten_planets = ['Venus', 'Earth', 'Mars', 'Pluto']
# ```

# In[7]:


planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 


# In[8]:


flatten_planets = []
for planet_group in planets:
    for planet in planet_group:
        if len(planet) < 6:
            flatten_planets.append(planet)
            
pprint(flatten_planets)


# In[9]:


[planet for planet_group in planets for planet in planet_group if len(planet) < 6]


# ### complex flattening and transform
# One final, more complex example: Let’s say that we have a list of lists of words 
# ```
# strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]
# ```
# and we want 
# 1. to get a list of all the letters of these words 
# 2. along with the index of the list they belong to 
# 3. but only for words with more than two characters. 
# 

# In[10]:


strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]


# In[11]:


output = []
for idx, group in enumerate(strings):
    for word in group:
        if len(word) > 2:
            for letter in word:
                output.append( [letter, idx])
                
pprint(output)


# In[12]:


[ [letter, idx] for idx, group in enumerate(strings) for word in group if len(word)>2 for letter in word]


# ## create groups of 3 from flat list
# given a flat list
# ```
# flat = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# ```
# group the elements into triplets and create a nested list
# ```
# nested_3s = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [9, 10, 11],
#              [12, 13, 14],
#              [15, 16, 17],
#              [18, 19    ]]
# ```

# In[13]:


flat = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# In[14]:


output = []
for i in range(0, len(flat), 3):
    triplet = flat[i:i+3]
    output.append(triplet)
    
pprint(output)


# In[15]:


[flat[i:i+3] for i in range(0, len(flat), 3) ]


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# exercise/questions
# ```
# 
