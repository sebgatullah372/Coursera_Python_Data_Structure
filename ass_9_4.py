# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 05:05:22 2020

@author: Arnob
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
new= []
for line in handle:
    if line.startswith("From"):
        if line.startswith("From:"): continue
        lst =line.split()
        
        new.append(lst[1])

#print(new)
for i in new:
    count[i]= count.get(i,0)+1

maxcnt= 0
maxemail= 0
for email, cnt in count.items():
    if maxcnt == 0 or cnt> maxcnt:
        maxcnt= cnt
        maxemail= email

print(maxemail, maxcnt);
        