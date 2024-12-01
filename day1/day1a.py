#!/bin/env python

file = open("day1a-input.txt")

list1 = []
list2 = []

line = file.readline()
while (line != ""):    
    vals = line.split()
    val1 = vals[0]
    val2 = vals[1]
    list1.append(int(val1))
    list2.append(int(val2))
    line = file.readline()

file.close()

list1.sort()
list2.sort()

dist_list = []

for i in range(len(list1)):
    dist_list.append(abs(list1[i] - list2[i]))

print(sum(dist_list))

