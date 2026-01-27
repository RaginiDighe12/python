# file = open("student.txt", "w")
# file.write("Name: Ragini\n")
# file.write("Course: Python\n")
# file.write("Level: Beginner\n")
# file.close()

# print("Data written successfully")

  
   
with open("Demo.txt","a")as f:
    f.write("\nHelloRagini")
    f.write("\nI am learning python and html")
    f.write("\nAlso try to understand django further for industries purpose")

    print("Data written successfully")

with open("student.txt","r+")as f:
    print("before:",f.read())

    f.write("Public:Anurag")
print("Successful")