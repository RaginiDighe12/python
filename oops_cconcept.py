
#The init method

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
       
# s1=student("Ragini",21)
# s2=student("Anurag",12)
# print(s1.name,s1.age)
# print(s2.name,s2.age)

#Default parameter in init function


# class person:
#     def __init__(self,name,age=12):
#         self.name=name
#         self.age=age
# s1=person("Ragini")

# print(s1.name,s1.age)



#self keyword

# class person:
#     def __init__(self,age,name,marks=30):
#         self.age=age
#     def printage(self):
#         print(self.age)
# p1=person(15)
# p2=person(20)
# # p1.printname()
# p1.printage()
# p2.printage()


#Addition of two number

# class math:
#     def add(Self,a,b):
#         return a+b
#     def sub(self,c,d):
#         return c-d

# m1=math()
# print(m1.add(2,4))
# print(m1.sub(5,3))

#Python inheritance


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printnameage(self):
#         print(self.name,self.age)
# class child(person):
#     pass
# x=child("amol","bhoye")
# x.printnameage()

# class Person:
#    def __init__(self, name, age):
#     self.name = name
#     self.age = age
#    def printnameage(self):
#     print(self.name, self.age)
# class Child(Person):
#   pass
# x = Child("Umesh", "Sanap")
# x.printnameage()

#Single inheritance

# class Grandfather:
#     def land(self):
#      print("Grandfather has its own land ")
# class Father(Grandfather):
#    def house(self):
#       print("Father has its own house")
# class Son(Father):
#    def bike(self):
#     print("Son has its own bike")
      
# s=Son()
# s.land()
# s.house()
# s.bike()

#Herirarchical inheritance

# class bank:
#     def interest_rate(self):
#         print("Bank interest is 6%")
# class saving_account(bank):
#     def saving(self):
#         print("Saving account")
# class Current_account(bank):
#     def current(self):
#         print("current account")
# s=saving_account()
# c=Current_account()
# s.interest_rate()
# c.interest_rate()
# s.saving()
# c.current()

# #Multiple Inheritance

# class Father:
#     def property(self):
#         print("Father own its own house")
# class Mother:
#     def care(self):
#         print("Mothers care")
# class son(Father,Mother):
#     def love(self):
#         print("Son love more to both mom and dad")
# s=son()
# s.care()
# s.love()
# s.property()


#Polymorphism:-Compile-time polymorphism

# class operation:
#     def add(self,a,b,c=3):
#         print(a+b)
# o=operation()
# o.add(2,3)
# o.add(2,6)

#Runtime polymorphism

class Animal:
    def sound(self):
        print("Animal make sound.")
class Dog(Animal):
    def sound(self):
        print("Dog barks.")
class cat(Animal):
    def sound(self):
        print("Cat meow.")
# a=Animal()
# a.sound()
# d=Dog()
# d.sound()
# c=cat()
# c.sound()
animal=[Dog(),cat()]
for a in animal:
    a.sound()

