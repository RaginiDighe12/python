#for loop

#Q1.Print numbers from 1 to 10 using for loop

# for i in range(1,11):
#     print(i)


# #Q.Alterative method to above example.

# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     print(i)


#Q2.Print all even numbers from 1 to 20.

# for i in range(2,21,2):
#     print("Even num:-",i)

# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#     if i % 2 == 0:
#         print(i)
       

#Q3.odd number

# for i in range(1,20,2):
#     print("Odd number.")

# num=[1,2,3,4,5,6,7,8,9,10]
# for i in num:
#  if i%3==0:
#     print(i)

#Q4.Print squares of numbers from 1 to 10

# for i in range(1,10):
#     square=i*i
#     print(square)

#Q5.Print each character of a string "Python" using for loop.

# name=["python","c","cpp","js"]       

# for i in name:
#     print("languages:-",name)

#languages:- ['python', 'c', 'cpp', 'js']
# languages:- ['python', 'c', 'cpp', 'js']
# languages:- ['python', 'c', 'cpp', 'js']
# languages:- ['python', 'c', 'cpp', 'js']


# Addition of even number.

# sum=0

# for i in range(1,10):
#     if i%2==0:
#        print(i,end=" ")
#        sum=sum+i
# print("the sum is:-",sum)

# Addition of odd number

# sum=1

# for i in range(1,16):
#     if i%3==0:
#         print(i,end=" ")
#         sum=sum+i
# print("Sum is:-",sum)


#Addition of even number.

# sum=0

# for i in range(1,10):
#     if i%2==0:
#        print(i,end=" ")
#        sum=sum+i
# print("the sum is:-",sum)

# Addition of odd number

# sum=1

# for i in range(1,16):
#     if i%3==0:
#         print(i,end=" ")
#         sum=sum+i
# print("Sum is:-",sum)

#Take a number from user and print its multiplication table

    # num=int(input("Enter the number:-"))    #take number from user

    # for i in range(1,11):    # i sequence cha number from 1 tp 10
    #     mul=num*i    #multiply input number and sequence number
    #        #increment 
    #     print(mul,end=" ")

#Q6.Find the sum of numbers from 1 to n (n user input)

# n=int(input("Enter the number:-"))

# sum=0
# for i in range(1,n):
#     sum+=i
# print("Sum is:-",sum)

#Q7.Count total digits in a number using for loop.

# num=(input("Enter the number:-"))

# count=0

# for i in num:
#     count+=1
# print(i)










      #Q1.Print numbers from 1 to 10 using for loop

# for i in range(1,11):
#     print(i)


#Q2.Print all even numbers from 1 to 20.

# for i in range(2,21,2):
#     print(i)

#Q3.Print all odd numbers from 1 to 15.

# for i in range(1,16,2):
#     print(i)

#Q4.Count how many numbers are divisible by 3 between 1 and 50.

# count=0

# for i in range(1,50):
#     if i%3==0:
#         count+=1
# print(count)


#Q5.Find the sum of numbers from 1 to 10

# sum=0

# for i in range(1,11):
#     sum+=i
# print(sum)

#Q6.Print each character of a string on a new line

# name="python"

# for i in name:
#     print(i)


#Q7.Count how many vowels are present in a given string.

# name="python"
# count=0
# for i in name:
#     if i in "aeiou":
#         count+=1
# print(count)
    

#Q8.Print only uppercase letters from a string.

# name="MaHaraShtra"

# for i in name:
#     if i.isupper():
#       print(i)

#Q9.Reverse a string using a for loop

# for i in range(10,0,-1):
#     print(i)
    

#Q10.Find the largest number in a list

# number=[10,30,50,40,70,90]
# largest=number[0]

# for num in number:
#     if num > largest:
#         largest=num
# print(largest)

#Q10.Find the smallest number in a list

# number=[10,30,50,40,70,2,90]
# smallest=number[0]

# for num in number:
#     if num<smallest:
#         smallest=num
# print(smallest)


#Q11.Count how many even and odd numbers are in a list.

# even_count=0
# odd_count=0
# number=[1,2,3,4,5,6,7,8,9,10]
# for num in number:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
# print("Even number:-",even_count)
# print("Odd number:-",odd_count)


#Q12.Print prime numbers between 1 and 50.

# for num in range(2, 51):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, end=" ")


#Q13.Print a multiplication table of a given number

# num=int(input("Enter the number:-"))
# for i in range(1,11):    
#          mul=num*i    
#          print(mul,end=" ")


#Q14.Print duplicate elements from a list

# num=[1,2,3,2,4,5,6,5,6,5,5]
# dup=[]
# for i in range(len(num)):
#    for j in range(i+1,len(num)):
#         if num[i]==num[j] and num[i] not in dup:
#             dup.append(num[i])
# print("Duplicate numbers:-",dup)

#Q15.Count how many times a given number appears in a list.

# count=0

# num=[1,2,3,4,5,4,6,4]
# number=int(input("Enter the number:-"))
# for i in num:
#     if i==number:
#         count+=1
# print(count)
   
#Q16.Check whether a number is prime using a for loop

# num=int(input("Enter the number:-"))
# count=0

# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime number.")
# else:
#     print("not prime number.")
   
#Q17.Print numbers greater than the average of a list.

# number=[10,20,30,40]
# avg=sum(number)/len(number)
# print(avg)

# for i in number:
#     if i>avg:
#         print(i)

#Q18.Print prime numbers between 1 and 50


# for num in range(2,51):
#     for  i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)

#Q19.Find the factorial of a number using a for loop

# fact=1
# num=int(input("Enter the number:-"))

# for i in range(1,num+1):
#     fact=fact*i

# print(fact)

#Q20.Check whether a string is a palindrome

# name=input("Enter the name:-")
# reverse=""

# for ch in name:
#     reverse=ch+reverse

#     if ch==reverse:
#         print("palindrome")
#     else:
#         print("not")


#Q21.Count words in a sentence using a for loop

# count=0
# sentence="I like to learn python"
# words=sentence.split()
# for word in words:
#         count+=1
#         print(word,end=" ")
# print(count)

#Q22.Find the first repeated character in a string.

name=input("Enter the string:-")
rep=[]
for i in name:
    if i in rep:
        print(i)
    else:
        rep.append(i)
    


        
       




    



   




        
                            




       





      
       



    