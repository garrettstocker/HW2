# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:52:11 2022

@author: gs009118@ohio.edu  (Garrett Stocker) 
"""
#  1 ) Create a list that contains all customer IDs
customerIdList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # create a list that contains all 10 customer ids
print(customerIdList)

# 2 ) How many customers do we have?
print(len(customerIdList)) # using the len function to count the total number of customer IDs

# 3 ) Create seperate lists that contain each of the other columns ( zip, state etc.)
zipCodeList = [43147, 30303, 30303, 54729, 43147, 30303, 43147, 11354, 49009, 30303] # zip code list in order
cityList = ["Pickerington", "Atlanta", "Atlanta", "Chippewa Falls", "Pickerington", "Atlanta","Pickerington", "Flushing", "Kalamazoo", "Atlanta"] # list of cities in order
stateList = ["OH", "GA", "GA", "WI", "OH", "GA", "OH", "NY", "MI", "GA"] # list of states in order
incomeList = [65000, 49000, 54000, 114000, 47000, 119000, 60000, 76000, 44000, 47000] # list of incomes in order
print("Customer ID: " + str(customerIdList[0])) # indesc customer ID to print the first aka "0" 
print("City: " + str(cityList[0])) # index set to 0 to print the first city
print("State: " + str(stateList[0])) # index set to 0 to print the first state
print("Zip Code: " + str(zipCodeList[0])) #  index set to 0 to print the first zip, 


# 4 ) create a variable you want to store the index value we want to use to look up values
customerIndexValue = customerIdList[0]   # made varialbes to show the index value of each previous variable, to shorten the code from the previous problem
cityIndexValue =  cityList[0]
stateIndexValue = stateList[0]
zipCodeIndexValue = zipCodeList[0]       # combine and concat the variables to print the statement 
print("Customer " +  str(customerIndexValue) + " ships to " + str(cityIndexValue) + ", " + str(stateIndexValue) + str(zipCodeIndexValue))

# 5 ) enter index value 5 instead of 0 for this problem
customerIndexValue = customerIdList[5]   # made varialbes to show the index value of each previous variable, to shorten the code from the previous problem
cityIndexValue =  cityList[5]
stateIndexValue = stateList[5]
zipCodeIndexValue = zipCodeList[5]       # combine and concat the variables to print the statement that includes all of these variables 
print("Customer " +  str(customerIndexValue) + " ships to " + str(cityIndexValue) + ", " + str(stateIndexValue) + " " + str(zipCodeIndexValue))

# 6 ) create a new variableto add the next custome
print(theNextNewCustomerId)






