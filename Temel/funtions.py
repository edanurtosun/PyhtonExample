# -*- coding: utf-8 -*-

name = input("What's your name ? ")

def sayHello(name):
    print("Hello " + name.upper())
    
sayHello(name)

def sayHello2(name2 = "visiter", surname = " person"):
    print("Hello " + name2+ " " + surname)
sayHello2("edanur","tosun")
    
#%%
def calculateArea(a,b):
    return (a*b)/2

result = calculateArea(3,8)
print(result)

#%%

calculate = lambda a,b: a*b/2
print(calculate(3,6))
print(type(calculate))

x = calculate
print(x(4,5))