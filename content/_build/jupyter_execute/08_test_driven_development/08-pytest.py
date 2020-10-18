#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/08_test_driven_development/08-pytest.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # useful resources:
# 1. https://stackabuse.com/test-driven-development-with-pytest/
# 2. https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery
# 3. https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
# 4. https://github.com/vanzaj/tdd-pytest/blob/master/docs/tdd-pytest/content/tdd-basics.md
# 5. https://opensource.com/article/18/6/pytest-plugins
# 
# 

# # setup

# 1. install `pytest`
# 2. install `pytest-sugar` which will give us nicer output

# In[1]:


pip -q install pytest pytest-sugar


# In[2]:


# move to tdd directory
from pathlib import Path
if Path.cwd().name != 'tdd':
    get_ipython().run_line_magic('mkdir', 'tdd')
    get_ipython().run_line_magic('cd', 'tdd')

get_ipython().run_line_magic('pwd', '')


# In[3]:


# cleanup all files
get_ipython().run_line_magic('rm', '*.py')


# # How pytest discovers tests
# 
# pytests uses the following [conventions](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery) to automatically discovering tests:
#   1. files with tests should be called `test_*.py` or `*_test.py `
#   2. test function name should start with `test_`
# 
# 
# 

# # our first test
# to see if our code works, we can use the `assert` python keyword. pytest adds hooks to assertions to make them more useful

# In[215]:


get_ipython().run_cell_magic('file', 'test_math.py', '\nimport math\ndef test_add():\n    assert 1+1 == 2\n\ndef test_mul():\n    assert 6*7 == 42\n\ndef test_sin():\n    assert math.sin(0) == 0')


# now lets run pytest

# In[216]:


get_ipython().system('python -m pytest test_math.py ')


# Great! we just wrote 3 tests that shows that basic math still works
# 
# Hurray!

# ## your turn
# 
# write a test for the following function. 
# 
# if there is a bug in the function, fix it
# 

# In[221]:


get_ipython().run_cell_magic('file', 'make_triangle.py', '\n# version 1\n\ndef make_triangle(n):\n    """\n    draws a triangle using \'@\' letters\n    for instance:\n        >>> print(\'\\n\'.join(make_triangle(3))\n        @\n        @@\n        @@@\n    """\n\n    for i in range(n):\n        yield \'@\' * i')


# ## solution
# 

# In[238]:


get_ipython().run_cell_magic('file', 'test_make_triangle.py', '\nfrom make_triangle import make_triangle\n\ndef test_make_triangle():\n    expected = "@"\n    actual = \'\\n\'.join(make_triangle(1))\n    assert actual == expected')


# In[239]:


get_ipython().system('python -m pytest test_make_triangle.py')


# so the expected starts with `'@'` and the actual starts with `''` ...
# 
# this is a bug! lets fix the code and re-run

# In[33]:


get_ipython().run_cell_magic('file', 'make_triangle.py', '\n# version 2 \ndef make_triangle(n):\n    """\n    draws a triangle using \'@\' letters\n    for instance:\n        >>> print(\'\\n\'.join(make_triangle(3))\n        @\n        @@\n        @@@\n    """\n\n    for i in range(1, n+1):\n        yield \'@\' * i')


# In[34]:


get_ipython().system('python -m pytest test_make_triangle.py')


# # Pytest context-sensitive comparisons
# [Reference](https://docs.pytest.org/en/3.0.1/assert.html#making-use-of-context-sensitive-comparisons)
# 
# pytest has rich support for providing context-sensitive information when it encounters comparisons. 
# 
# Special comparisons are done for a number of cases:
# - comparing long strings: a context diff is shown
# - comparing long sequences: first failing indices
# - comparing dicts: different entries
# 
# Here's how this looks like for set:

# In[217]:


get_ipython().run_cell_magic('file', 'test_compare_fruits.py', "def test_set_comparison():\n    set1 = set(['Apples', 'Bananas', 'Watermelon', 'Pear',  'Guave', 'Carambola', 'Plum'])\n    set2 = set(['Plum', 'Apples', 'Grapes', 'Watermelon','Pear', 'Guave', 'Carambola',  'Melon' ])\n    assert set1 == set2")


