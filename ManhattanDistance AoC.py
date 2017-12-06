# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 22:26:44 2017

@author: Zach
"""

def whichShell(n):
    i = 1
    x = 1
    delta = 0
    
    if n == 1:
        return 0
    
    while x <= n:
        #the numbers in the i'th shell
        delta = 2*(2*i + 1)+2*(2*i - 1)
        if x <= n <= (x+delta):
            break
        else:
            x += delta
            i += 1
            
    
    return i, x+1
    

def howHigh(n):
    shell, start = whichShell(n)
    corner1 = start + 2*shell -1
    corner2 = corner1 + 2*shell
    corner3 = corner2 + 2*shell
    corner4 = corner3 + 2*shell
    #print corner1, corner2, corner3, corner4
    
    #find the axis 
    axis1, axis2, axis3, axis4 = start + shell-1, (corner1 + corner2)/2,(corner2+corner3)/2,(corner3+corner4)/2

    #print axis1,axis2,axis3,axis4
    if start <= n <= corner1:
        return abs(n-axis1)
    elif corner1 <= n <= corner2:
        return abs(n-axis2)
    elif corner2<=n <= corner3:
        return abs(n-axis3)
    else:
        return abs(n-axis4)
    

def manhattanDistance(n):
    return howHigh(n) + whichShell(n)[0]

#entering a shell, n, this gives the offset of each of the sides with the n-1st shell
def offset(n):
    shell,start = whichShell(n)
    i = n - (2*(2*shell + 1)+2*(2*shell - 1))
    shell0,start0 = whichShell(i)
    print start,shell,'$',start0,shell0
    
    rightHandOffset = start+1 - start0
    corner1Offset = rightHandOffset +1
    
    TopOffset = corner1Offset + 1
    corner2Offset = TopOffset + 1
    
    leftHandOffset = corner2Offset +1
    corner3Offset = leftHandOffset +1
    
    bottomOffset = corner3Offset + 1
    
    
    
    corner1 = start + 2*shell -1
    corner2 = corner1 + 2*shell
    corner3 = corner2 + 2*shell
    corner4 = corner3 + 2*shell
    return corner1,corner2,corner3,corner4,rightHandOffset,corner1Offset,TopOffset,corner2Offset,leftHandOffset,corner3Offset,bottomOffset
    
#to build the array, for every index find the indexes of the 
    #cells to add, making sure only to go back
    #for the first cell, 1 initializes the process
    #nine cases, two for each corner and sides



        
