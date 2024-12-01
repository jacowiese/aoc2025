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

sim_score_list = []

for val1 in list1:
    val2 = list2.count(val1)
    sim_score_list.append(val1 * val2)

print(sum(sim_score_list))


