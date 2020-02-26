# -*- coding: utf-8 -*-

studentsSet = {"Engin","Derin","Salih","Ahmet"} #You can't change value of elements 
studentsSet2 = set(("Edanur","Merve"))
print(studentsSet)
print(studentsSet2)


for student in studentsSet:
    print(student)
    
#print("derin" in studentsSet)   #It is false because pyhton is case sensitive

print("Derin" in studentsSet)

if "Derin" in studentsSet:
    print("It is in the list")
    
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Mert","Selin"]) #They are added to end of the set
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Selin")
print(studentsSet)
print(len(studentsSet))

#If the element not in the set don't show error message (use functions -> discard)
studentsSet.discard("Selin")
print(studentsSet)
print(len(studentsSet))

#x = studentsSet.pop() #It delete last element in the set
#print(studentsSet)
#print(len(studentsSet))

x = studentsSet.clear() #delete elements in the set, set is still exist
print(len(studentsSet))
print(studentsSet)

del studentsSet #delete set, set is not exist anymore
#print(studentsSet)



