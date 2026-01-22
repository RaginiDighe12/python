#Q1Create a tuple with three fruits and print it.

fruitstuple=("Mango","Apple","Grapes")
print(fruitstuple)

#Q2.Create a tuple with one item Python and print its type.

tuplename=("Python",)
print(type(tuplename))

#Q3.Create a tuple of five numbers and print its length using len()

tuplenum=(1,2,3,4)
print(len(tuplenum))


#Q4.Create a tuple and print its first element using index

fruits=("Mango","Apple","Grapes","Orange","Pineapple")
print(fruits[0])

#Q5.Create a tuple and print its last element using negative indexing

fruits=("Mango","Apple","Grapes","Orange","Pineapple")
print(fruits[-1])

#Q6.Create a tuple using tuple() constructor with value 1 to 5 and print it

listnum=[1,2,3,4,5]
tuplenum=tuple(listnum)
print(tuplenum)

#Q7.Given t=(10,20,30,40,50) print element at index 1 and 3

t=(10,20,30,40,50)
print(t[1])
print(t[3])

#Q8.Given t=("a","b","c","d","e"),print element from index 1 to 4 using slicing

t=("a","b","c","d","e")
print(t[1:5])

#Q9.From a tuple t=(5,10,15,20,25,30),print element from index 2 to end

t=(5,10,15,20,25,30)
print(t[2:])



#Q10.From a tuple t=(5,10,15,20,25,30),print element from start to index 3

t=(5,10,15,20,25,30)
print(t[:4])

#Q11.Create a tuple with mixed data types (int, float, string, boolean) and print it

tuplename=(2,4.5,"Ragini",True,"Anurag",False,5)
print(tuplename)

#Q12.Check whether Python exists in a given tuple and print the result

fruits=("Mango","Apple","Grapes","Orange","Pineapple")
print("Python" in fruits)

#Q13.Convert a tuple to a list, add a new element, and print the updated list.

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist.append("Rinal")
print(namelist)

#Q14.Convert a list back into a tuple and print it

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist.append("Rinal")
nametuple=tuple(namelist)
print(nametuple)

#Q15.Create two tuples and concatenate them using += operator

firstname=("Ragini","Dipti","Anushka")
lastname=("Dighe","Bhawar","Kakade")
firstname += lastname
print(firstname)

#Q16.Convert a tuple to list, change the second element, and convert back to tuple

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist[1]="Rinal"
nametuple=tuple(namelist)
print(nametuple)

#Q17.Create a tuple and access elements using both positive and negative indexing

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
print(nametuple[0])
print(nametuple[2])
print(nametuple[-1])
print(nametuple[-2])

#Q18.Create a tuple of 7 elements and print its middle element

nametuple=("Ragini","Dipti","Khushbu","Anushka","Bhakti","Rinal","Jayashri")
print(nametuple[3])

#Q19.Create a tuple and try to change one value directly (observe and write the error)

# nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
# nametuple[1]="Rinal"
# print(nametuple)
# #TypeError: 'tuple' object does not support item assignment

#Q20.Write a program that takes a tuple, converts it to list, replaces the last element, and converts back to tuple.

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist[-1]="Jayashri"
nametuple=tuple(namelist)
print(nametuple)

#Q21.Create a tuple of 10 numbers and extract the middle 5 elements using slicing

tuplenum=(1,2,3,4,5,6,7,8,9,10)
print(tuplenum[2:7])

#Q22.Write a program to check if a value exists in a tuple before accessing its index

tuplenum=(1,2,3,4,5,6,7,8,9,10)
print(20 in tuplenum)

#Q23.Create a tuple, convert it to list, remove one item, and convert it back to tuple

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist.remove("bhakti")
nametuple=tuple(namelist)
print(nametuple)

#Q24.Write a program that accepts a tuple, converts it to list, inserts a value at index 2, and converts back to tuple

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
namelist=list(nametuple)
namelist.insert(2,"Rinal")
nametuple=tuple(namelist)
print(nametuple)

#Q25.Create a tuple and demonstrate slicing with positive and negative indexes in one program

tuplenum=(1,2,3,4,5,6,7,8,9,10)
print(tuplenum[0:3])
print(tuplenum[-3:])
print(tuplenum[-6:-1])
print(tuplenum[1:])
print(tuplenum[::-1])

#Q26. Write a complete program that :-
# *creates a tuple
# * prints its length
# * accesses elements
# * slices it
# * converts to list
# * updates a value
# * converts back to tuple

nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
print(len(nametuple))
print(nametuple[1])
print(nametuple[3])
print(nametuple[1:4])


namelist=list(nametuple)
namelist[1]="Rinal"
nametuple=tuple(namelist)
print(nametuple)

#Q27.Write a program that takes two tuples, adds them, and prints the final result

firstname=("Ragini","Dipti","Anushka")
lastname=("Dighe","Bhawar","Kakade")
result=firstname+lastname
print(result)

#Q28.Create a tuple, delete it using del , and then try to print it (observe the error)

# nametuple=("Ragini","Dipti","Khushbu","Anushka","bhakti")
# del nametuple
# print(nametuple)

#Q29. A school stores a student’s basic details in a tuple because the data should not be changed accidentally.
#        The tuple contains: student = ("Rahul", 10, "A", 85.5)
#        Write a program to:
# 1. Print the student’s name and class using indexing.
# 2. Check whether "A" exists in the tuple.
# 3. Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
# 4. Print the final updated tuple


student = ("Rahul", 10, "A", 85.5)

# 1. Print the student’s name and class using indexing.
print(student[0])
print(student[1])
print(student[0:2])

# 2. Check whether "A" exists in the tuple.
print("A" in student)

# 3. Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
studentlist=list(student)
studentlist[3]=90.0
student=tuple(studentlist)
print(student)

#Q30.30. A customer’s selected product prices are stored in a tuple:
#       prices = (250, 500, 750, 1000, 1250)
#        Write a program to:
# 1. Print the total number of items using len().
# 2. Print the first and last price using positive and negative indexing.
# 3. Extract the middle three prices using slicing.
# 4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
# 5. Print the final tuple

prices = (250, 500, 750, 1000, 1250)
print(len(prices))

# 2. Print the first and last price using positive and negative indexing.
print(prices[0])
print(prices[-1])

# 3. Extract the middle three prices using slicing.
print(prices[1:4])

# 4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
prices = (250, 500, 750, 1000, 1250)
priceslist=list(prices)
priceslist.append(1500)
prices=tuple(priceslist)
print(prices)

 #Print the final tuple

print(prices)