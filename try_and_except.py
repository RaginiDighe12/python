# try:
#     num1=int(input("Enter the num1:-"))
#     num2=int(input("Enter the num2:-"))
#     result=num1/num2
#     print("Result:",result)
# except:
#    print("Error:cannot divided by 0")

try:
    age=int(input("Enter the number:-"))
    print("ypur age is:",age)
except ValueError:
    print("Please enter the valid age")

