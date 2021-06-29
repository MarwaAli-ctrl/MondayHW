#!/usr/bin/env python
# coding: utf-8

# # Map, Filter, Reduce, Lambda & Recursion

# ## Tasks Today:
# 
# 1) <b>Lambda Functions</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Saving to a Variable <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Multiple Inputs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Passing a Lambda into a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Returning a Lambda from a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #1 <br>
# 2) <b>Map</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Map <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #2 <br>
# 3) <b>Filter</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Filter <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #3 <br>
# 4) <b>Reduce</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Reduce <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #4 <br>
# 5) <b>Recursion</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Implementing a Base <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Writing a Factorial Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #5 <br>
# 6) <b>Generators & Iterators</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Yield Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Inifinite Generator <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #6 <br>
# 7) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Filtering Empty Strings <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Exercise #2 - Sorting with Last Name <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Exercise #3 - Conversion to Farhenheit <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Exercise #4 - Fibonacci Sequence <br>

# ## Lambda Functions <br>
# <p>Lambda functions... or "Anonymous Functions" are referring to inline functions with no name. The keyword lambda denotes the no name function, and executes within a single line. Without saving it to a variable; however, it is not able to be used, unless passed in either as a paramater or within list comprehension.<br>Written as "(keyword lambda) (one or more inputs) (colon) (function to be executed)"</p>

# #### Syntax

# In[1]:


def addTwo(x):
    return x + 2

print(addTwo(4))

# Lambda Function Syntax
# Example of calling a lambda function without a variable
print((lambda x: x + 2)(4))


# #### Saving to a Variable

# In[2]:


f_test = lambda x: x + 2

f_test(4)


# #### Multiple Inputs

# In[3]:


# Multiple Inputs with no variable
print((lambda x,y,z: x * y * z)(3,5,8))

# Multiple Inputs with a variable attached
x_test = lambda x,y,z: x * y * z
print(x_test(3,5,8))


# #### Passing a Lambda into a Function

# In[4]:


def multiply(f,num):
    """
        f expects a lambda function
        num expects a number
    """
    return f(num)
multiply(lambda x: x * x, 4) # lambda 4: 4 * 4


# #### Returning a Lambda from a Function

# In[5]:


# Regular defined function
def multiply_test(num):
    return num * 4

# Function within a function
def returnFunc():
    test = 4
    def multiply(num):
        return num * 2
    return multiply

f_return = returnFunc()
print(returnFunc())
print(f_return(4))

# Lambda function returned from a regular function
def returnLam(b,c):
    return lambda x,a: x + a + b + c
r_lamb = returnLam(4,5)
print(r_lamb(5,5))


# #### If Statements within Lambdas

# In[6]:


# Lambda x : True if (condition) else False
f_condition = lambda num : num * 2 if num > 10 else num + 2

print(f_condition(8))

print(f_condition(12))

print(f_condition(10))


# #### In-Class Exercise #1 <br>
# <p>Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'.</p>

# In[7]:


print((lambda f: f**3)(5))
f = lambda x: x**3


# ## Map <br>
# <p>The map function allows you to iterate over an entire list while running a function on each item of the list. This is why the map function works well with lambda's, because it simplifies things and you write less lines of code.<br>The syntax for a map function is "map(function to be used, list to be used)"<br>However, you must be careful, as the map function returns a map object, not a list. To turn it into a list we use the list() type conversion.</p>

# #### Syntax

# In[8]:


# map(func,iterable(list,dict,tuple,set))
# Normally the usage of map happens with a pre-defined function -- but we can use lambdas as well
def squared(num,num2):
    if num < 10 and num2 < 10:
        return num ** 2, num2 ** 2
    else:
        return num,num2
    
numbers = [4,11,20,3,15,20]
more_nums = [4,10,3,2,6]

squared_nums_map = list(map(squared,numbers,more_nums))
print(squared_nums_map)


# #### Using Lambda's with Map

# In[9]:


# map(lambda x: x + 2, list)
# using lambda in map happens in line (or in one line) usually
# list(map(lambda x : x * 2,nums))
squared_nums_lamb = list(map(lambda x,y : (x ** 2,y ** 2) if x < 10 and y < 10 else (x,y),numbers,more_nums))
print(squared_nums_lamb)


