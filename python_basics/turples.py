# Name : Gabriel Egan Gakere
# Date : 18/02/2026
# A program to show turples in python

fruits =("Avocado",  "Kiwi", "Apples", "Banana", "Orange")


print(len(fruits))
print(fruits[0])
print(fruits[-1])
print(fruits[4])

# Error - in turples you can not append nor pop or the rest of the function because its immutablle 
# Immutable means that cannot change the list


fruits_list = list(fruits) #converts a turple to a list 

fruits_list.append("guava")

print(fruits_list)