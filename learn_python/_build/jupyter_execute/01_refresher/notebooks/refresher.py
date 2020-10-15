#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/refresher.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# In[1]:


x = 10


# In[2]:


x


# In[3]:


y= 20
y
x


# In[4]:


for i in range(10):
    print(i)


# In[5]:


x = 100


# In[6]:


print(x)


# In[7]:


x = [1,2,3]
x.append(4)
x = x* 2
print(x)


# In[8]:


prices = {
    'pizza' : 45,
    'hamburger' : 59,
    'salad' : 33,
    'dessert' : 25,
    'soup' : 30,
    'pie' : 32
}

order = ['pizza', 'pizza', 'salad', 'dessert']


# In[9]:


sum = 0
for item in order:
    sum+=prices[item]
print(sum)


# In[10]:


sum( [prices[item] for item in order] )


# In[5]:


i=0
while i<8:
    print(2**i)
    i+=1


# In[6]:


for i in range(8):
    print(2**i)


# In[7]:


newlist = []
for i in range(8):
    newitem = 2**i
    newlist.append(newitem)


# In[8]:


newprices = { item : prices[item] * 2 for item in prices}
print(newprices)


# In[9]:


prices.items()


# In[13]:


item = ('pizza', 45)
name = item[0]
price = item[1]


# In[14]:


name, price = ('pizza', 45)
print(name, price)


# In[15]:


name2, price2 = item
print(name2, price2)


# In[17]:


for name, price in prices.items():
     print(name, '-->>', price)
    

newprices = { name : price * 2 for name, price in prices.items()}
print(newprices)


# In[18]:


order


# In[19]:


order[2:]


# In[20]:


order[:3]


# In[21]:


order[::-1]


# In[22]:


x = 10
y = x
x += 1
print(y)


# In[23]:


x = [1,2,3]
y = x
x += [4]
print(y)


# In[24]:


{
    1 :  []
}


# In[25]:


{
    [] : 1
}


# In[26]:


2/3


# In[27]:


2//3


# In[28]:


float(2)


# In[29]:


list(range(10))


# In[30]:


int("42")


# In[31]:


str(42)


# In[32]:


[]


# In[33]:


[]


# In[34]:


()


# In[35]:


(2)


# In[36]:


(1,2,3)


# In[37]:


(1,2)


# In[38]:


(1,)


# In[39]:


1,


# In[44]:


x = 10
y = 'blah'


# In[41]:


z = x
x = y
y = x


# In[50]:


x, y = y, x
print(x,y)


# In[51]:


order


# In[52]:


order[0]


# In[53]:


order[1]


# In[54]:


order[-1]


# In[55]:


order[-2]


# In[56]:


order[-2 + len(order)]


# In[57]:


len(order)


# In[59]:


order[-10]


# In[60]:


order[-3:]


# In[61]:


order


# In[62]:


'hello ' * 3


# In[63]:


[1] * 3


# In[67]:


m = [ [ 0, 0, 0 ] ]* 3


# In[68]:


m


# In[69]:


m[0][0] = 99
print(m)


# In[70]:


x = [1,2,3, 2, 1]
sorted(x)


# In[71]:


x


# In[72]:


x.sort()
print(x)


# In[87]:


fruits = ['watermelon', 'apple', 'grapes', 'melon', 'peach', 'citrus']


# In[74]:


sorted(fruits)


# In[75]:


len


# In[76]:


sorted(fruits, key=len)


# In[89]:


prices = {
    'apple' : 20, 
    'melon' : 7, 
    'peach' : 12,
    'grapes' : 25,
    'watermelon' : 5,
    'citrus' : 5
}


# In[78]:


def getprice(fruit):
    return prices[fruit]


# In[90]:


sorted(fruits, key=getprice)


# In[80]:


[1] < [2, 2]


# In[81]:


[2] < [1, 1]


# In[83]:


[2] < [10,1] 


# In[85]:


[10, 2, 1000] < [10,100, 0] 


# In[91]:


int


# In[92]:


x = int


# In[93]:


int = float


# In[94]:


int(10)


# In[95]:


type(10)