# In[218]:


get_ipython().system('python -m pytest test_compare_fruits.py')


# ## your turn
# 
# test the following function `count_words()` and fix any bugs.
# 
# the expected output from the function is given in `expected_output`

# In[ ]:


expected_output = {
 'and': 2,
 'chief': 2,
 'didnt': 1,
 'efficiency': 1,
 'expected': 1,
 'expects': 1,
 'fear': 2,
 'i': 1,
 'inquisition': 2,
 'is': 1,
 'no': 1,
 'one': 1,
 'our': 1,
 'ruthless': 1,
 'spanish': 2,
 'surprise': 3,
 'the': 2,
 'two': 1,
 'weapon': 1,
 'weapons': 1,
 'well': 1}


# In[272]:


get_ipython().run_cell_magic('file', 'spanish_inquisition.py', '# version 1: buggy\nimport collections\n\nquote = """\nWell, I didn\'t expected the Spanish Inquisition ...\nNo one expects the Spanish Inquisition!\nOur chief weapon is surprise, fear and surprise;\ntwo chief weapons, fear, surprise, and ruthless efficiency! \n"""\n\ndef remove_punctuation(quote):\n    quote.translate(str.maketrans(\'\', \'\', "\',.!?;")).lower()\n    return quote\n\ndef count_words(quote):\n    quote = remove_punctuation(quote)\n    return dict(collections.Counter(quote.split(\' \')))')


# ## solution
# 
# 

# In[267]:


get_ipython().run_cell_magic('file', 'test_spanish_inquisition.py', "\nfrom spanish_inquisition import *\n\nexpected_output = {\n 'and': 2,\n 'chief': 2,\n 'didnt': 1,\n 'efficiency': 1,\n 'expected': 1,\n 'expects': 1,\n 'fear': 2,\n 'i': 1,\n 'inquisition': 2,\n 'is': 1,\n 'no': 1,\n 'one': 1,\n 'our': 1,\n 'ruthless': 1,\n 'spanish': 2,\n 'surprise': 3,\n 'the': 2,\n 'two': 1,\n 'weapon': 1,\n 'weapons': 1,\n 'well': 1}\n\ndef test_spanish_inquisition():\n    actual = count_words(quote)\n    assert actual == expected_output")


# In[269]:


get_ipython().system('python -m pytest -vv test_spanish_inquisition.py')


# In[274]:


get_ipython().run_cell_magic('file', 'spanish_inquisition.py', '# version 2: fixed\nimport collections\n\nquote = """\nWell, I didn\'t expected the Spanish Inquisition ...\nNo one expects the Spanish Inquisition!\nOur chief weapon is surprise, fear and surprise;\ntwo chief weapons, fear, surprise, and ruthless efficiency! \n"""\n\ndef remove_punctuation(quote):\n    # quote.translate(str.maketrans(\'\', \'\', "\',.!?;")).lower() # BUG: missing return\n    return quote.translate(str.maketrans(\'\', \'\', "\',.!?;")).lower()\n\ndef count_words(quote):\n    quote = remove_punctuation(quote)\n    # return dict(collections.Counter(quote.split(\' \'))) # BUG\n    return dict(collections.Counter(quote.split()))')


# In[275]:


get_ipython().system('python -m pytest -vv test_spanish_inquisition.py')


# # Using fixtures to simplify tests
# 
# 

# ## Motivating example
# 
# Lets look at an example of class `Person`, where each person has a name and remembers their friends.

# In[147]:


get_ipython().run_cell_magic('file', 'person.py', "\n#version 1\nclass Person:\n    def __init__(self, name, favorite_color, year_born):\n        self.name = name\n        self.favorite_color = favorite_color\n        self.year_born = year_born\n        self.friends = set()\n\n    def add_friend(self, other_person):\n        if not isinstance(other_person, Person): raise TypeError(other_person, 'is not a', Person)\n        self.friends.add(other_person)\n        other_person.friends.add(self)\n\n    def __repr__(self):\n        return f'Person(name={self.name!r}, '  \\\n               f'favorite_color={self.favorite_color!r}, ' \\\n               f'year_born={self.year_born!r}, ' \\\n               f'friends={[f.name for f in self.friends]})'")


# Lets write a test for `add_friend()` function.
# 
# notice how the setup for the test is taking so much of the function, while also requiring _inventing_ a lot of repetitious data
# 
# is there a way to reduce this boiler plate code

# In[83]:


get_ipython().run_cell_magic('file', 'test_person.py', "\nfrom person import Person\n\ndef test_name():\n    # setup\n    terry = Person(\n        'Terry Gilliam',\n        'red',\n        1940\n        )\n    \n    # test\n    assert terry.name == 'Terry Gilliam' \n\n\ndef test_add_friend():\n    # setup for the test \n    terry = Person(\n        'Terry Gilliam',\n        'red',\n        1940\n        )\n    eric = Person(\n        'Eric Idle',\n        'blue',\n        1943\n        )\n    \n    # actual test\n    terry.add_friend(eric)\n    assert eric in terry.friends\n    assert terry in eric.friends")


# In[85]:


get_ipython().system('python -m pytest -q test_person.py')


# ## Fixtures to the rescue
# 
# 

# 
# what is we had a magic factory that can conjure up a name, favorite color and birth year?
# 
# then we could write our `test_name()` more simply like this:
# 
# ```python
# def test_name(person_name, favorite_color, birth_year):
#     person = Person(person_name, favorite_color, birth_year)
#     
#     # test
#     assert person.name == person_name 
# ```
# 

# furthermore, if we had a magic factory that can create `terry` and `eric` we could write our `test_add_friend()` function like this:
# 
# ```python
# def test_add_friend(eric, terry):
#     eric.add_friend(terry)
#     assert eric in terry.friends
#     assert terry in eric.friends
# ```
# 

# fixtures in `pytest` allow us to create such magic factories using the `@pytest.fixture` notation.
# 
# here's an example:

# In[6]:


get_ipython().run_cell_magic('file', 'test_person_fixtures1.py', "\nimport pytest\nfrom person import Person\n\n@pytest.fixture\ndef person_name():\n    return 'Terry Gilliam'\n\n@pytest.fixture\ndef birth_year():\n    return 1940\n\n@pytest.fixture\ndef favorite_color():\n    return 'red'\n\ndef test_person_name(person_name, favorite_color, birth_year):\n    person = Person(person_name, favorite_color, birth_year)\n \n    # test\n    assert person.name == person_name ")


# In[7]:


get_ipython().system('python -m pytest test_person_fixtures1.py')


# what's happening here?
# 
# `pytest` sees that the test function `test_person_name(person_name, favorite_color, birth_year)` requires three parameters, and searches for fixtures annotated with `@pytest.fixture` with the same name.
# 
# when it finds them, it calls these fixtures on our behalf, and passes the return value as the parameter. in effect, it calls
# 
# ```python
# test_person_name(person_name=person_name(), favorite_color=favorite_color(), birth_year=birth_year()
# ```
# 
# note how much code this saves

# ## your turn
# 1. rewrite the `test_add_friend` function to accept two parameters `def test_add_friend(eric, terry)` 
# 2. write fixtures for eric and terry
# 3. run pytest

# ## solution
# 

# In[8]:


get_ipython().run_cell_magic('file', 'test_person_fixtures2.py', "\nimport pytest\nfrom person import Person\n\n@pytest.fixture\ndef eric():\n    return Person('Eric Idle', 'red', 1943)\n\n@pytest.fixture\ndef terry():\n    return Person('Terry Gilliam', 'blue', 1940)\n\ndef test_add_friend(eric, terry):\n    eric.add_friend(terry)\n    assert eric in terry.friends\n    assert terry in eric.friends\n    ")


# In[9]:


get_ipython().system('python -m pytest -q test_person_fixtures2.py')


# # parameterizing fixtures
# 
# Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i. e. the tests that depend on this fixture. 
# 
# Test functions usually do not need to be aware of their re-running. Fixture parametrization helps to write exhaustive functional tests for components which themselves can be configured in multiple ways.
# 
# 

# In[48]:


get_ipython().run_cell_magic('file', 'test_primes.py', '\nimport pytest\nimport math\n\ndef is_prime(x):\n    return all(x % factor != 0 for factor in range(2, int(x/2)))\n\n@pytest.fixture(params=[2,3,5,7,11, 13, 17, 19, 101])\ndef prime_number(request):\n    return request.param\n\ndef test_prime(prime_number):\n    assert is_prime(prime_number) == True')


# In[49]:


get_ipython().system('python -m pytest --verbose test_primes.py')


# ## your turn
# 
# test `is_prime()` for non prime numbers
# > bonus: can you find and fix the bug in `is_prime()` using a test?

# ## solution

# In[55]:


get_ipython().run_cell_magic('file', 'test_non_primes.py', '\nimport pytest\n\nFIX_BUG = True\nif FIX_BUG:\n    def is_prime_fixed(x):\n        # notice the +1 - it is important when x=4\n        return all(x % factor != 0 for factor in range(2, int(x/2) + 1))\n    is_prime = is_prime_fixed\nelse:\n    from test_primes import is_prime\n\n@pytest.fixture(params=[4, 6, 8, 9, 10, 12, 14, 15, 16, 28, 60, 100])\ndef non_prime_number(request):\n    return request.param\n\ndef test_non_primes(non_prime_number):\n    assert is_prime(non_prime_number) == False')


# In[56]:


get_ipython().system('python -m pytest --verbose test_non_primes.py')


# In[41]:


all([factor for factor in range(2, int(4/2))])


# In[36]:


get_ipython().system('python -m pytest --verbose test_primes.py')


# 

# # printing and logging within tests
# 

# ## printing
# [Reference](https://docs.pytest.org/en/latest/capture.html)
# 
# You can use prints within tests to provide additional debug info.
# 
# pytest redirects the output and captured the output of each test. it then:
# - __suppresses__ the output of all __successful__ tests (for brevity)
# - __shows__ the output off all __failed__ tests (for debugging)
# - both `stdout` and `stderr` are captured
# 

# In[74]:


get_ipython().run_cell_magic('file', 'test_prints.py', 'import sys\n\ndef test_print_success():\n    print(\n        """\n        @@@@@@@@@@@@@@@\n        this statement will NOT be printed\n        @@@@@@@@@@@@@@@\n        """\n    )\n\n    assert 6*7 == 42\n\ndef test_print_fail():\n\n    print(\n        """\n        @@@@@@@@@@@@@@@\n        this statement WILL be printed\n        @@@@@@@@@@@@@@@\n        """\n    )\n    assert True == False\n\n\ndef test_stderr_capture_success():\n    print(\n        """\n        @@@@@@@@@@@@@@@\n        this STDERR statement will NOT be printed\n        @@@@@@@@@@@@@@@\n        """, \n        file=sys.stderr\n    )\n     \n    assert True\n\n\ndef test_stderr_capture_fail():\n    print(\n        """\n        @@@@@@@@@@@@@@@\n        this STDERR statement WILL be printed\n        @@@@@@@@@@@@@@@\n        """, \n        file=sys.stderr\n    )\n     \n    assert False')


# In[75]:


get_ipython().system('python -m pytest -q test_prints.py')


# ## logging
# [Reference](https://docs.pytest.org/en/latest/logging.html)
# 
# pytest captures log messages of level WARNING or above automatically and displays them in their own section for each failed test in the same manner as captured stdout and stderr.
# 
# - WARNING and above will displayed for failed tests
# - INFO and below will not be displayed
# 
# example:

# In[90]:


get_ipython().run_cell_magic('file', 'test_logging.py', "\nimport logging\n\nlogger = logging.getLogger(__name__)\n\ndef test_logging_warning_success():\n    logger.warning('\\n\\n @@@ this will NOT be printed \\n\\n')\n    assert True\n\ndef test_logging_warning_fail():\n    logger.warning('\\n\\n @@@ this WILL be printed @@@ \\n\\n')\n    assert False\n\ndef test_logging_info_fail():\n    logger.info('\\n\\n @@@ this will NOT be printed @@@ \\n\\n')\n    assert False")


# In[91]:


get_ipython().system('python -m pytest test_logging.py')


# ## your turn
# 
# We give below an implementation of the _FizzBuzz_ puzzle:
# > Write a function that returns the numbers from 1 to 100. But for multiples of three returns “Fizz” instead of the number and for the multiples of five returns “Buzz”. For numbers which are multiples of both three and five return “FizzBuzz”.
# 
# thus this SHOULD be true
# ```python
# >>> fizzbuzz() # should return the following (abridged) output
# [1, 2, 'Fizz', 4, 'Buzz', 6, 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', ... ]
# ```
# 
# BUT the implementation is buggy. can you write tests for it and fix it?
# 

# In[99]:


get_ipython().run_cell_magic('file', 'fizzbuzz.py', '\ndef is_multiple(n, divisor):\n    return n % divisor == 0\n\ndef fizzbuzz():\n    """\n    expected output: list with elements numbers \n        [1, 2, \'Fizz\', 4, \'Buzz\', 6, 7, 8, \'Fizz\', \'Buzz\', 11, \'Fizz\', 13, 14, \'FizzBuzz\', ... ]\n    """\n    result = []\n    for i in range(100):\n        if is_multiple(i, 3):\n            return "Fizz"\n        elif is_multiple(i, 5):\n            return "Buzz"\n        elif is_multiple(i, 3) and is_multiple(i, 5):\n            return "FizzBuzz"\n        else:\n            return i\n    \n    return result')


# ## solution
# 

# In[129]:


get_ipython().run_cell_magic('file', 'test_fizzbuzz.py', '\nFIX_BUG = 1\nif not FIX_BUG:\n    from fizzbuzz import fizzbuzz\nelse:\n    def fizzbuzz_fixed():\n        def translate(i):\n            if i%3 == 0 and i%5 == 0:\n                return "FizzBuzz"\n            elif i%3 == 0:\n                return "Fizz"\n            elif i%5 == 0:\n                return "Buzz"\n            else:\n                return i\n\n        return [translate(i) for i in range(1, 100+1)]\n\n    fizzbuzz = fizzbuzz_fixed\n\n\nimport pytest\n@pytest.fixture\ndef fizzbuzz_result():\n    result = fizzbuzz()\n    print(result)\n    return result\n\n@pytest.fixture\ndef fizzbuzz_dict(fizzbuzz_result):\n    return dict(enumerate(fizzbuzz_result, 1))\n\ndef test_fizzbuzz_len(fizzbuzz_result):\n    assert len(fizzbuzz_result) == 100\n\ndef test_fizzbuzz_len(fizzbuzz_result):\n    assert type(fizzbuzz_result) == list\n\ndef test_fizzbuzz_first_element(fizzbuzz_dict):\n    assert fizzbuzz_dict[1] == 1\n\ndef test_fizzbuzz_3(fizzbuzz_dict):\n    assert fizzbuzz_dict[3] == \'Fizz\'\n\ndef test_fizzbuzz_5(fizzbuzz_dict):\n    assert fizzbuzz_dict[5] == \'Buzz\'\n\ndef test_fizzbuzz_15(fizzbuzz_dict):\n    assert fizzbuzz_dict[15] == \'FizzBuzz\'\n\n')


# In[130]:


get_ipython().system('python -m pytest test_fizzbuzz.py')


