#Q1.Store your name in a string variable and print it using f-string.

string="Ragini"
print(f"My name is {string}")

#Q2.Print your city name using string concatenation.


city="Akole"
print("I am from " +city)

#Q3.Print: "Hello" and "World" on two separate lines using escape character

print("Hello \nWorld")

#Q4.Print a sentence that contains a single quote using escape character

print("My name is Ragini and I\'m from Akole")

#Q5.Print a tab space between two words using escape character

print("Hello\tWorld")

#Q6.Check and print the boolean value of 100

num=100
print(bool(num))

#Q7.Check and print the boolean value of 0.

print(bool(0))

#Q8. Compare two numbers and print whether first is greater than second.

a=10
b=5
print( "first is greater then second:",a>b)

#Q9.Add two numbers and print the result.
num1=4
num2=3
result=num1+num2
print(result)

#Q.10.Multiply two numbers and print the result.

a=2
b=3
result=a*b
print(result)

#Q11.Find remainder of 25 divided by 4.

a=25
b=4
print(a%b)

#Q12.Use += operator to increase a variable by 10.

num=1
num +=10
print(num)

#Q13.Use -= operator to decrease a variable by 5

num=10
num -=5
print(num)

#Q14.Compare two numbers using == operator and print result

a=10
b=10
result=a==b
print(result)

#Q15.Use logical and to check if a number is greater than 10 and less than 20

num=15
print(num>5 and num<20)

#Q16.Take two numbers from user and print sum, difference, product, and division.

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#Q17.Print a formatted string that includes name and age using f-string

name="Ragini"
age=21
print(f"My name is {name} and age is {age}")

#18.Check whether a number entered by user is greater than 50 and print True/False
num=int(input("Enter the number:"))
print(num>50)

#Q19.Use logical or to check if a number is less than 10 or greater than 100

num=9
print(num<10 or num>100)

#Q20.Use logical not to reverse a comparison result.

a=10
b=10
print(not(a==b))

#Q21.Use identity operator is to compare two variables referencing same list.

list1=[1,2,3]
list2=[1,2,3]

print(list1 is list2)

#Q22.Use identity operator is not to compare two different lists.

list1=[1,2,3]
list2=[1,2,3,4]
print(list1 is not list2)

#Q23.Perform bitwise AND on two numbers 5 and 3

a=5
b=3
print(a & b)

#24.Perform bitwise OR on two numbers 7 and 4.

a=7
b=4
print(a | b)

#Q25.Perform bitwise XOR on two numbers 6 and 2.

a=6
b=2
print(a^b)

#26. Take three numbers and evaluate. a + b * c - a // b ** 2  and print the result following operator precedence

a=3
b=2
c=4
result=a+b*c-a//b**2
print(result)

#27. Take a number from user and check:
#* It is greater than 10
#* It is even
#  Print result using logical and

num=int(input("Enter the number:"))
print(num>10 and num%2==0)

#Q28.Create two lists, assign one list to another variable, then check identity using is and print result

list1=[1,2,3,4]
list2=[1,2,3]
list1=list2
print(list2 is list1)

#Q29.Take two integers, convert them to binary using bitwise operations, then perform AND, OR, and XOR and print results

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("Binary of a:",bin(a))
print("Binary of b:",bin(b))

print(num1&num2 ,"binary:",bin(a&b))
print(num1|num2 ,"binary:",bin(a|b))
print(num1^num2 ,"binary:",bin(a^b))

#30. Write a program that:
# Takes two numbers
# Uses arithmetic, comparison, logical, and assignment operators in one program
#Prints at least 6 different outputs

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a==b)
print(a!=b)
print(a and b)
print(a or b)
print(a>b)
print(a<=b)