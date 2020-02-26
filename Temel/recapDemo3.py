# -*- coding: utf-8 -*-

number = int(input("Enter number = "))

isPrime = True

for i in range(2,number):
    if number % i == 0:
        isPrime = False
        break
    
if isPrime == True:
    print(str(number) + " is a prime number.")
else:
    print(str(number) + " isn't a prime number.")
    
    
    