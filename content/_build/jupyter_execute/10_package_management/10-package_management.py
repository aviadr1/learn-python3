#!/usr/bin/env python
# coding: utf-8

# 
# <a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/10_package_management/10-package_management.ipynb" target="_blank">
# <img src="https://colab.research.google.com/assets/colab-badge.svg" 
#      title="Open this file in Google Colab" alt="Colab"/>
# </a>
# 

# # Where are my packages?
# 
# In this lesson we will learn to answer the following questions:
# 
# 1. where are my installed packages located
# 2. what packages and package versions do I have

# ### FYI: where is the standard library located?
# We can use `inspect.getfile(object)` to get the filename where a module, class or function is defined

# In[1]:


import os, inspect
stdlib = os.path.dirname(inspect.getfile(os))
print(stdlib) # c:\users\aviad\appdata\local\programs\python\python37-32\lib


# ## Package locations
# 
# `pip` installs packages into a `site-packages` directory in one of three locations
# 1. global packages - these packages all available for all users on the machine
# 2. per-user packages - these packages are available only to the current user
# 3. venv packages - virtual environment packages available to a particular environment/project
#    > _more on [venv](https://docs.python.org/3/library/venv.html) later_
# 

# ### 1. global site-packages
# We you can use the `site` module to figure out programatically where our global packages are being installed

# In[2]:


import site, pprint
pprint.pprint(site.getsitepackages())


# what packages (global or user)  do I have?

# In[3]:


get_ipython().system('pip list -v')


# ### 2. per-user site-package
# 
# Lets use the `site` module again to see where our per-user site-packages folder is

# In[4]:


# programmatically with python
site.getusersitepackages()


# In[5]:


# from the shell / command-line
get_ipython().system('python -m site --user-site')


# what local packages do I have?

# In[6]:


get_ipython().system('pip list --user -v')


# # Development of Projects with Different Dependencies
# 
# Lets talk about three common issues that arise when using python extensively:
# 
# 1. working with muliple projects, where each has their own depencies
# 2. having reproducible deterministic development / production environments
# 3. updating dependencies to fix security issues
# 
# we're going to show one awesome tool called [pipenv](https://docs.pipenv.org/en/latest/) that is a solution to all three problems.
# 
# first, lets install pipenv:

# In[7]:


get_ipython().system('pip install pipenv')


# ## 1.working with muliple projects, where each has their own dependencies
# 
# Lets examine a common issue that arises when you’re working on multiple projects. Imagine that ProjectA needs `django==2.1`, but ProjectB needs `django==1.9`.
# 
# By default, Python tries to store all your third-party packages in the system-wide location. This means that every time you want to switch between ProjectA and ProjectB, you have to make sure the right version of django is installed. This makes switching between projects painful because you have to uninstall and reinstall packages to meet the requirements for each project.
# 
# The standard solution is to use a virtual environment that has its own Python executable and third-party package storage. That way, ProjectA and ProjectB are adequately separated. Now you can easily switch between projects since they’re not sharing the same package storage location. PackageA can have whatever version of django it needs in its own environment, and PackageB can have what it needs totally separate. 
# 
# > a common, slightly older way to fix this issue is using [virtualenv](https://virtualenv.pypa.io/en/latest/) + [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). <br>
# > see this [stackoverflow answer](https://stackoverflow.com/a/41573588/52917) for a nice comparison of tools
# 
# Pipenv has virtual environment management built in so that you have a single tool for your package management.
# 
# Lets see how to use this in practice, by creating two seperate django projects
# 
# > [django](https://www.djangoproject.com/) is a well-loved web framework 
# 

