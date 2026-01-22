#Q1.Create a set with 5 integer values and print it.

numSet = {1,2,3,4,5}
print(numSet)

#Q2.Create a set using the set() constructor from a list

numlist=[1,2,3,4,5]
numSet=set(numlist)
print(numSet)

#Q3.Create a set with duplicate values and print the result

nameSet={"Ragini",1,False,"Disha",0,"Ragini"}
print(nameSet)

#Q4.Create a set containing True and 1. Print the set.

numSet={True,"Ragini","Mona",0,1,"False"}
print(numSet)

#Q5.Write a program to find the length of a set using len()

nameSet={"Ragini",1,False,"Disha",0,"Ragini"}
print(len(nameSet))

#Q6.Create a set with mixed data types and print it.

mixedSet={"Ragini",1,4+2j,False,3.5}
print(mixedSet)

#Q7.Write a program to access set elements using a for loop

numSet={1,2,3,4,5}
for i in numSet:
    print(numSet)

#Q8.Create an empty set and add three elements using add().

nameSet=set()
nameSet.add("Ragini")
nameSet.add("Anushka")
nameSet.add("Jayashri")
print(nameSet)

#Q9.Write a program to remove an element from a set using discard().

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
nameSet.discard("Dipti")
print(nameSet)

#Q10.Write a program to remove an element from a set using remove().

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
nameSet.remove("Rinal")
print(nameSet)

#Q11.Write a program that removes a non-existing element using discard()


nameSet={"Ragini","Dipti","Rinal","Bhakti"}
nameSet.discard("Anushka")
print(nameSet)

#Q12.Write a program that removes a non-existing element using remove() and observe the error


# nameSet={"Ragini","Dipti","Rinal","Bhakti"}
# nameSet.remove("Anushka")
# print(nameSet)

# KeyError: 'Anushka'

#Q13.Write a program to remove a random element from a set using pop().

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
nameSet.pop()
print(nameSet)

#Q14.Write a program to clear all elements from a set using clear().

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
nameSet.clear()
print(nameSet)

#Q15.Write a program to delete a set completely using del.

# nameSet={"Ragini","Dipti","Rinal","Bhakti"}
# del nameSet
# print(nameSet)

#Q16.Write a program to combine two sets using union()

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
numSet={1,2,3,4}
merginSet=nameSet.union(numSet)
print(merginSet)

#Q17.Write a program to combine two sets using the | operator

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
numSet={1,2,3,4}
merginSet = nameSet | numSet
print(merginSet)

#Q18.Write a program to update one set using another set with update()

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
numSet={1,2,3,4}
nameSet.update(numSet)
print(nameSet)

#Q19.Write a program to join a set with a list using union()

nameSet={"Ragini","Dipti","Rinal","Bhakti"}
numSet=[1,2,3,4]
merginSet = nameSet.union(numSet)
print(merginSet)

#Q20.Write a program to join three sets using union()


nameSet={"Ragini","Dipti","Rinal","Bhakti"}
numSet={1,2,3,4}
mixedSet={"Anushka",4+3j,1,True,4.5}
merginSet=nameSet.union(numSet,mixedSet)
print(merginSet)

#Q21.Write a program to find common elements between two sets using intersection()

nameSet={"Ragini","Dipti","Rinal","Bhakti",1,True}
numSet={1,2,"Rinal",True}
merginSet=nameSet.intersection(numSet)
print(merginSet)

#Q22.Write a program to find common elements between two sets using the & operator.

nameSet={"Ragini","Dipti","Rinal","Bhakti",1,True}
numSet={1,2,3,4}
merginSet=nameSet & numSet
print(merginSet)

#Q23.Write a program to find intersection between a set and a list using intersection().

nameSet={"Ragini","Dipti","Rinal","Bhakti",1,True}
numSet=[1,2,3,"Ragini"]
merginSet=nameSet.intersection(numSet)
print(merginSet)

#Q24.Write a program to update a set using intersection_update().

nameSet={"Ragini","Dipti","Rinal","Bhakti",1,True}
numSet={1,2,3,"Ragini"}
nameSet.intersection_update(numSet)
print(nameSet)

#Q25.Write a program to find elements present in first set but not in second using difference().

name1Set={"Ragini","Dipti","Rinal","Bhakti",1,True}
name2Set={"Ragini","Dipti","Rinal"}
merginSet=name1Set.difference(name2Set)
print(merginSet)

#Q26.Write a program to find difference between two sets using the - operator.

name1Set={"Ragini","Dipti","Rinal","Bhakti",1,True}
name2Set={"Ragini","Dipti","Rinal"}
merginSet=name1Set - name2Set
print(merginSet)

#Q27.Write a program to update a set using difference_update()

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={"Ragini","Dipti","Rinal"}
name1Set.difference_update(name2Set)
print(name1Set)

#Q28.Write a program to find symmetric difference using symmetric_difference()

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={"Ragini","Dipti","Rinal",1,2,3}
merginSet=name1Set.symmetric_difference(name2Set)
print(merginSet)

#Q29.Write a program to find symmetric difference using the ^ operator

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={"Ragini","Dipti","Rinal",1,2,3}
merginSet=name1Set^name2Set
print(merginSet)

#Q30.Write a program to perform union, intersection, difference, and symmetric difference on two sets and print all results.

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={1,2,3}
merginSet=name1Set.union(name2Set)
print(merginSet)

name1Set={"Ragini","Dipti","Rinal","Bhakti",1}
name2Set={1,2,3,"Rinal"}
merginSet=name1Set.intersection(name2Set)
print(merginSet)

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={1,2,3,"Rinal"}
merginSet=name1Set.difference(name2Set)
print(merginSet)

name1Set={"Ragini","Dipti","Rinal","Bhakti"}
name2Set={1,2,3,"Rinal"}
merginSet=name1Set.symmetric_difference(name2Set)
print(merginSet)