# Personal Information

# fullname=input("Enter the full name:")
# age=int(input("Enter the age:"))
# gender=input("Enter the Gender:")
# city=input("Enter the City:")
# State=input("Enter the State:")
# country=input("Enter the Country:")
# email=input("Enter the Email:")
# phone=input("Enter the Phone Number:")

# Simple Billing System

# Name=input(" Customer Name:")
# pens=10
# print("Pens:",pens)
# Notebook=50
# print("Notebook:",Notebook)A
# Bag=700
# print("Bag:",Bag)
# TotalAmount=pens+Notebook+Bag
# print("Total Amount:",TotalAmount)
# GST=(TotalAmount*5)/100 
# print("GST(5%):",GST)
# print("Final Amount:",TotalAmount+GST)

# Append()

# Q1.. Write a program to add 10 user-entered integers into a list using append().


# numlist=[]

# for i in range(1,11):
#     num=int(input("Enter the integer:"))
#     numlist.append(num)

# print("Number List:",numlist)


# Q2. Append only even integers from 1 to 20 into a list.

# EvenNum= []

# for num in range(1, 21):
#      if num % 2 == 0:
#          EvenNum.append(num)

# print("Even numbers list:", EvenNum)

# Q3.Append the square of each integer from an existing list into a new list.

# numlist=[2,3,4,5,6]
# Square=[]

# for i in numlist:
#     Square.append(i*i)

#     print("Square list:",Square)


# Q4. Take integer input until the user enters `0` and append each value to a list.


# Q5.Append elements of a tuple `(5, 10, 15)` one by one into a list.

# numTuple=(5,10,15)
# lst=[]
# lst.append(numTuple[0])
# lst.append(numTuple[1])
# lst.append(numTuple[2])
# print(lst)

# clear method()
    
# #Q1.Write a program to clear all elements from an integer list.

# numList=[1,2,3,4,5]
# numList.clear()
# print(numList)

# #Q2.Clear a list only if it contains more than 5 integers

# numList=[1,2,3,4,5]
# if len(numList)>5:
#     numList.clear()
# print(numList)

# #Q3.Display all elements of a list and then clear it.


# numList=[1,2,3,4,5]
# print(numList)
# numList.clear()
# print(numList)

# Q4.Clear a list and then add 3 new integer values to it

# numList=[1,2,3,4,5]
# numList.append(6)
# numList.append(7)
# numList.append(8)
# print(numList)

# Q5.Clear a list inside a function and print the list outside the function.




# copy method

# Q1.. Copy all elements of one integer list into another list using copy()

# numList1=[1,2,3,4,5]
# numList2=numList1.copy()
# print(numList2)

# #Q2.. Copy a list and add new integers to the copied list without affecting the original.

# numList1=[1,2,3,4,5]
# numList2=numList1.copy()
# numList2.append(10)
# print(numList2)

# #Q3.Copy a list and remove an element from the copied list.

# numList1=[1,2,3,4,5]
# numList2=numList1.copy()
# numList2.remove(2)
# print(numList2)


# Count method

# Q1.Count how many times the integer 5 appears in a list.

# numbers=[1,2,3,4,5,6,7,5,2,5,8,5]
# print(numbers.count(5))

# #Q2.. Count the occurrences of a user-entered integer in a list

# numList=[1,2,3,4,3,2,5,6,5,6,1,2]
# # num=int(input("Enter a number:"))
# # count=numList.count(num)
# # print(count)

# #Q3.Count how many times an even number appears in a list.

# numList=[1,4,6,3,7,6,9,8,10]
# count=0
# for num in numList:
#     if num % 2==0:
#         count+=1
# print(count)

# #Extebd method


# #Q1.. Extend a list with another integer list entered by the user

# num1=[1,2,3,4,5]
# num2=map(int,input("Enter a numbers:"))
# num1.extend(num2)
# print(num1)

# Q2.Extend a list using a tuple of integers.

# numList=[1,2,3,4]
# numTuple=(5,6,7)
# numList.extend(numTuple)
# print(numList)

# #Q3.Extend an empty list with integers from range 1 to 5.

# emptyList=[]
# lst=[1,2,3,4,5]
# emptyList.extend(lst)
# print(emptyList)


# Index method

# Q1. . Find the index of a given integer in a list

# lst=[1,2,3,4,5,6]
# print(lst.index(2))

# Q2.Find the index of the first occurrence of integer 10 in a list

# lst=[1,2,3,4,5,6,10,3,45,6,10,2,10]
# print(lst.index(10))


# #Q3.Take an integer from the user and display its index in the list.

# lst=[10,20,30,40,50]
# num=int(input("Enter Integer:"))
# if num in lst:
#     index=lst.index(num)
#     print(index)



# Inset method

# Q1.Insert an integer at the beginning of a list

# lst=[10,20,30,40,50]
# lst.insert(0,100)
# print(lst)


# Q2.. Insert an integer at a specific index entered by the user.

# lst=[11,22,33,44,55]
# index=int(input("Index:"))
# value=int(input("values:"))
# lst.insert(index,value)
# print(lst)

# Q3.Insert the integer 100 at index 3.

# lst=[11,22,33,44,55]
# lst.insert(3,100)
# print(lst)

# #pop method

# #Q1.Remove the last integer from a list using pop()

# lst=[11,22,33,44,55]
# lst.pop(4)
# print(lst)


# #2. Remove the integer at index 2 using pop().

# lst=[11,22,33,44,55]
# lst.pop(2)
# print(lst)

# #Q3.Pop all integers from a list one by one.


# lst = [11, 22, 33, 44, 55]
# for i in range(len(lst)):
#     value = lst.pop()
#     print("Popped:", value)

# print("Final list:", lst)



# #Remove method

# #Q1.Remove a specific integer value from a list.

# lst = [11, 22, 33, 44, 55]
# lst.remove(22)
# print(lst)

# #Q2.. Remove the first occurrence of integer 10 from a list.

# lst = [11, 22,10,33, 44, 55,10]
# lst.remove(10)
# print(lst)

# #3. Remove all occurrences of a given integer from a list.

# Reverse method

# Q1.. Reverse an integer list using reverse().

# lst = [11, 22, 33, 44, 55]
# (lst.reverse())
# print(lst)

# #Q2.Reverse a list of integers without creating a new list

# lst = [11, 22, 33, 44, 55]
# lst.reverse()
# print(lst)

# Q3.Reverse a list inside a function.


# def reverseList(lst):
#     lst.reverse()
#     num=[10,20,30,40]
#     reverseList(num)
#     print(num)

# Sort method

# Q1.. Sort a list of integers in ascending order

# lst=[1,4,6,5,3,0,2,9,8]
# lst.sort()
# print(lst)


# #Q2. Sort a list of integers in descending order

# lst=[1,4,6,5,3,0,2,9,8]
# lst.sort(reverse=True)
# print(lst)

# #Q3.. Sort a list and display the smallest integer.


# lst=[1,4,6,5,3,0,2,9,8]
# lst.sort()
# print(lst)

# Q2.Clear a list only if it contains more than 5 integers

# lst=[1,2,3,4,5]
# if len(lst)>5:
#     lst.clear()
# print(lst)


