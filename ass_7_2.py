# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:35:58 2020

@author: Arnob
"""

fname = input("Enter file name: ")
fh = open(fname)
values= []
count= 0
sums = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    pos = line.find(" ")
    val = line[pos:].rstrip()
    val= float(val)
    #values.append(val)
    count = count+1
    sums= sums +val
    
"""
for i in values:
    sum = sum +i
"""
print(sums/count);
#print("Done")