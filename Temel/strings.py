# -*- coding: utf-8 -*-

#substring
message = "Hello World"
print(message[2:5])

newMessage = message[:2]
print(newMessage)

#What is the last letter in the word? Lets find!
print(len(message))
newMessage2 = message[len(message)-1:len(message)]
print(newMessage2)

#lower upper
print(message.lower())  #hello world
print( message.upper()) #HELLO WORLD

#replace
print(message.replace("o","ö"))
print(message)

#split & strip
info ="  Edanur TOSUN 23 Kocaeli   ".strip()
print(info.split())
print(info.split(" "))

info2 ="  Edanur;TOSUN;23;Kocaeli   ".strip()
print(info.split())
print("Adı : " + info2.split(";")[0])

#input
name = input("What is your name?")
number1 = input("Number 1 = ?")
number2 = input("Number 2 = ?")
print(int(number1)+int(number2))









