# -*- coding: utf-8 -*-

number = int(input("Enter a star number = "))

counter = 1

star = ""

while counter <= number:
    for x in range(1,number+1):
        star = star + "*"
        print(star)
        counter = counter + 1