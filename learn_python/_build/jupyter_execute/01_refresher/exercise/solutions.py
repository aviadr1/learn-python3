#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/exercise/solutions.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # multi-level sorting
# 
# here's a list of fruits and their prices:
# 
# ```
# prices = {
#     'apple' : 20, 
#     'melon' : 7,
#     'peach' : 20,
#     'grapes' : 25,
#     'watermelon' : 5,
#     'apricot' : 7,
#     'citrus' : 5
# }
# fruits_in_store = list(prices.keys())
# ```
# can you use the function `sorted` to `fruits_in_store` first by price and then by alphabetical order?
# 

# In[1]:


### useful
prices = {
    'apple' : 20, 
    'melon' : 7,
    'peach' : 20,
    'grapes' : 25,
    'watermelon' : 5,
    'apricot' : 7,
    'citrus' : 5
}
fruits_in_store = list(prices.keys())


# In[2]:


# solution 1
def getprice(fruit):
    return prices[fruit]

def price_and_name(fruit):
    return (prices[fruit], fruit)

sorted(fruits_in_store, key=price_and_name)


# In[3]:


# solution 2
def identity(fruit):
    return fruit

def make_sorter(key_funcs):
    def sort_key(fruit):
        return tuple(key(fruit) for key in key_funcs)
    return sort_key

sorted(fruits_in_store, key=make_sorter([len, getprice, identity]))
    


# # count repeating words in a song
# 
# Count the number of times each word appears in this short song 
# ```
# song = """\
# Lovely Spam! Wonderful Spam!
# Lovely Spam! Wonderful Spam
# Spa-a-a-a-a-a-a-am
# Spa-a-a-a-a-a-a-am
# Spa-a-a-a-a-a-a-am
# Spa-a-a-a-a-a-a-am
# Lovely Spam! (Lovely Spam!)
# Lovely Spam! (Lovely Spam!)
# Lovely Spam!
# Spam, Spam, Spam, Spam!
# """
# ```
# 
# you may find certain classes in the module `collections` useful

# In[4]:


song = """Lovely Spam! Wonderful Spam!
Lovely Spam! Wonderful Spam
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Lovely Spam! (Lovely Spam!)
Lovely Spam! (Lovely Spam!)
Lovely Spam!
Spam, Spam, Spam, Spam!
"""
song = song.translate(song.maketrans('', '', ',.!()')) # remove annoying chars
words = song.split()
from pprint import pprint

def order_by_value(d):
    return dict(sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True))

# solution #1
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] +=1
pprint(order_by_value(counter))
print()

# solution #2
counter = {}
for word in words:
    counter[word] = 1+ counter.get(word, 0)
pprint(order_by_value(counter))
print()

# solution #3
import collections
counter = collections.defaultdict(int)
for word in words:
    counter[word] +=1
pprint(order_by_value(counter))
print()

# solution #4
counter = collections.Counter(words)
pprint(order_by_value(counter))
print()


# # file read generator
# how is it that we can iterate over lines in a file with a for loop?
# in this exercize we will write a generator function that shows how this works in practice.
# 
# write a function called `def make_file_reader(f):` that can be used in the following manner:
# ```
# for line in make_file_reader(open('spam.txt')):
#     print(line)
# ```
# 
# the `make_file_reader` function should take very little time/memory to run, 
# regardless of how big the file is. the file could potentially be 1000GB or more and still take only milliseconds to run.
# 
# you are only allowed to use the function `f.readline()` on file objects.
# 
# 

# In[5]:


def make_file_reader(f):
    line = None
    while line != "":
        line = f.readline()
        yield line


# In[6]:


### useful test for your make_file_reader()
with open('spam.txt', 'w') as f: print(song, file=f)

for line in make_file_reader(open('spam.txt')):
    print(line, end='')

