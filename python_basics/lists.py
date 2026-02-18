# Name : Gabriel Egan Gakere
# Date : 18/02/2026
# A program to show lists in python


friends = ["Racheal", "Phoebe", "Ross", "Chandler", "Monica", "Joey"] #list of friends

print(friends)


# Sort function
friends.sort()
print(friends)

# Reverse function
friends.reverse()
print(friends)

# Append function 
friends.append("Jack") # Adds "JAck" to the furthest end
print(friends)



new_friends = ["Tracy", "James", "Faith", "Don", "augustine", "Wendy"]



# Len - gives the number of elements in the lists
print(len(new_friends))


# New list of students - addint two lists

students = friends + new_friends
print(students)


students.pop() # removes the last item on the list
print(students)


students.insert(5,"Jenny") # Inserts a new item to the list
print(students)

students.insert(9,"Valarie")
print(students)

students.extend("James")
print(students)

students.remove("Jack") # Removes an item from the list
print(students)


new_students = students.copy()
print(new_students)