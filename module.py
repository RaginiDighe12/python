# num1=int(input("Enter the num1:-"))
# num2=int(input("Enter the num2:-"))
# def add(n1,n2):
#     print("Addition of two number is:",n1+n2)
# obj=add(num1,num2)

# def greet():
#     print("Hello Ragini")
# obj=greet()


# def greet():
#     print("Hello Ragini")
# obj=greet()

# n1=10
# n2=5
# def mul(num1,num2):
#     print("Multiplication of two number:",num1*num2)
# obj=mul(n1,n2)

# def greet(count):
#     if count==0:
#         return
#     print("Hello Ragini")
#     greet(count -1)
# obj=greet(5)

# def greet(name):
#     print("Hello",name)
# obj=greet("Ragini")

# def add(n1,n2):
#     return(n1+n2)

# result=add(2,3)
# # print(result)

# def check_even_odd(num):
#     if num%2==0:
#         return "Even number"
#     else:
#         return "Odd number"
# result=check_even_odd(4)
# print(result)

def greater_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
obj=greater_num(2,3,5)
print(obj)