# In[96]:


int = type(10)


# In[98]:


a = len


# In[99]:


a


# In[100]:


len = 10


# In[101]:


len("hello")


# In[102]:


len = print


# In[103]:


len("hello")


# In[104]:


import math


# In[105]:


math


# In[106]:


x = math


# In[107]:


x


# In[108]:


del x


# In[109]:


len = a


# In[110]:


len('hello')


# In[111]:


a = {"hello"}


# In[112]:


a


# In[114]:


a += {'hello', 'world' }


# In[129]:


a = set()
x = """hello"""
a.update({x})
print(a)


# In[120]:


a


# In[130]:


x = 10


# In[131]:


x < 20


# In[132]:


x == [1,2,3]


# In[133]:


bool(10)


# In[134]:


bool(0)


# In[135]:


bool([0])


# In[136]:


bool([])


# In[137]:


result = []


# In[138]:


if result :
    print("got results")
else:
    print('failed | empty result | eof | eos')


# In[139]:


bool(result)


# In[140]:


score = 87
if score > 0 and score < 100:
    print('yes')


# In[142]:


if 0<score<100<score**2< 10000:
    print('yes')


# In[144]:


x = "hello"
y = "HELLO".lower()
z = "hel" + "lo"
x == y == z == 'moshe'


# In[145]:


2 in [1,2,3]


# In[146]:


0 in [1,2,3]


# In[147]:


fruits


# In[148]:


"melon" in fruits


# In[150]:


"car" in fruits


# In[151]:


"car" not in fruits


# In[152]:


max


# In[153]:


min


# In[154]:


sum


# In[155]:


all


# In[156]:


any


# In[157]:


all([1, [2], "3"])


# In[158]:


all([1, [2], "3", 0])


# In[159]:


all([1, [2], "3", ""])


# In[160]:


fruits


# In[161]:


prices


# In[167]:


[ { 
    'name' : fruit, 
    'price' : prices[fruit], 
    '+vat' : prices[fruit]*1.17
  } 
    for fruit in fruits]


# In[170]:


[ [fruit, prices[fruit]] for fruit in fruits if prices[fruit] <= 10]


# In[171]:


def make_price_pair(fruit):
    return [fruit, prices[fruit]]


# In[172]:


make_price_pair('melon')


# In[176]:


list(map(make_price_pair, fruits))


# In[177]:


[ [fruit, prices[fruit]] for fruit in fruits ]


# In[178]:


def keep_cheap_fruits(fruit):
    return prices[fruit] <= 10


# In[180]:


list(filter(keep_cheap_fruits, fruits))


# In[182]:


[ [fruit, prices[fruit]] for fruit in fruits if prices[fruit] <= 10 and len(fruit)<= 5]


# In[190]:


matrix = []
for i in range(1, 6):
    row = []
    matrix.append(row)
    for j in range(1, 11):
        row.append(i*j)

from pprint import pprint        
pprint(matrix)
    


# In[191]:


[ [i*j for i in range(1, 6)] for j in range(1, 11) ]


# In[193]:


matrix


# In[197]:


[ matrix[i][j] for i in range(5) for j in range(10)]


# In[199]:


list(map(len, fruits))


# In[201]:


list(reversed(fruits))


# In[204]:


enumerate(fruits)


# In[207]:


range(10**12)


# In[209]:


fruit_iterator = reversed(fruits)


# In[217]:


next(fruit_iterator)


# In[211]:


fruits


# In[218]:


for fruit in reversed(fruits):
    print(fruit)


# In[219]:


dir(fruit_iterator)


# In[223]:


a = range(10)
b = a.__iter__()
next(b)


# In[228]:


list(reversed(fruits))


# In[229]:


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


# In[230]:


with open('spam.txt', 'w') as f:
    print(song, file=f)


# In[232]:


import os
os.system('spam.txt')


# In[233]:


fin = open('spam.txt')


# In[234]:


next(fin)


# In[235]:


next(fin)


# In[236]:


for line in fin:
    print(line)


# In[237]:


reduce


# In[238]:


for line in open('spam.txt'):
    print(line)


# In[ ]:




