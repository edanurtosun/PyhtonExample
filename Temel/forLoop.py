# -*- coding: utf-8 -*-

cities = ["İstanbul","İzmir","Ankara"]

#%% for intro
for city in cities:
    if city == "İzmir":
        continue
    print(city + " code = " +city[0:3])
    
#%% for range
for x in range(100):
    print(x)
    
#%% for range 2
for y in range(0,100,2):
    print(y)