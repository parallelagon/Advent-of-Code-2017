# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 22:30:44 2017

@author: Zach
"""

"""This program should make a list of objects that keep track of where
they are located on a spiral (either right, top, left, bottom, and the corners)
a function 'corners(n)' returns the corner indices and from those an object can find
a side that it is on.  With a corner location and a side, the offsets can be found
to give the indices of all nearby objects.  All counting starts
from one as an unfortunate legacy of the previous exercies"""

def whichShell(n):
    i = 0
    x = 0
    delta = 0
    
    if n == 0:
        return 0,1
    
    while x <= n:
        #the numbers in the i'th shell
        delta = 2*(2*i + 1)+2*(2*i - 1)
        if x <= n <= (x+delta):
            break
        else:
            x += delta
            i += 1
            
    
    return i, x+1

def corners(n): #returns the corners of shell n
    shell, start = whichShell(n)
    corner1 = start + 2*shell -1
    corner2 = corner1 + 2*shell
    corner3 = corner2 + 2*shell
    corner4 = corner3 + 2*shell
    
    return corner1,corner2,corner3,corner4

def offset(n):# takes the index and returns a list of indices of 
    #neighboring cells
    side = ''
    shell, start = whichShell(n)
    c1,c2,c3,c4 = corners(n)
    
    start0 = 1
    for num in range(0,shell-1):
        start0+=num*8
    start1 = 1
    for num in range(0,shell+1):
        start1+=num*8
    """i = n - 8*shell
    shell0,start0 = whichShell(i)
    
    j = n+ 8*shell
    shell1,start1 = whichShell(j)"""
    
    if n == 0:
        return 'start',0
    
    if n == start:
        side = 'start'
        offIndex = 1
    elif n == c1:
        side = 'corner 1'
        offIndex = start - start0 +2
    elif n == c2:
        side = 'corner 2'
        offIndex = start +1 - start0 +1 +1 + 1
    elif n == c3:
        side = 'corner 3'
        offIndex = start +1 - start0 + 5
    elif n == start + 1:
        side = 'start+1'
        offIndex = start+1 - start0
    elif start + 1 < n < c1-1:
        side = 'right'
        offIndex = start+1 - start0
    elif n == c1 -1:
        side = 'c1-1'
        offIndex = start +1 - start0    
    elif n == c1+1:
        side = 'c1+1'
        offIndex = start -start0 + 3
    elif c1+1 < n < c2-1:
        side = 'top'
        offIndex = start - start0 +3
    elif n == c2-1:
        side = 'c2-1'
        offIndex = start - start0 + 3
    elif n == c2+1:
        side = 'c2+1'
        offIndex = start +1 - start0 +1 +1 + 1
    elif c2+1 < n <c3-1:
        side = 'left'
        offIndex = start +1 - start0 + 4
    elif n == c3-1:
        side = 'c3-1'
        offIndex = start +1 - start0 + 4
    elif n == c3+1:
        side = 'c3+1'
        offIndex = start +1 - start0 + 5
    elif c3+1 < n < (start1 -1):
        side = 'bottom'
        offIndex = start +1 - start0 + 6
    else:
        side = 'start-1'
        offIndex = start+1 - start0 + 6
        
        
    return side,offIndex

#building the list
class number:
    def __init__(self,n):
        self.offIndices = ['a']*8
        self.index = n
        self.side,self.offset = offset(n)
        self.value = 0
        if self.side == 'start' or self.side == 'corner 1' or self.side == 'corner 2' or self.side == 'corner 3':
            self.offIndices[0] = n - 1
            self.offIndices[1] = n - 1 - offset(n-1)[1]
        elif self.side == 'start+1' or self.side == 'c1+1' or self.side == 'c2+1' or self.side == 'c3+1':
            self.offIndices[0] = n -1
            self.offIndices[1] = n - 2
            self.offIndices[2] = n - 2 - offset(n-2)[1]
            self.offIndices[3] = n - 2 - offset(n-2)[1] + 1
        elif self.side == 'right' or self.side == 'left' or self.side =='top' or self.side == 'bottom':
            self.offIndices[0] = n-1
            self.offIndices[1] = n - self.offset
            self.offIndices[2] = self.offIndices[1] + 1
            self.offIndices[3] = self.offIndices[1] - 1
        elif self.side == 'c1-1' or self.side == 'c2-1' or self.side == 'c3-1' or self.side == 'start-1':
            self.offIndices[0] = n-1
            self.offIndices[1] = n - self.offset
            self.offIndices[2] = self.offIndices[1] - 1
            
        self.offIndices = list(filter((lambda x: x!= 'a'),self.offIndices))
        #self.offIndices = list(map((lambda x: x-1),self.offIndices)) #to correct the off by one error mentioned above
        
# to build the list, every entry will be an object with a value
#the value will be calculated by looking for objects in the array to add
#because of the ordering, the list gets initialized
spiral0 = [1,1,2,4,5,10,11,23,25,26]
spiral = []
for i in range(0,9):
    spiral.append(number(i))
    spiral[i].value = spiral0[i]


x = 0
while x <= 368078:
    i = len(spiral)
    spiral.append(number(i))
    a = spiral[i].offIndices
    spiral[i].value = sum([spiral[e].value for e in a])
    x = spiral[i].value
    
print x,i
    
    
    