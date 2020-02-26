# -*- coding: utf-8 -*-

dictionary = {
        "book" : "kitap",
        "table" : "masa",
        
        }

dictionary2 = dict(kitap="book", masa="table")

dictionary["book"] = "kitap 1"
dictionary["pencil"] = "kalem"  #added new key and value

del(dictionary["book"])

print(dictionary)
print(len(dictionary))
print(dictionary2)