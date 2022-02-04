# -*- coding: utf-8 -*-

# details on the encoding: https://www.python.org/dev/peps/pep-0263/

"""
Created on 3:10 1/13/2022

@author: gs009118 (Garrett Stocker)
"""

#####
##### Python Language Reference:    https://docs.python.org/3/reference/index.html
##### Python Standard Library:      https://docs.python.org/3/library/
#####


####################
##### QUESTION
####################
"""
Question: 
    Lists, sets, tuples, and dictionaries are all examples of complex data types in Python. Whar are the general differenct between them?
Answer: 
    list: [] mutable, can contain any datatype uses and is ordered
    set: {} mutable not ordered, quick way to delete duplicates
    tuple: () immutable, the data within a tuple may not be changed after the initial print
    dictionary: {key:value} 
"""



####################
##### QUESTION
####################
"""
Question: 
    What does mutable/immutable mean?
Answer: mutable means it can be changed and immutable means it cannot be changed
    
"""



####################
##### QUESTION
####################
"""
Question: How do you create a list/set/tuple/dictionary? Provide an example of each.
Answer: 
    list: ['a', 'b', 'c', 'd']
    set: {}
    tuple: ()
    dictionary: {key:value}
"""
myList = ['a', 'b', 'c', 'd']

####################
##### QUESTION
####################
"""
Question: 
    How do you print out the 2nd item in a list?
Answer: 
    
"""
print(myList[1])


####################
##### QUESTION
####################
"""
Question: 
    How do you print out items 1-3 in a list?
Answer: 
    
"""
print(myList[0:3])

####################
##### QUESTION
####################
"""
Question: 
    If you were unsure of how many items were in a list, what could you do to determine the length of a list?
Answer: 
    
"""
len(myList)


####################
##### QUESTION
####################
"""
Question:
    How do you get the minimum or maximum value in a list?
Answer: 
    
"""
min(myList)
max(myList)

####################
##### QUESTION
####################
"""
Question: 
    How do you display the sorted values in a list?
Answer: 
    
"""
myList = ['c', 'd', 'a', 'b']
print(sorted(myList))

####################
##### QUESTION
####################
"""
Question: 
    What if you wanted to see all of the values in a list except for the last value. Also, assume you do not know the length of the list.    
Answer: 
    
"""
print(myList[0:-1])
print(myList[0:len(myList) -1])
print(myList[:-1])

####################
##### QUESTION
####################
"""
Question: 
    What does a dir function do?
Answer: shows all the functions available to us within a module
"""
dir(myList)


####################
##### QUESTION
####################
"""
Question: 
    A method may be refered to as a funciton - all methods will always require what following the name of the method?
Answer: 
    
"""


####################
##### QUESTION
####################
"""
Question: 
    How do you look at the keys of a dictionary?
Answer: 
    How do you look at the values of a dictionary?
""" 
#myDictionary{"A": value, "B": value}


####################
##### QUESTION
####################
"""
Question: 
    How do you get the mean/median/mode of numeric data?
Answer: leverage the statistics module
    
"""
import statistics
#print(statistics.mean())