# # float: when things are (almost) equal
# [Reference](https://docs.pytest.org/en/latest/reference.html#pytest-approx)
# 
# consider the following code, what do you expect the result to be?
# ```
# x = 0.1 + 0.2
# y = 0.3
# print('x == y', x ==y) # what will it print?
# ```

# In[133]:


x = 0.1 + 0.2
y = 0.3
print('x == y:', x == y) # what will it print?


# if you had anticipated `True` it means you haven't tried testing code with `float` data yet

# In[135]:


print(x, '!=', y)


# the issue is that float is _approxiamtely_ accurate (enough for most calculations) but may have small rounding errors.
# 
# here'e a common but ugly way to test for float equivalence

# In[136]:


abs((0.1 + 0.2) - 0.3) < 1e-6


# here's a more pythonic and pytest-tic way, using `pytest.approx`

# In[137]:


from pytest import approx
0.1 + 0.2 == approx(0.3)


# ## your turn
# 

# 
# test that 
# - `math.sin(0) == 0`, 
# - `math.sin(math.pi / 2) == 1`
# - `math.sin(math.pi) == 0`
# - `math.sin(math.pi * 3/2) == -1`
# - `math.sin(math.pi * 2) == 0`

# ## solution

# In[143]:


get_ipython().run_cell_magic('file', 'test_sin.py', '\nfrom pytest import approx\nimport math\ndef test_sin():\n    assert math.sin(0) == 0\n    assert math.sin(math.pi / 2) == 1\n    assert math.sin(math.pi) == approx(0)\n    assert math.sin(math.pi * 3/2) == approx(-1)\n    assert math.sin(math.pi * 2) == approx(0)')


# In[142]:


get_ipython().system('python -m pytest test_sin.py')


# # adding timeouts to tests
# [Reference](https://pypi.org/project/pytest-timeout/)
# 
# Sometimes code gets stuck in an infinite loop, or waiting for a response from a server.
# Sometimes, tests that run too long is in _itself_ an indication of failure.
# 
# how can we add timeouts to tests to avoid getting stuck?
# the package `pytest-timeout` solves for that by providing a plugin to pytest.
# 
# 1. install the package using `pip install pytest-timeout` 
# 2. you can set timeouts individually on tests by marking them with the `@pytest.mark.timeout(timeout=60)` decorator
# 3. you can set the timeout for all tests globally by using the timeout commandline parameter for pytest, like so:`pytest --timeout=300`

# In[ ]:


pip install -q pytest-timeout


# In[171]:


get_ipython().run_cell_magic('file', 'test_timeouts.py', "\nimport pytest\n\n@pytest.mark.timeout(5)\ndef test_infinite_sleep():\n    import time\n    while True:\n        time.sleep(1)\n        print('sleeping ...') \n\ndef test_empty():\n    pass")


# In[212]:


get_ipython().system('python -m pytest --verbose test_timeouts.py')


# notice how the `test_empty` test still runs and passes, even though the previous test was aborted

# ## your turn
# 
# 1. use the `requests` module to `.get()` the url http://httpstat.us/101 and call `.raise_for_status()`
# 2. since this will hang forever, use a timeout on the test so that it fails after 5 seconds
# 3. since the test is guranteed to fail, mark it with the `xfail` (_expected fail_) annotation `@pytest.mark.xfail(reason='timeout')`
# 
# 

# In[196]:


get_ipython().run_cell_magic('file', 'test_http101_timeout.py', "\nimport pytest\nimport requests\n\n@pytest.mark.xfail(reason='timeout')\n@pytest.mark.timeout(2)\ndef test_http101_timeout():\n    response = requests.get('http://httpstat.us/101')\n    response.raise_for_status()")


# In[211]:


get_ipython().system('python -m pytest test_http101_timeout.py')


# # testing for exceptions
# [Reference](https://docs.pytest.org/en/3.0.1/assert.html#assertions-about-expected-exceptions)
# 
# consider the following code fragment from `person.py`:
# 
# ```python
# class Person:
#     def add_friend(self, other_person):
#         if not isinstance(other_person, Person) raise TypeError(other_person, 'is not a', Person)
#         self.friends.add(other_person)
#         other_person.friends.add(self)
# ```
# 
# the `add_friend()` method will raise an exception if it is used with a parameter which is not a `Person`
# 
# how can we test this?
# 
# if we wrap the code that is supposed to throw the exc

# In[154]:


get_ipython().run_cell_magic('file', 'test_add_person_exception.py', '\nfrom person import Person\nfrom test_person_fixtures2 import *\n\ndef test_add_person_exception(terry):\n    with pytest.raises(TypeError):\n        terry.add_friend("a shrubbey!")\n\ndef test_add_person_exception_detailed(terry):\n    with pytest.raises(TypeError) as excinfo:\n        terry.add_friend("a shrubbey!")\n    \n    assert \'Person\' in str(excinfo.value)\n\n@pytest.mark.xfail(reason=\'expected to fail\')\ndef test_add_person_no_exception(terry, eric):\n    with pytest.raises(TypeError): # is expecting an exception that won\'t happen\n        terry.add_friend(eric) # this does not throw an exception')


# In[210]:


get_ipython().system('python -m pytest test_add_person_exception.py')


# ## your turn
# use the `requests` module and the `.raise_for_status()` method
# 
# 1. test that `.raise_for_status` will raise an exception when accessing the following URLs:
#    - http://httpstat.us/401
#    - http://httpstat.us/404
#    - http://httpstat.us/500
#    - http://httpstat.us/501
# 2. test that `.raise_for_status` will NOT raise an exception when accessing the following URLs:
#    - http://httpstat.us/200
#    - http://httpstat.us/201
#    - http://httpstat.us/202
#    - http://httpstat.us/203
#    - http://httpstat.us/204
#    - http://httpstat.us/303
#    - http://httpstat.us/304  
# 
# ### hints:
# 1. the `requests` module raises exceptions of type `requests.HTTPError`
# 1. use parameterized fixtures to avoid writing a lot of tests or boilerplate code
# 2. use timeouts to avoid tests that wait forever
# 
# 

# ## solution

# In[198]:


get_ipython().run_cell_magic('file', 'test_requests.py', "\nimport pytest\nimport requests\n\n@pytest.fixture(params=[200, 201, 202, 203, 204, 303, 304])\ndef good_url(request):\n    return f'http://httpstat.us/{request.param}'\n\n@pytest.fixture(params=[401, 404, 500, 501])\ndef bad_url(request):\n    return f'http://httpstat.us/{request.param}'\n\n@pytest.mark.timeout(2)\ndef test_good_urls(good_url):\n    response = requests.get(good_url)\n    response.raise_for_status()\n\n@pytest.mark.timeout(2)\ndef test_bad_urls(bad_url):\n    response = requests.get(bad_url)\n    with pytest.raises(requests.HTTPError):\n        response.raise_for_status()")


# In[208]:


pip install pytest-sugar


# In[209]:


get_ipython().system('python -m pytest --verbose test_requests.py')


# # running tests in parallel
# 
# [Reference](https://pypi.org/project/pytest-xdist/)
# 
# The `pytest-xdist` plugin extends pytest with some unique test execution modes:
# 
# - **test run parallelization**: if you have multiple CPUs or hosts you can use those for a combined test run. This allows to speed up development or to use special resources of remote machines.
# - **--looponfail**: run your tests repeatedly in a subprocess. After each run pytest waits until a file in your project changes and then re-runs the previously failing tests. This is repeated until all tests pass after which again a full run is performed.
# - **Multi-Platform coverage**: you can specify different Python interpreters or different platforms and run tests in parallel on all of them.
# - **--boxed** and **pytest-forked**: running each test in its own process, so that if a test catastrophically crashes, it doesn't interfere with other tests
# 
# We're going to cover only test run parallelization.
# 

# first, lets install `pytest-xdist`:

# In[ ]:


pip install -qq pytest-xdist


# now, lets write a few long running tests

# In[206]:


get_ipython().run_cell_magic('file', 'test_parallel.py', '\nimport time\ndef test_t1():\n    time.sleep(2)\n\ndef test_t2():\n    time.sleep(2)\n\ndef test_t3():\n    time.sleep(2)\n\ndef test_t4():\n    time.sleep(2)\n\ndef test_t5():\n    time.sleep(2)\n\ndef test_t6():\n    time.sleep(2)\n\ndef test_t7():\n    time.sleep(2)\n\ndef test_t8():\n    time.sleep(2)\n\ndef test_t9():\n    time.sleep(2)\n\ndef test_t10():\n    time.sleep(2)')


# now, we can run these tests in parallel using the `pytest -n NUM` commandline parameter.
# 
# Lets use 10 threads, this will allow us to finish in 2 seconds rather than 20

# In[207]:


get_ipython().system('python -m pytest -n 10 test_parallel.py')


# # Codebase to test: class Person
# 
# Lets reuse the `Person` and `OlympicRunner` classes we've defined in earlier chapters in order to see how to write tests
# 

# In[26]:


get_ipython().run_cell_magic('file', 'person.py', '\n# Person v1\nclass Person:\n    def __init__(self, name):\n        name = name\n    def __repr__(self):\n        return f"{type(self).__name__}({self.name!r})"\n    def walk(self):\n        print(self.name, \'walking\')\n    def run(self):\n        print(self.name,\'running\')\n    def swim(self):\n        print(self.name,\'swimming\')\n        \nclass OlympicRunner(Person):\n    def run(self):\n        print(self.name,self.name,"running incredibly fast!")\n        \n    def show_medals(self):\n        print(self.name, \'showing my olympic medals\')\n    \ndef train(person):\n    person.walk()\n    person.swim()\n    person.run()')


# # our first test
# 
# - [conventions](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery) 
#   1. files with tests should be called `test_*.py` or `*_test.py `
#   2. test function name should start with `test_`
# 
# - to see if our code works, we can use the `assert` python keyword. pytest adds hooks to assertions to make them more useful

# In[31]:


get_ipython().run_cell_magic('file', 'test_person1.py', "from person import Person\n\n# our first test\ndef test_preson_name():\n    terry = Person('Terry Gilliam')\n    assert terry.name == 'Terry Gilliam'")


# In[32]:


get_ipython().system('python -m pytest')


# ## lets run our tests
# 

# In[ ]:


# execute the tests via pytest, arguments are passed to pytest
ipytest.run('-qq')


# ## running our first test
# 

# In[ ]:


# very simple test
def test_person_repr1():
    assert str(Person('terry gilliam')) == f"Person('terry gilliam')"

# test using mock object
def test_train1():
    person = mocking.Mock()
    
    train(person)
    person.walk.assert_called_once()
    person.run.assert_called_once()
    person.swim.assert_called_once()

# create factory for person's name
@pytest.fixture
def person_name():
    return 'terry gilliam'
    
# create factory for Person, that requires a person_name 
@pytest.fixture
def person(person_name):
    return Person(person_name)

# test using mock object
def test_train2(person):
    # this makes sure no other method is called
    person = mocking.create_autospec(person)
    
    train(person)
    person.walk.assert_called_once()
    person.run.assert_called_once()
    person.swim.assert_called_once()


# test Person using and request a person, person_name from the fixtures
def test_person_repr2(person, person_name):
    assert str(person) == f"Person('{person_name}')"
    
# fixture with multiple values
@pytest.fixture(params=['usain bolt', 'Matthew Wells'])
def olympic_runner_name(request):
    return request.param

@pytest.fixture
def olympic_runner(olympic_runner_name):
    return OlympicRunner(olympic_runner_name)

# test train() using mock object for print
@mocking.patch('builtins.print')
def test_train3(mocked_print, olympic_runner):
    train(olympic_runner)
    mocked_print.assert_called()


# In[ ]:


# execute the tests via pytest, arguments are passed to pytest
ipytest.run('-qq')


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# 08-unittest_mock
# exercise/questions
# ```
# 
