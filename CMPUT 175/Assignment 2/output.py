# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 00:48:37 2020

@author: marza
"""

def isSame(alist):
      first = alist[0]
      index = 1
      same = True
      while index < len(alist) and same == True:
         #if alist[index] != first:
         #  same = False
         same = alist[index] == (first)
         index = index + 1
         
      return same
  
print(isSame(['x','x','x','o']))