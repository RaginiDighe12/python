#Q1.Create a dictionary with keys name, rollNo, and address and print it

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(data)

#Q2.Write a program to access and print the value of key name from a dictionary


data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(data["name"])

#Q3.Create a dictionary and print its length using len()

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(len(data))

#Q4.Write a program to check the type of a dictionary using type()

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(type(data))

#Q5.Create a dictionary with two keys and print all its values

data={
    "name":"Ragini",
    "rollno":21,
}

print(data["name"])
print(data["rollno"])

#Q6.Create a dictionary and access values using both [] and get() methods

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(data["name"])
print(data.get("rollno"))

#Q7.Write a program to add a new key-value pair to an existing dictionary

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data["marks"]=50
print(data)


#Q8.Create a dictionary and update one value using the update() method

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data.update({"rollno":12})
print(data)

#Q9.Write a program to remove a key using the pop() method.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data.pop("name")
print(data)

#Q10.Create a dictionary and remove the last inserted item using popitem()

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data.popitem()
print(data)

#Q11.Write a program to print all keys using the keys() method.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print(data.keys())

#Q12.Write a program to print all values using the values() method.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}

print(data.values())

#Q13.Create a dictionary and print all key-value pairs using items(

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}

print(data.items())

#Q14.Convert a tuple of key-value pairs into a dictionary using dict()

nameTuple=((1,"one"),(2,"Two"),(3,"Three"),(4,"Four"))
tupleTodict=dict(nameTuple)
print(tupleTodict)

#Q15.Write a program to check if a key exists in a dictionary.


data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
print("name" in data)

#Q16.Create a dictionary with duplicate keys and print the output.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":30,
    "marks":40,
    "marks":50
}
print(data)

#Q17.Write a program to delete a specific key using the del keyword.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
del data["address"]
print(data)

#Q18.Write a program to delete the entire dictionary using de

# data={
#     "name":"Ragini",
#     "rollno":21,
#     "address":"Akole"
# }
# del data
# print(data)

#Q19.Create a dictionary and empty it using the clear() method

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}

data.clear()
print(data)

#Q20.Copy a dictionary using the copy() method and show both dictionaries

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data1=data.copy()
data1.pop("name")
print("Original dic:",data)
print("copy dic:",data1)


#Q21.Copy a dictionary using the dict() constructor and modify the original dictionary.

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"
}
data1=dict(data)
data.pop("name")
print("Original dict:",data)
print("copy dict:",data1)

#Q22.Write a program to demonstrate why dict1 = dict2 is not a proper copy

dict1={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"

}
dict2=dict1

dict2["name"]="Dipti"
print("original:",dict1)
print("copy",dict2)

#dict1=dict2 create a reference not a copy

#Q23.Create a dictionary and add multiple items using assignments

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole"

}
data["marks"]=40
data["state"]="Maharashtra"
data["city"]="pune"
print(data)

#Q24.Write a program to remove multiple keys one by one using pop()

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":50,
    "State":"Maharashtra"
}
data.pop("marks")
data.pop("State")
print(data)

#Q25.Use fromkeys() to create a dictionary with default values.


keys=[10,20,30,40,50]
new=dict.fromkeys(keys,1)
print(new)

#Q26.Write a program to access a missing key using get() without error

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":50,
    "State":"Maharashtra"
}

data.get("city")
print(data)

#Q27.Create a dictionary and print key-value pairs in tuple form

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":50,
    "State":"Maharashtra"
}

print(data.items())

#Q28.Write a program to update multiple values using update().

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":50,
    "State":"Maharashtra"
}
data.update({"name":"Anu"})
data.update({"rollno":12})
data.update({"address":"virgoan"})
print(data)

#Q29.Create a dictionary and check membership of a key using in

data={
    "name":"Ragini",
    "rollno":21,
    "address":"Akole",
    "marks":50,
    "State":"Maharashtra"
}
print("marks" in data)

#Q30.Write a program that creates a dictionary from tuples and accesses values using keys

nameTuple=((1,"one"),(2,"two"),(3,"Three"),(4,"four"))
tupleToDict=dict(nameTuple)
print(tupleToDict)
print(tupleToDict[1])
print(tupleToDict[3])
