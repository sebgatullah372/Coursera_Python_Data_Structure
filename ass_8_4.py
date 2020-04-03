# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 02:09:18 2020

@author: Arnob
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
newlist= list()
for line in fh:
    line= line.rstrip()
    a= line.split()
    for i in a:
       if i not in lst:
           lst.append(i)

lst.sort()
print(lst)
   