# run the following in your shell
# ```
# >> mkdir ProjectA
# >> cd ProjectA
# >> pipenv install django==2.1
# >> pipenv shell
# (ProjectA) >> django-admin startproject ProjectA .
# (ProjectA) >> exit
# ```
# 
# pipenv did a few things for us:
# 1. when we ran `pipenv install django==2.1` it detected that we're in a new project 
#    1. it created a new, empty virtual environment for us, where there are no pre-installed python packages
#    1. it created a new file called `Pipfile` for us <br>
#       the `Pipfile` contains a specification of all of our direct dependencies
#    3. it added a dependency on django version 2.1 to the Pipfile
#    4. it downloaded and installed django 2.1 to our virtual environment
# 2. running `pipenv shell` allowed us to _enter_ our virtual environment where our PATH variable is set to 
#    include only packages in the virtual environment. the 
# 3. it created a `Pipfile.lock` file which lists all the sub-dependencies django relies on (as it happens, django does not rely on additional packages)
# 
# this is how the file structure looks now
# ```
# ProjectA/
# ├── ProjectA/
# ├── manage.py
# ├── Pipfile
# └── Pipfile.lock
# ```
# 
# Notes:
# 1. we should commit to source control the `Pipfile` and `Pipfile.lock` files that describe's the project dependencies. <br>
# 
# 2. notice that running `pip freeze`, django was not installed in our global/user directory, but rather just in our virtual environment <br>
# 
# 3. we could now easily create as many projects as we want with different dependencies or versions of dependencies without any collisions

# ## 2. having reproducible deterministic development / production environments
# 
# Now lets imagine we're using the `pandas` package in our project. 
# right now we're just interested in having an up-to-date version without caring too much about the version.
# 
# lets add it to our environment
# ```
# >> pipenv install pandas
# ```
# 
# as it happens, the pandas package relies on a few sub-dependencies like numpy
# ```
# >> pipenv graph
# Django==2.1
#   - pytz [required: Any, installed: 2019.1]
# pandas==0.24.2
#   - numpy [required: >=1.12.0, installed: 1.16.4]
#   - python-dateutil [required: >=2.5.0, installed: 2.8.0]
#     - six [required: >=1.5, installed: 1.12.0]
#   - pytz [required: >=2011k, installed: 2019.1]
# ```
# 
# but what happens if one of the sub-dependencies later publish a new version with breaking changes, and another developer on my team tries to install the project's dependencies and ends up with a build that doesn't work?
# > It worked on my computer, I swear
# 
# What we need is a deterministic build - that is, to be able to have _exactly_ the same environment and code for the project on our teammates' computer, as well as in production. this is exactly the information held in our `Pipfile.lock` file. it has a list of all the sub-dependencies that were installed, and their exact version numbers and hashes.
# 
# We can install the exact packages and versions listed in our Pipfile.lock file using the `pipenv sync` command.
# 
# ```
# >> pipenv sync
# Installing dependencies from Pipfile.lock (aac533)…
#   ================================ 6/6 - 00:00:03
# All dependencies are now up-to-date!
# ```
# 
# 
# when deploying code to developer machines or to production environment `pipenv sync` creates a deterministic build by ensuring everyone has exactly the same packages in the same versions
# 

