#!/usr/bin/env python
# coding: utf-8

# # Python User Define Function Practice Activity - 2 

# Asst. Prof. Syed Faisal Ali              $\;\;\;\;\;\;$              Programming Fundamentals - FALL 2019 $\;\;\;\;\;\;$ Software Engineering                     $\;\;\;\;\;\;$                   Dated: 27 Nov 2019

# Question 1: Create a function to find the following:
# If the base of triangle is 3 cm long and its equilateral triangle and the radius of circle is 1.5 cm then find the area of triangle shaded. 
# 

# ![proj](q1.jpg)

# In[40]:


import math
def area(r, b):
    area_of_circle = math.pi*r*r
    area_of_triangle = b*b*3
    x = area_of_triangle-area_of_circle        
    print("area of shaded region is: " ,x)
area(1.5,3)

    


# Question 2: Create a function which can read a dictionary of your family members such as 5 members. 
# 1 Abbu, 1 Ammi, 2 Brothers 1 Sister. Now feed this data in dictionary in terms of name and relations.
# The UDF will ask findrelation() in this you will enter Brother it will return the names of two brothers you have inserted. In case if the relation is not found it will return “Sorry the relation doesn’t exist in your family.” 
# 

# In[6]:


def relation(d):
    dict={'father':'MOHAMMAD ALI','brother':'SHAYYAN','sister':'HERMAIN','mother':'REENA ALI'}
    x=dict[d]
    return x
print(relation('mother'))
print(relation('brother'))


# Question 3: Create a function to find the following:
# If the base of triangle is 5 cm long and its equilateral triangle and the radius of circle is 2.25 cm then find the area of triangle shaded. 
# 

# ![proj](q3.jpg)

# In[38]:


import math
def area(r, b):
    area_of_circle = math.pi*r*r
    area_of_triangle = b*b*5
    x = area_of_circle-area_of_triangle        
    print("area of shaded region is: " ,r," cm^2")
area(2.25,5)


# Question 4:
# Create a function that takes a list of random numbers from users and add only those which are even. If all the numbers are odd it will return sorry no even number found.
# 

# In[4]:


def even(a,f,d,e,s):
    lst = [a,f,d,e,s]
    sum = 0
    for i in lst:
        if i%2 == 0:
            sum = +i
    print("sum of even numbers are ",sum)
even(2,3,5,6,8)    


# Question 5:
# Write a function which can take a list of numbers and it will return sorted list.
# 

# In[8]:


def sortt(a,f,d,e,s,z):
    lst = [a,f,d,e,s,z]
    lst.sort()
    print("the sorted list is ",lst)
sortt(23,43,54,63,99,53)


# Question 6:
# Write a function that will take the radius and return the perimeter and area of circle with 5% increment.
# 

# In[11]:


def area_circle(pi,r):
    return(pi*r**2)*5/100
def perimeter_rectangle(a, b):
    return (2 * (pi*r))*5/100
pi = 3.142
r = 6
print ("area = ", area_circle(pi, r))
print("perimeter = ",
perimeter_rectangle(pi, r))      


# Question 7:
# Write a function that will take the strings as argument and return number of vowels and consonants.
# 

# In[4]:


def vowels(s):
    vowel = 0
    consonant = 0
    for i in s:
        if i in "aeiouAEIOU":
            vowel += 1
        else:
            consonant +=1
    print("the number of vowels are ",vowel)
    print("the number of consonants are ",consonant)
vowels("Faizan Ali")    


# Question 8:
# Write a function that will take length and breadth for a rectangle and return perimeter and area of rectangle with 8% increment.
# 

# In[7]:


def perimeter_area(l,b):
    p=2*(l+b)
    a=l*b
    x=p/12.5+p
    y=a/12.5+a
    print("the perimeter of rectangle is ",x,"\nthe area of rectangle is ",y)
perimeter_area(5,10)


# Question 9:
# Write a function that can take the numbers in strings. From string find which number is even and which one is odd. Save them in two different lists and generate the result.
# 

# In[8]:


def str1(a,d,e,s,z,f):
    even=[]
    odd=[]
    lst=[a,d,e,s,z,f]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even list are ",even,"\nodd list are ",odd)
str1(2,10,18,25,88,72)


# Question 10:
# Write a function which will take the string from the user and return how many alphabets have been used in it and which alphabets are missing.
# 

# In[30]:


def alphabet(s):   
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s:
        alphabets.remove(i)
    print('the missing alphabets are ',alphabets)
    print("the used alphabet are ",s)
    for i in s:
        print(i,end=" ")
alphabet("faizn")


# Question 11:
# Write a function that will take verbs in words and return a list of verbs with continuous tense by adding (ing) at the end of each verb.
# 

# In[9]:


def verb(x):
    return x+"ing"
print(verb("dance"))
print(verb("sing"))


# Question 12:
# Make a function which can take two radius of circles and find the areas of it and subtract smaller one from larger one and tell the remaining area of circle.
# 

# In[14]:


import math
def area(rad1,rad2):
    area_1=math.pi*rad1*rad1
    area_2=math.pi*rad2*rad2
    if rad1>rad2:
        area=area_1-area_2
        print("the area of circle is ",area)
    elif rad1<rad2:
        area=area_2-area_1
        print("the area of circle is ",area)
print(area(2,8))
print(area(8,2))


# Question 13:
# Write a function that will take a string and calculate number of Upper case letters and lower case letters.
# 

# In[15]:


def strtest(s):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if i.isupper():
            d["UPPER_CASE"]+=1
        elif i.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("Original string :", s)
        print("No. of Upper case characters : ", d["UPPER_CASE"])
        print("No. of Lower case characters : ", d["LOWER_CASE"])
                                                   
strtest('Try to be Practical in Life')     


# Question 14:
# Write a function which will take length and breadth of two rectangles. Subtract the smaller rectangle from the larger rectangle and return the area left behind.
# 

# In[34]:


def area_rectangle(len1,bread1,len2,bread2):
    area_1 = len1*bread1
    area_2 = len2*bread2
    if area_1>area_2:
        area = area_1-area_2
        print("the area of rectangle is ",area," m.sq")
    elif area_2>area_1:
        area = area_2-area_1
        print("the area of rectangle is ",area," m.sq")
area_rectangle(2,4,6,8)
area_rectangle(1,3,5,7)


# Question 15:
# Create a function that can add the fractions in series such as 1 to 8 = 1/8+1/7+1/6+1/5 …… ½ and return the result in fraction not in decimal.
# 

# In[19]:


import fractions
def fraction(x1,x2):
    lst = []
    for i in range(x1,x2+1):
        x=fractions.Fraction(1,i)
        lst.append(x)
    print(sum(lst))
fraction(4,9)    


# Question 16:
# Write a function which will take height and base for a triangle and 
# 

# In[22]:


import math
def triangle(x,y):
    z = (x*x)+(y*y)
    Z = math.sqrt(z)
    print("the third side of triangle is ",Z)
triangle(2,4)    


# Question 17:
# Write a function which will take a list of fruits names. The function will return how many alphabets are repetitive in the names of fruits and how many are unique letters.
# 

# In[33]:


import collections
def repitivewords(a,p,e):
    lst=[a,p,e]
    z=0
    an=0
    for i in lst:
        for j in i:
            n=i.count(j)
            if n>1:
                an+=1
    print('the repititive elements are: ',an)
repitivewords("grapes","apple","banana")
            


# Question 18:
# Write a function that can take square length and radius of circle. Find the area of both and subtract the smallest shape from largest one and return the remaining shape area.
# 

# In[23]:


def shape_area(l1,r1,l2,r2):
    area1=l1*l1*r1
    area2=l2*l2*r2
    if area1>area2:
        area=area1-area2
        print("the area of shape is ",area)
    elif area2>area1:
        area=area2-area1
        print("the area of shape is ",area)
shape_area(10,5,20,10)
shape_area(20,10,10,5)


# In[ ]:




