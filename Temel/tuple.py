# -*- coding: utf-8 -*-

tupleList = (2,4,6,"Ankara",(2,3,4),[])
list = [2,4,6,"Ankara",[3,4,5],()]

list[0] = "6"
# tupleList[0] = 6   ---> Tuple is read only. You cannot change value of element in tuple

tupleValue = ("Edanur") # Edanur If tuple is exist one element you have , after your first element
print(type(tupleValue))

tupleValue2 = ("Edanur",)
print(type(tupleValue2))

print(tupleList[1:2]) # (4,)
print(list[1:2])      # [4]

print(tupleList[-2]) #read left to right 
print(list[-2])

print(type(tupleList))
print(type(list))

print(tupleList)
print(list)

print(len(tupleList))
print(len(list))

