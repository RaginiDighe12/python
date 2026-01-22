#Q1.Write a Python program to create a list of 5 student names and print it

student=["Ram","shyam","ganesh","Radha","priya"]
print(student)

#Q2. Write a program to find the length of a list using len()

student=["Ram","shyam","ganesh","Radha","priya"]
print(len(student))

#Q3.Create a list with mixed data types and print all elements one by one

info=["Ragini","Anurag",2,True,5,False,3+4j]
print(info[0])
print(info[1])
print(info[2])
print(info[3])
print(info[4])
print(info[5])
print(info[6])

#Q4.Write a program to access the first and last element of a list.


student=["Ram","shyam","ganesh","Radha","priya"]
print(student[0])
print(student[-1])

#Q5.Create a list and print the element using negative indexing.

student=["Ram","shyam","ganesh","Radha","priya"]
print(student[-1])
print(student[-2])
print(student[-3])
print(student[-4])
print(student[-5])

#Q6.Write a program to check whether "Chetan" exists in a list

student=["Ram","shyam","ganesh","Radha","priya"]
print("chetan" in student)

#Q7. Write a program to change the second element of a list.

student=["Ram","shyam","ganesh","Radha","priya"]
student[1]="John"
print(student)

#Q8.Create an empty list and append three values to it

student=[]
student.append("Ragini")
student.append("Anurag")
student.append("Richa")
print(student)

#Q9.Write a program to remove the last element from a list


student=["Ram","shyam","ganesh","Radha","priya"]
student.remove("priya")

#Q10. Create a list and clear all its elements using a method

student=["Ram","shyam","ganesh","Radha","priya"]
student.clear()

#Q11.Write a program to slice a list from index 2 to 5

student=["Ram","shyam","ganesh","Radha","priya"]
print(student[2:5])

#Q12.Write a program to replace the first two elements of a list using range assignment

student=["Ram","shyam","ganesh","Radha","priya"]
student[0:2]=("Ragini","Anurag")
print(student)

#13.Create two lists and join them using the + operator

firstName=["Ragini","Rinal","Dipti"]
lastName=["Dighe","Shinde","Bhawar"]
Name=firstName+lastName
print(Name)

#14.Write a program to insert an element at index 3 in a list

student=["Ram","shyam","ganesh","Radha","priya"]
student.insert(3,"Shreya")
print(student)

#15. Write a program to extend a list using:
#another list
#a tuple

firstName=["Ragini","Rinal","Dipti"]
lastName=["Dighe","Shinde","Bhawar"]
rollno=(1,2,3,4)

firstName.extend(lastName)
print(firstName)

firstName.extend(rollno)
print(firstName)

#Q16.Write a program to remove a specific value from a list using remove()

student=["Ram","shyam","ganesh","Radha","priya"]
student.remove("Radha")
print(student)

#17.Write a program to sort a list of integers in ascending order

number=[34,54,0,78,12,32,6,2,65,7]
number.sort()
print(number)

#Q18.Write a program to sort a list of integers in descending order

number=[34,54,0,78,12,32,100,2,65,7]
number.sort(reverse=True)
print(number)

#Q19.Write a program to reverse a list using an inbuilt method

student=["Ram","shyam","ganesh","Radha","priya"]
student.reverse()
print(student)

#Q20.Write a program to copy a list using the copy() method and show that changes in the original list do not affect the copied list

rollno=[11,12,13,14,15]
print("old rollno:",rollno)

newrollno=rollno.copy()
rollno.append(2)
print("new roll no:",newrollno)
print("old roll  on:",rollno)



#Q21.Write a program to extend a list using a dictionary and print the result

namelist=["Ragini","Anurag","Rinal","Dipti"]
dictlist= {
  1:"Anushka",
  2:"Bhakti",
  3:"Khushabu"
}
namelist.extend(dictlist)
print(namelist)

#Q22.Write a program to demonstrate that list2 = list1 creates a reference, not a copy.

list1=[1,2,3,4,5]
list2=[1,2,3,4,5,6]
list1=list2
list2.append(8)
print("after appending:",list2)
print("after appending",list1)


#Q23.Write a program to sort a list containing both uppercase and lowercase letters alphabetically

list=["a","D","R","z","m","O"]
list.sort()
print(list)

#Q24.Write a program to sort a list containing uppercase and lowercase letters together using key=str.lower

list=["a","D","R","z","m","O","f"]
list.sort(key=str.lower)
print(list)

#Q25.Write a program to remove the element at index 4 using pop().

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.pop(4)
print(namelist)

#Q26.Write a program to delete the third element of a list using the del keyword.

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
del namelist[2]
print(namelist)

#Q27.Write a program to count how many times a specific value occurs in a list

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka","Ragini","Anurag","Ragini"]
print(namelist.count("Ragini"))

#Q28.Write a program to find the index of a specific element in a list

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
print(namelist.index("Anurag"))

#Q29.Write a program to add elements of a set to a list using extend()

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
nameset={"Khushabu","jayashri","Akshata"}
namelist.extend(nameset)
print(namelist)

#Q30. Write a program that performs the following operations on a list:

# *append
# * insert
# * remove
# * sort
# * revers

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.append("Khushabu")
print(namelist)
namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.insert(0,"Saisha")
print(namelist)
namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.remove("Rinal")
print(namelist)
namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.sort()
print(namelist)

namelist=["Ragini","Anurag","Rinal","Dipti","Anushka"]
namelist.reverse()
print(namelist)
