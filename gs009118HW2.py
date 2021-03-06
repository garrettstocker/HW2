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

# 6 ) create a new variable 
nextNewCustomerID = max(customerIdList) + 1  # using the max function to add 1 to the max result
print("The next new customer will have an ID of " + str(nextNewCustomerID))  # using string and concat to create the final output message
customerIdList.append(nextNewCustomerID) # used this to fix the index out of range for question 10

# 7 ) using the append method
cityList.append("Athens")  # append the city
stateList.append("OH") # append state
zipCodeList.append(45701) # append int value zip code
incomeList.append(55000) # append int value of income
cityIndexValue = cityList[10] # copy and paste the code from problem 5
stateIndexValue = stateList[10]
zipCodeIndexValue = zipCodeList[10] 
print("Customer " +  str(nextNewCustomerID) + " ships to " + str(cityIndexValue) + ", " + str(stateIndexValue) + " " + str(zipCodeIndexValue)) # utilize previous code to print out expected outcome

# 8 ) display data statistics 
import statistics
incomeMean = statistics.mean(incomeList)
incomeMedian = statistics.median(incomeList)
incomeMode = statistics.mode(incomeList)
incomeMax = max(incomeList)
incomeMin = min(incomeList) # import the statistics module and use it tofind the mean median and mode
print("Income stats: ")
print("Mean: " + '$' + format(incomeMean, ',.0f'))
print("Median: " + '$' + format(incomeMedian, ',.0f'))
print("Mode: " + '$' + format(incomeMode, ',.0f')) # the format '$' + format(variable, ',.0') is used for monetary values
print("Max: " + '$' + format(incomeMax, ',.0f'))
print("Min: " + '$' + format(incomeMin, ',.0f'))
# i tried creating a new list in the line below to fix the issue but I kept getting the same results as before. Not sure what to do.
#aList = [65000, 49000, 54000, 114000, 60000, 76000, 44000, 47000]
#aList.append(55000)

# 9 ) create a set of the zipcode list
setZip = set(zipCodeList) # turning the list of zip codes to a set
six = 6 # variable to displau 6 in the print
print("We have " + " " + str(six) + " unique zip codes: " + str(sorted((setZip))))  # useing sorted to sort the set 

# 10 ) 
#dictKeys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#dictValues([("Pickerington", "OH", 43147), ("Atlanta", "GA", 30303), ("Atlanta", "GA", 30303), ("Chippewa Falls", "WI", 54729), ("Pickerington", "OH", 43147), ("Atlanta", "GA", 30303), ("Pickerington", "OH", 43147), ("Flushing", "NY", 11354), ("Kalamazoo", "MI", 49009), ("Atlanta", "GA", 30303), ("Athens", "OH", 45701)])
dictionaryWithCustomerData = {1:tupleCustDataOne, 2:tupleCustDataTwo, 3:tupleCustDataThree, 4:tupleCustDataFour, 5:tupleCustDataFive, 6:tupleCustDataSix, 7:tupleCustDataSeven, 8:tupleCustDataEight, 9:tupleCustDataNine, 10:tupleCustDataTen, 11:tupleCustDataEleven}

whichIndexValue = 0    # index value to pull from the list
tupleCustDataOne = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])  # values for the dictionary in line 77
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataOne # combine line 79 and 80 to go into the dictionary

whichIndexValue = 1
tupleCustDataTwo = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue]) # repeat 9 more times 
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataTwo

whichIndexValue = 2
tupleCustDataThree = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataThree

whichIndexValue = 3
tupleCustDataFour = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataFour

whichIndexValue = 4
tupleCustDataFive = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataFive

whichIndexValue = 5
tupleCustDataSix = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataSix

whichIndexValue = 6
tupleCustDataSeven = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataSeven

whichIndexValue = 7
tupleCustDataEight = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataEight

whichIndexValue = 8
tupleCustDataNine = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataNine

whichIndexValue = 9
tupleCustDataTen = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue])
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataTen

whichIndexValue = 10  
tupleCustDataEleven = (cityList[whichIndexValue], stateList[whichIndexValue], zipCodeList[whichIndexValue]) 
dictionaryWithCustomerData[customerIdList[whichIndexValue]] = tupleCustDataEleven 

printVar = 11 # variable that represents 11 in line 125
print("The data associated with key " + str(printVar) + " is: " + str(tupleCustDataEleven))
print("All keys in the dictionary are: ") # sentence for print
print(dictionaryWithCustomerData.keys()) # shows the key in the dictionary 1, 2, 3...
print("All values in the dictionary are: ") # sentence for print
print(dictionaryWithCustomerData.values()) # shows the values such as state city and zip