# ## 3. updating dependencies to fix security issues
# 
# so for our ProjectA we pinned the version of django to be 2.1 `django==2.1`.
# we have a deterministic build and our code seems to work well.
# 
# but what if there was an important bugfix or a security error in one of our dependencies, or worse, in one of our sub-dependencies?
# 
# lets check for security issues by running `pipenv check`:
# ```
# (ProjectA) >> pipenv check
# Checking PEP 508 requirements…
# Passed!
# Checking installed package safety…
# 36883: django <2.1.6,>=2.1.0 resolved (2.1 installed)!
# Django 2.1.x before 2.1.6  allows Uncontrolled Memory Consumption via a malicious attacker-supplied value to the django.utils.numberformat.format() function.
# 
# 36522: django <2.1.2,>=2.1 resolved (2.1 installed)!
# An issue was discovered in Django 2.1 before 2.1.2, in which unprivileged users can read the password hashes of arbitrary accounts. The read-only password widget used by the Django Admin to display an obfuscated password hash was bypassed if a user has only the "view" permission (new in Django 2.1), resulting in display of the entire password hash to those users. This may result in a vulnerability for sites with legacy user accounts using insecure hashes.
# 
# 36517: django <2.1.2,>=2.1.0 resolved (2.1 installed)!
# django before 2.1.2 fixes a security bug in 2.1.x.
# If an admin user has the change permission to the user model, only part of the
# password hash is displayed in the change form. Admin users with the view (but
# not change) permission to the user model were displayed the entire hash.
# ```
# 
# Oh My! <br>
# seems a lot has already been been fixed since 2.1.0, the version we pinned to ...
# lets upgrade to the latest bugfix version of 2.1.x
# 
# ```
# >> pipenv install django<2.2
# ```
# 
# this should do it. lets take a look at our list of packages now
# ``` >> pipenv graph
# Django==2.1.10
#   - pytz [required: Any, installed: 2019.1]
# pandas==0.24.2
#   - numpy [required: >=1.12.0, installed: 1.16.4]
#   - python-dateutil [required: >=2.5.0, installed: 2.8.0]
#     - six [required: >=1.5, installed: 1.12.0]
#   - pytz [required: >=2011k, installed: 2019.1]
# ```
# 
# now we have the latest django 2.1.10, without switching to a major new django 2.2.x
# lets see if our security problems are fixed:
# 
# ```
# >> pipenv check
# Checking PEP 508 requirements…
# Passed!
# Checking installed package safety…
# All good!
# ```
# 
# what happens if in the future additional security issues are fixed for the 2.1 branch?
# running `pipenv install` would install all packages mentioned in my `Pipfile`, including upgrading them if newer versions that satisfy my constraints are available.

# ## Tying it all together
# 
# so what have we seen? 
# 
# 1. pipenv manages a virtual environment for us where each project can have exactly the dependencies it needs and nothing more
# 2. we used `pipenv install django` and `pipenv install pandas` to add packages to our virtual environment
# 3. we used two [PEP 508](https://www.python.org/dev/peps/pep-0508/) version specifiers to pin down a version of django. `django==2.1` which pinned us to 2.1.0 and `django<2.2` which allowed us to receive bug/security fixes upto 2.1.10
# 4. we used `pipenv sync` to install a deterministic build using the specific pinned down versions specified in our `Pipfile.lock` file
# 5. we used `pipenv install` to upgrade to the latest versions in our `Pipfile` that satisfy our constraints
# 6. we used `pipenv check` to test for security issues
# 7. we used `pipenv shell` to _enter_ into our virtual environment and use installed tools for that environment like django-admin
# 
# generally, pipenv ...
# * Enables truly deterministic builds, while easily specifying only what you want.
# * Generates and checks file hashes for locked dependencies.
# * Automatically generates a Pipfile, if one doesn’t exist.
# * Automatically creates a virtualenv in a standard location.
# * Automatically adds/removes packages to a Pipfile when they are un/installed.
# 
# 
# ### Further reading
# * https://docs.pipenv.org/en/latest/
# * https://realpython.com/pipenv-guide/
# * https://www.python.org/dev/peps/pep-0508/

# ## Additional features

# ### development-only packages 
# 
# Let’s say you also have some unit tests for this awesome application, and you want to use pytest for running them. You don’t need `pytest` in production so you can specify that this dependency is only for development with the `--dev` argument:
# 
# ```
# $ pipenv install pytest --dev
# ```
# 
# Providing the `--dev` argument will put the dependency in a special [dev-packages] location in the Pipfile. These development packages only get installed if you specify the `--dev` argument with pipenv install.
# 
# The different sections separate dependencies needed only for development from ones needed for the base code to actually work. Typically, this would be accomplished with additional requirements files like dev-requirements.txt or test-requirements.txt. Now, everything is consolidated in a single Pipfile under different sections.

# 

# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# exercise/questions
# ```
# 
