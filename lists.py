#LISTS - it can store heterogeneous data - integers,floating numbers,strings,boolean
#values , EVEN ANOTHER LIST
l1 = list([1,2,3])
print(l1)
list1 = [1,3,9,0]
list2 = [1,7,"sdfjhsigh",'thu',True,4,8,[1,5,7]]
temp = ["mon","tue","wed","thu"]
print(list1)
print(list2)
print(len(list1) , " : list1 length") # same as using len() on a strings
print(len(list2) , " : list2 length")

#INDEXING AND SLICING IN A LIST IS THE SAME AS strings

#ADDING ITEMS TO A LISTS
list1.append(8) #adds an item to the end of the specified list(only one arg allowed)
print(list1)
temp.extend(list1) #adds list1 elements at the end of temp list elements
#(basically for adding two lists together)
print(list1) #this won't change
print(temp) #this will change

#Adding item at a specific position in a list
fests = ["New year" , "Good Friday","Easter","Diwali","Holi"]
fests.insert(3,"Dussehra") #where and what to insert
print(fests)

#REMOVING ITEMS FROM A LISTS(using their index) - We generally use the pop() method
item1 = temp.pop() #pop() returns the popped out value so it must be saved like this in order to know what got removed
print(temp)
print(item1)

item2 = list1.pop(3) #by default pop() removes the last element from the list but if we put
#the specific index of the element we want to remove like in this line it removes that
print(list1)
print(item2)
#REMOVING ITEMS FROM A LISTS(using their values)
fruits = ["apple","orange","cherry","banana","cherry"]
fruits.remove("cherry") #will remove the first occurence of "cherry" - not all of them
print(fruits)

#LISTS ARE MUTABLE UNLIKE STRINGS

#REVERSING A LIST
list3 = ["jan","feb","mar","apr","may"]
print("Before Reversing : ",list3)
list3.reverse() #The changes take place in list3 itself (permanently)
print("After Reversing : ",list3)

#SORTING A LIST
list4 = [7,45,80,12,45]
print("Before Sorting : ",list4)
list4.sort() #The changes take place in list4 itself (permanently)
print("After Sorting : ",list4)

#INDEXING A NESTED LIST (this could go on)
nestedlist = [1,[4,5],9,8,5]
print(nestedlist[1]) #prints the 2nd element which is a list in its own
print(nestedlist[1][0]) #prints the 1st item of the 2nd element of nestedlist
print(nestedlist[1][1]) #prints the 2nd item of the 2nd element of nestedlist

#LIST COMPREHENSION
matrix = [[1,2,3] , [1,4,9] , [1,8,27]]
print(matrix)
#The normal for loop
for element in matrix:
    print(element)

#for loop usage in LIST COMPREHENSION:
result = [element[1] for element in matrix]
print(result)

#for loop usage in LIST COMPREHENSION (complicated version tried by me):
for i in range(0,len(matrix)):
    res = [element[i] for element in matrix]
    print(res)



#TUPLES - IMMUTABLE UNLIKE LISTS - Quite good at unpacking - you will see in many string formats
t1 = ("Infy","Virtusa","Paytm")
i,v,p = t1
print(i,end=":")
print(v,end=":")
print(p)
