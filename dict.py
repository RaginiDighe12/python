# keys=[1,2,3,4]
# d=dict.fromkeys(keys,1)
# print(d)

# keys=(10,20,30,40,50)
# d=dict.fromkeys(keys,12)
# print(d)

# student = {'name': 'Ragini',"city": "Akole","age":21}
# student.update({"marks":40})
# print(student)
# student[1]="one"
# print(student)
# print(student["name"])
# print(student["city"])
# print(type(student))    

# numbers=[1,2,3,2,4,5,2]
# count={}
# for n in numbers:
#     d=numbers.setdefault(n,2)
#     count[n]+=1
# print(count)

# data = {

#     "employees": [
#         [
#             "id", 101,
#             "name", "Alice",
#             "skills", ["Python", "SQL", "GCP"],
#             "projects", [
#                 {"project_id": "P1", "status": "Completed"},
#                 {"project_id": "P2", "status": "Ongoing"}
#             ],


#             ["id", 102,
#             "name", "Bob",
#             "skills", ["Python", "SQL", "GCP"],
#             "projects", [
#                 {"project_id": "P1", "status": "Completed"},
#                 {"project_id": "P2", "status": "Ongoing"}]
#             ]
#         ]
#     ]
# }

# list=data["employees"][0][8]
# print(list[0:2])
# print(list[2:4])
# print(data["employees"][0][8])

# name={"Ragini","Anu",4+2j}
# name.remove("ragini")
# name.discard("ragini")
# print(name)
# name.pop()
# print(name)

# name.clear()
# print(name)
# del name
# print(name)


# name=["Ragini","Anu",4+2j]
# lstname=list(name)
# print(lstname)
# lstname.insert(0,1)
# print(lstname)
# name=tuple(lstname)
# lstname.append("mona")
# name=tuple(lstname)
# print(name)

# name1=[1,2,3,4,5]
name=["Ragini","Anu","rinal","Bhakti","Dipti","anu","eagle"]
# print(name.index(4+2j))
# print(name.count("Anu"))
# name.reverse()
# print(name)

# name.sort()
# name.sort(reverse=True)
# name.sort(key=str.lower)
# name.insert(4,"isha")
# print(name)

name="Ragini"
age=21
print(f"my name is {name} a and age is {age}")
