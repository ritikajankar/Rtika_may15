#!/usr/bin/env python
# coding: utf-8

# # Machine learning -FST-5
# Grading Test -15-05-2023
# 
# Note : Read all the questions carefully before answering.
# 
# Save your jupyter notebook with ur name_date pattern ( shilpa_may15) and upload on github,and submit
# the github link in the google form provided.

# ## PART A ( Multiple choice 6*1 = 6)

1.A Lambda Function is a _________function

a)Small function

b)Anonymous function

c)Default function

d)All of the above
# In[ ]:


ANS : b) Anonymous Function.

2.Why would you use the pass statement ?

a) Python has the syntactical requirement that code blocks cannot be empty.

b)Ignoring (all or) a certain type of Exception

c)Testing that code runs properly for a few test values, without caring about the results

d) All of the above
# In[ ]:


ANS : d) All of the above.

3.What is MRO in Python?

a)Machine learning repository

b)defines the order in which the base classes are searched when executing a method.

c)Method over riding

d)Method overloading
# In[ ]:


ANS : b) defines the order in which the base classes are searched when executing a method.

4.What is self in Python?

a)You can access the attributes and methods of the class in python

b)Represents the instance of the class

c)Binds the attributes with the given argument

d) All of the above
# In[ ]:


ANS : b) Represents the instance of the class

5.What is __init__?

a)Object of every class

b)Constructor method in python

c)Only few classes in python have init methods

d)None of the above
# In[ ]:


ANS : b) Constructor method in python .


# In[ ]:


get_ipython().run_line_magic('pinfo', 'expression')

a)One or more occurrences

b)Zero or more occurrences

c)Zero or one occurrences

d)Exactly the specified number of occurrences


# In[ ]:


ANS : Zero or more occurrences 


# ## PART B ( Answer in a line 10*2  = 20)
# 
6.What is break and continue in python? Explain with example
# In[178]:


# Break:
for i in range(5):
    if i == 2:
        break
    print(i)


# In[186]:


# Continue:
n=0
while n<12:
        n=n+1
        if n%2==0:
            continue
        print(n)

7.What are Dict and List comprehensions? Give atleast one example(code)
# In[107]:


# Dictonary comprehensation 
li=[1,2,13,15,10,11,14]
ol={}

for i in li:
    if(i%2!=0):
        ol[i] = i*2
ol


# In[103]:


ol= {i:i**3 for i in li if i % 2!= 0}
ol


# In[97]:


# List Comprehensation : 
Number=[i*i*i for i in range(10)]
Number

8.How do you create a class in Python?
# In[81]:


class FoodMall:
    def __init__(self):
        print("Lonavla")
    def menu():
        print("Food")


# In[83]:


Mumbai=FoodMall()

9.What is inheritance ?Give  one example 
# In[ ]:




10.What is polymorphism? Give one example
# In[200]:


class Shape:
   def area(self,radius):
       return 3.14 * radius * radius
    
   def area(self,l,b):
       return l * b

11.Difference between multilevel and multiple inheritance?
# In[ ]:


# Multiple Inheritance has Two Parent class and One child Class.


# In[71]:


# Multilevel Inheritance has Three Different Parent Class .
class Student:
    def review(self):
        print("Result of Student")
class Parent(Student):
    def __init__(self,school,name):
        print("Exam is Easy")
        self.school=school
        self.name=name
    def buy(self):
        print("Exam is hard")
class Teacher(Parent):
    pass

12.Create a 1D,2D and 3D array?
# In[64]:


import numpy as np 
# 1D Array 
c=np.array([1,2,3])
print(c)
print(c.ndim)


# In[63]:


# 2D Array
c=np.array([[4,5,6]])
print(c)
print(c.ndim)


# In[65]:


# 3D Array
c=np.array([[[8,9,10],[4,5,6]]])
print(c)
print(c.ndim)

13.How will you reverse the numpy array using one line of code?
# In[95]:


import numpy as np
c=np.array([[1,2,3],[4,5,6]])
print(c)
print(c.shape)
c[1:3,1:2]

14.What advantages do NumPy arrays offer over  Python lists?
# In[ ]:


Numpy arrays Excecuted fatser than Python List
Arrays Consumes more memory than List 

15.python3 code to print the below pattern

*
**
***
# In[26]:


for i in range(3):
    for j in range(i+1):
        print("*",end ="")
    print()


# ## PART C (Exploratory data analysis)
16.Draw insights from the dataset provided using suitable visualization libraries.(6*4 = 24)



1.Load the "Diamonds dataset " from seaborn library

Dataset desciption:
(carat: weight of the diamond
cut: (Fair, Good, Very Good, Premium, Ideal) ordinal
color: J (worst) to D (best) ordinal
clarity: [I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)]
depth: z / (mean(x,y)) = 2*z / (x+y) in percentage
table: percentage of width on the top relative to width
price: given in US Dollars
x: length in mm
y: width in mm
z: depth in mm)

2.Which column has highest correlation with the target variable?(Graphs)

3.Find the outliers in each column?Use suitable graphs

4.what is the count of premium diamonds in the dataset?

5.What is the average price of diamonds?

6.Create a new column called "size = x*y*z
# In[120]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# In[198]:


# Qstn 2 .
data=pd.read_csv(r"C:\Users\dell\Downloads\diamonds.csv")
data


# In[199]:


data.drop("Unnamed: 0",axis=1,inplace=True)
data.head()


# In[197]:


data.shape


# In[171]:


data.index


# In[172]:


data.corr()


# In[173]:


corr = data.corr()
sns.heatmap(corr)


# In[174]:


# Qstn 3. Outliers 
sns.boxplot(x = 'depth',data = data)


# In[175]:


sns.boxplot(x = 'table',data = data)


# In[191]:


#Qstn 4. 
most_prem=data['cut'].value_counts()
most_prem


# In[194]:


# Qstn 5 . Average Price 
data.describe()


# In[ ]:




