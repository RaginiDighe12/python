# Q1.Write a program to print all odd numbers from 1 to 50, but skip numbers divisible by 5 using continue

# for i in range(1,50):
#     if i%2!=0:
#         if i%5==0:
#           continue
#         else:
#            print(i)
#         i+=1

# Q2.Write a for loop that prints numbers from 1 to 100, but stops completely when a number divisible by both 7 and 9 is found

# for i in range(1,101):
#     if i%7==0 and i%9==0:
#         break
#     else:
#         print(i)
        

# Q3.Using a while loop, print numbers from 10 to 1, but skip number 6

# num=10
# while(num>=1):
#     if num==6:
#        num-=1
#        continue
#     print(num)
#     num-=1


# Q4.Write a program to iterate through a list of names and stop printing once the name "admin" is found

# name=["Ragini","Anurag","Dipti","admin","Rinal"]
# for i in name:
#     if i=="admin":
#         break
#     print(i)

# Q5.Write a program to print the first 5 even numbers using a while loop

# i=1
# while(i<=10):
#     if i%2==0:
#         print(i)
#     i+=1

# Q6.Write a loop that prints characters of a string, but does not print vowels

# name="python"
# for ch in name:
#     if ch in "aeiou":
#         continue
#     print(ch)

# Q7.Write a program using for loop and else to check whether a number exists in a list

# number=[1,2,3,4,5,6]
# n=int(input("Enter the number:-"))
# for num in number:
#     if num==n:
#         print(f"{n} is exist in list")
# else:
#     print(f"{n} not exist in list")

# Q8.Write a program that prints numbers from 1 to 20, but prints "Skipped" instead of the number 13.

# i=1
# while(i<=20):
#     if i==13:
#         print("Skipped")
#     else:
#         print(i)
#     i+=1
       

# Q9.Write a loop that prints numbers from 1 to 10, but uses pass for even numbers

# for i in range(1,10):
#     if i%2==0:
#         pass
#     else:
#         print(i)

# Q10.Write a program that counts how many numbers between 1 and 100 are divisible by 3.

# count=0
# for i in range(1,101):
#     if i%3==0:
#         count+=1
# print("Total number divisible by 3 is:-",count)

# Q11.Write a program to find the first number between 1 and 1000 that is divisible by 11 and 13, then stop the loop

# for i in range(1,1000):
#     if i%11==0 and i%13==0:
#         print(i)
#         break
    

# 12. Write a program that prints all numbers from 1 to 100, but:
# Skip multiples of 3
# Stop if a number divisible by 17 appears

# for i in range(1,100):
#     if i%3==0:
#         continue
#     elif i%17==0:
#         break
#     print(i)


# Q13.Using a while loop, keep taking numbers from the user until they enter 0, then print how many numbers were entered.

# count=0
# while True:
#    num=int(input("Enter the number:-"))
#    if num==0:
#       break
#    count+=1
# print(count)

# Q14.Write a program to check whether a given number is prime, using a loop and break.

# num=int(input("Enter the number:-"))
# if num<=1:
#     print("Not a prime number.")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not prime number.")
#             break
#     else:
#             print("prime number")/

# Q15.Write a program that prints a triangle pattern using nested for loops

# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# Calculator


# while True:
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division")

#     option=input("Enter the option(1-4):")

#     match option:
#         case '1':
#             num1=int(input("Enter the num1:-"))
#             num2=int(input("Enter the num2:-"))
#             print("Result:-",num1+num2)
#         case '2':
#             num1=int(input("Enter the num1:-"))
#             num2=int(input("Enter the num2:-"))
#             print("Result:-",num1-num2)
#         case '3':
#             num1=int(input("Enter the num1:-"))
#             num2=int(input("Enter the num2:-"))
#             print("Result:-",num1*num2)
#         case '4':
#             num1=int(input("Enter the num1:-"))
#             num2=int(input("Enter the num2:-"))
#             print("Result:-",num1/num2)
        
#             break
        

# Q16.Write a program to iterate through a list of integers and print **only the first negative number, then stop

# number=[1,2,3,-5,4,-6]
# for num in number:
#     if num<0:
#         print("**")
#         break
#     else:
#         print(num)

   
# Q17.Write a program using for-else to check if a number is present in a range from 1 to 50

# num=int(input("Enter the number:-"))
# for i in range(1,50):
#     if num==i:
#      print("number is present in given range.")
#      break
# else:
#    print("not present")


# Q18.Write a program that skips all numbers divisible by 4, but prints all others from 1 to 40

# for i in range(1,40):
#     if i%4==0:
#         continue
#     else:
#         print(i)

# Q19.Write a program that finds the “sum of numbers until the sum becomes greater than 100”, then stops

# sum=0
# while(sum<=100):
#     num=int(input("Enter the number:-"))
#     sum+=num
#     print(sum)

# Q20. Write a program that prints numbers from 1 to 100, but replaces:

#  multiples of 3 → "Fizz"
#  multiples of 5 → "Buzz"
#  multiples of both → "FizzBuzz"

# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

# Q21. Login Attempts System
#     A user gets 3 attempts to enter the correct password.
#     Stop the loop if the password is correct, otherwise block access.
 
# password="raginidighe"
# for i in range(1,4):
#     p=input("Enter the password:-")
#     if p==password:
#        break
#     else:
#         print("Invalid password")

# Q22. ATM Withdrawal
#     Keep asking for withdrawal amount until the amount is less than or equal to balance
     
# balance=10000
# while True:
#     amount=float(input("Enter the amount:-"))
#     if amount<=balance:
#         balance-=amount
#         print("Withdraw succesfully")
#         print(balance)
#         break
#     else:
#         print("Insufficient Balance")

# Q23.23. Student Attendance
#     Iterate through a student list and stop checking attendance when "absent" is found


# name=["present","present","present","absent","present","absent"]
# for i in name:
#     if i=="absent":
#         print("This student is absent.")
#         break
#     else:
#         print("student is present")

# Q24.  Skip a question if the student chooses "skip" and continue to the next question

# Q=["Q1","Q2","Q3","Q4"]
# for i in Q:
#     print(Q)
#     answer=input("Type your answer:-")
#     if answer.lower()=="skip":
#         continue
#     print("Answer saved")

# Q25.25. Inventory Check
#     Loop through product quantities and stop when *stock reaches zero*


# quantity=[7,3,4,8,0,2,1]
# for i in quantity:
#     if i==0:
#   print("Stock reached zero")
#         break
#     print(i)

# Q26.26. OTP Verification
#     Users have 5 chances to enter OTP. Stop immediately when OTP matches.

# i=1
# otp=23412
# while(1<=5):
#     num=int(input("Enter the OTP:-"))
#     if otp==num:
#         print("OTP successfully match")
#         break
#     print("Invalid oTP")

# Q27. Website Visitor Counter
#     Count visitors until count reaches 100, then stop the loop

# count=0
# while(count<100):
#     count+=1
#     print(count)
 
#     if count==100:
#      print("visitor limited reached")
#      break

# Q28.28. Salary Processing
#     Skip employees whose salary is 0, process others

# salary=[100000,25000,40000,0,53000,44000]
# for i in salary:
#     if i==0:
#         continue
#     print(i)
    

# Q29. Menu-Driven Program
#     Show menu repeatedly until user selects "Exit"

# while True:
#     print("...Menu...")
#     print("1,say hello")
#     print("2.Adding two num")
#     print("3.Exit")

#     option=input("Enter the choice(1-3):-")

#     match option:
#         case '1':
#             print("Hello")
#         case '2':
#             num1=int(input("Enter the num1:-"))
#             num2=int(input("Enter the num2:-"))
#             print("Addition",num1+num2)
#         case '3':
#             print("Exit")
#             break
#         case _:
#             print("Invalid choice")


# Q  30. Game Lives System
#     The player has 3 lives. Each wrong move reduces one life. End game when lives become 0

# lives=3
# while(lives>0):
#     move=input("Enter the moves(correct/wrong):-").lower()
#     if move=="correct":
#         print("Your are alive,live left",lives)
#     else:
#         lives-=1
#         print("You miss the chance ,Live left",lives)
# print("Game over")
       

    




    
