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
        lsttime= lst[5].split(':')
        new.append(lsttime[0])

#print(new)
for i in new:
    count[i]= count.get(i,0)+1
tuplist=[]
for key,value in count.items():
    newtup = (key,value)
    tuplist.append(newtup)
tuplist= sorted(tuplist)
for key,value in tuplist:
    print(key, value)
    
        