# #### In-Class Exercise #2 <br>
# <p>Use the map function to double each number and minus it by one in the list by using a lambda function</p>

# In[10]:


nums = [4,11,20,3,15,20]
x2sub1 = list(map(lambda x: x*2-1, nums))
x2sub1


# ## Filter() <br>
# <p>Filter's are similar to the map function, where you're able to pass a function argument and a list argument and filter out something from the list based on the conditions passed. Similar to the map function, it returns a filter object, so you need to type convert it to a list()</p>

# #### Syntax

# In[40]:


names = ['Bob','Andy','Max','Evan','Angelica']

def a_names(name):
    if name[0].lower() == 'a':
        return True
    else:
        return False
new_names_list = list(filter(a_names, names))
print(new_names_list)

print(a_names)


# #### Using Lambda's with Filter()

# In[12]:


new_names_lamb = list(filter(lambda name: True if name[0].lower() == 'a' else False, names))
print(new_names_lamb)


# #### In-Class Exercise #3 <br>
# <p>Filter out all the numbers that are below the mean of the list.<br><b>Hint: Import the 'statistics' module</b></p>

# In[13]:


nums = [2,7,4.2,1.6,9,4.4,4.9]


# ## Recursion <br>
# <p>Recursion means that a function is calling itself, so it contanstly executes until a base case is reached. It will then push the returning values back up the chain until the function is complete. A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.</p>

# #### Implementing a Base Case

# In[14]:


def addNums(num):
    # Set base case for recusive function
    if num <= 1:
        print("addNums(1) = 1")
        return num
    else:
        print(f"addNums({num}) = {num} + addNums({num - 1})")
        return num + addNums(num - 1)
    
addNums(5)


# #### Writing a Factorial Function

# In[15]:


# 5! = 5 * 4 * 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
    
factorial(5)


# #### In-Class Exercise #5 <br>
# <p>Write a recursive function that subtracts all numbers to the argument given.</p>

# In[16]:


# f(n) = n-(n-1)-(n-1)-....-2, -1
# f(10) = 10-9-8-7-6-5-4-3-2-1


# ## Generators <br>
# <p>Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the yield statement.</p>

# #### Yield Keyword <br>
# <p>The yield keyword denotes a generator, it doesn't return so it won't leave the function and reset all variables in the function scope, instead it yields the number back to the caller.</p>

# In[17]:


def my_range(stop, start, step = 2):
    while start < stop:
        yield start # yield keyword denotes a generator
        start += step
for i in my_range(20, start = 2):
    my_generator_value = i
    print(my_generator_value)

my_range(20,start = 2)


# #### Infinite Generator

# In[18]:


# bad, never create infinite loops


# #### In-Class Exercise #6 <br>
# <p>Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.</p>

# In[19]:


# for i in numbers_squared(10)
def generator(num):
    while num >= 0:
        yield num**2
        num-=1
        
for x in generator(5):
    print(x)
       


# # Exercises

# ### Exercise #1 <br>
# <p>Filter out all of the empty strings from the list below</p>
# 
# `Output: ['Argentina', 'San Diego', 'Boston', 'New York']`

# In[57]:


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

places = list(filter(None, places))

print ("Output : " + str(places))


# ### Exercise #2 <br>
# <p>Write an anonymous function that sorts this list by the last name...<br><b>Hint: Use the ".sort()" method and access the key"</b></p>
# 
# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']`

# In[50]:


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
x = sorted(author, key=lambda name: name.split(" ")[-1].lower())
print(x)


# ### Exercise #3 <br>
# <p>Convert the list below from Celsius to Farhenheit, using the map function with a lambda...</p>
# 
# `Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# `

# In[36]:


# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

#F_C = (9/5)*int(c) + 32
f = list(map(lambda x: (x[0], (9/5)*x[1] +32), places))

print(f)


# ### Exercise #4 <br>
# <p>Write a recursion function to perform the fibonacci sequence up to the number passed in.</p>
# 
# `Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8`

# In[ ]:




