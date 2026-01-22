# Q1.Write a program to check whether a number is positive or negative

a=int(input("Enter the number:-"))
if a>0:
    print(f"{a} is Positive.")
else:
    print(f"{a} is Negative")

# Q2.Write a program to check if a number is greater than 100.

num=int(input("Enter the Number:-"))
if num>100:
    print(f"{num} is greater than 100")

# Q3.Write a program to check whether a given number is even or odd

num=int(input("Enter the number:-"))
if num%2==0:
    print(f"{num} is Even")
else:
    print(f"{num} is odd")

# Q4.Write a one-line if statement to check if a number is less than 50

num=int(input("Enter the Number:-"))
if num<50: print(f"{num} is less than 50")

#Q5.Write a program to check whether a person is eligible to vote (age ≥ 18)

age=int(input("Enter the age:-"))
if(age>=18):
    print("Person is eligible for vote")
else:
    print("Person is not eligible for vote")

# Q6.Write a program to check whether a number is positive, negative, or zero

num=int(input("Enter the number:-"))
if num>0:
    print(f"{num} is positive")
elif(num<0):
    print(f"{num} is negative")
else:
    print("Zero")

# Q7.Write a program to check the largest of two numbers

a=int(input("Enter first number:-"))
b=int(input("Enter Second number:-"))
if a>b:
    print(f"{a} is largest number")
else:
    print(f"{b} is largest number")

# Q8.Write a program to check the largest of three numbers using if-elif

num1=10
num2=20
num3=44
if num1>num2:
    print("num1 is greater")
elif num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")

# Q9.Write a program to check whether a year is a leap year.

year=int(input("Enter the year:-"))
if year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")

# Q10.Write a program to check if a student passed or failed (marks ≥ 40).

marks=int(input("Enter the marks:-"))
if marks>=40:
    print("Student pass in exam")
else:
    print("student failed in exam.")

# Q11. Write a program to assign grades:
# ≥90 → A
#  ≥75 → B
#  ≥60 → C
#  Else → Fail

grade=int(input("Enter the grade:-"))
if grade>=90:
    print("A grade")
elif grade>=75:
    print("B grade")
elif grade>=60:
    print("C grade")
else:
    print("Failed in Exam")

# Q12.Write a program to check whether a number lies between 10 and 50 using and.

num=int(input("Enter the number:-"))
if (num>=10 and num<=50):
    print(f"{num} is lies between 10 and 50")
else:
      print(f"{num} is  not lies between 10 and 50")



# Q13.Write a program to check whether at least one condition is true using or.

num1=int(input("Enter the number:-"))
if (num1<10 or num1>20):
    print("first condition is true")
else:
    print("second condition is true")


# Q14. Write a program to check login:
# username = "admin"
# password = "1234

username = "admin"
password = "1234"
if username=="admin":
    if password=="1234":
       print(f"if username is {username} and password is {password}, then user can login.")
    else:
        print(f"if username is {username} and password is {password}, then user cannot  login.")

# Q15.Write a program to check if a number is divisible by 3 and 5.

num=int(input("Enter the number:-"))
 
if (num%3==0 and num%5==0):
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

# Q16. Write a nested if program to check:
# gender = female
# age ≥ 18 → Can vote

gender=input("Enter the gender:-")
age=int(input("Enter th age:-"))

if gender=="female":
    if age>=18:
        print("person can vote")

# Q17.Write a program to check whether a character is a vowel or consonant

ch=input("Enter the character:-").lower()

match ch:
    case 'a'|'e'|'i'|'o'|'u':
        print(f"{ch} is vowels")
    case _:
        print(f"{ch} is consonant")

# Q18.Write a one-line if-else to check pass/fail

marks=int(input("Enter the marks:-"))
print("Pass in Exam")if marks>60 else print("Failed in Exam")

# Q19.Write a program using not operator to reverse a condition

num1=int(input("Enter the num1:-"))
num2=int(input("Enter the num2:-"))
if not num1>num2:
    print(f"{num1} is not less than {num2}")

# Q20.Write a program that uses pass inside an if block and print “Thank you” in else

a=12
b=21

if a>b:
    pass
else:
    print("Thank you")

# Q21.Write a program using match to print the day name for numbers 1–7

day=int(input("Enter the number:-"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")

# Q22.Write a program using match to build a simple calculator (+, -, *, /)

num1=int(input("Enter the num1:-"))
num2=int(input("Enter the num2:-"))
operator=input("Enter the operator('+','-','/','*'):-")

match operator:
    case '+':
        print("Result=",num1+num2)
    case '-':
        print("Result=",num1-num2)
    case '*':
        print("Result=",num1*num2)
    case '/':
        if num2!=0:
            print("Result=",num1/num2)
    case _:
        print("Invalid operator.")
    

# Q23. Write a program to categorize age:
# <13 → Child
# 13–19 → Teen
# 20–59 → Adult
# 60+ → Senior

age=int(input("Enter the age:-"))

if age<13:
    print("Child")
elif (age>=13 and age<=19):
    print("Teenager")
elif(age>19 and age<=59):
    print("Adult")
else:
    print("Senior")


# Q24.Write a program using match to check month name from month number

month=int(input("Enter the number(1-12):-"))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")

# Q25.Write a program using a match with a default case and print “Month number is not present”

month=int(input("Enter the number:-"))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Month is not present")    

# Q26.Write a program to check traffic signal colors and print actions.

color=input("Enter the color('red','yellow','green'):-").lower()

match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Ready to go")
    case _:
        print("Invalid traffic signal")

# Q27.Write a program using match to classify student group based on name list.


name=input("Enter the name:-").lower()

match name:
    case "anu"|"alice"|"akshu"|"amol":
        print("Student belong to A group")
    case "bob"|"bindu"|"bablu":
        print("Student belong to B group")
    case "charlie"|"cherry"|"chotu":
        print("Student belong to C group")
    case _:
        print("Student do no belong to any group")

# Q28. Write a program to check eligibility for a job:
# Age ≥ 21
# Degree = Yes
# Experience ≥ 1 year

age = int(input("Enter your age: "))
degree = input("Do you have a degree? (Yes/No): ").lower()
experience = int(input("Enter your years of experience: "))

if age >= 21 and degree == "yes" and experience >= 1:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

# Q29.Write a program using match with multiple values in one case.

number=int(input("Enter the number:-"))


match number:
    case 1|2|3|4|5|6|7|8|9|10:
        print("Numbers lies between 1 and 10")
    case 11|12|13|14|15|16|17|18|19|20:
        print("Number lies between 11 and 20")
    case 21|22|23|24|25|26|27|28|29|30:
        print("Number lies between 21 and 30")
    case _:
        print("Different Numbers.")


    















