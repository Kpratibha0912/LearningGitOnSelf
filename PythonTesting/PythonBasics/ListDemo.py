list1 = [1, 2,"Pratibha", "Python", 4, 5]

# This can be modified, updated and deleted
# Insert "learning" at index 3
list1.insert(3, "Learning")
print(list1)

# updating the list
list1[3] = "Rahul"
print(list1)

# slicing
print(list1[3:]) #This will give you the elements of the list from index 3 till the end
print(list1[-3:]) #This will give you the elements of the list from last 3rd index till the end of the list
print(list1[1:5:2]) #this will skip one element from the list

#deleting
del list1[3]
print(list1)

