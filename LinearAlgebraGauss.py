# Sumaiya Hashmi
# LinAlg/ Gaussian elimination (without numpy)
# to start: gauss()

from math import *
import random
import sys

def menu():
    """ a function that simply prints the menu """
    print
    print "(1) Enter the size and values of an array"
    print "(2) Print the array"
    print "(3) Multiply an array row by a constant"
    print "(4) Add one row into another"
    print "(5) Add a multiple of one row to another"
    print "(6) Solve"
    print "(9) Quit"

    print "Which choice would you like?"


def gauss():
    """ the main user-interaction loop """
    A = [ [2.0,4.0,5.0,34.0], [2.0,7.0,4.0,36.0], [3.0,5.0,4.0,35.0] ] # an initial array
    print "Welcome!"
    
    while True:     # the user-interaction loop
        print 'The array is now'
        print printArray(A) 
        menu()
        uc = input( "Choose an option: " )
        
        if uc == 9: # we want to quit
            print "Later gator!"
            break

        elif uc == 1:  # input array
            A = enterValues()
            print A
           
        elif uc == 2:  # print array
            print 

        elif uc == 3: # mult array by a constant
            r= input("Which row?")
            m=input("What multiple?")
            print multRow(A,r,m)

        elif uc == 4:  # add one row into another
            rs= input("Which is the source (unchanged) row?")
            rd=input("Which is the destination (changed) row?")
            print addRowSIntoRowD(A,rs,rd)
            
        elif uc == 5:  # add mult of one row into another
            rs= input("Which is the source (unchanged) row?")
            m = input("What multiple of that row?")
            rd=input("Which is the destination (changed) row?")
            print addMofRowSIntoRowD(A,m,rs,rd)

        elif uc == 6: #solve
            print solve(A)
            
        else:
            print "That's not on the menu."

    print
    print "See you later!"

def enterValues():
    """takes input and stores as A and returns A"""
    c = input("Please type/paste a 2d list of lists:")
    A = c
    return A

def printArray(A):
    """ prints array A"""
    h = len(A)
    w = len(A[0])
    for row in range(h):
        '\n'
        for col in range(w):
            print "%8.3f " % (A[row][col]) ,
        print
    return ' '

def multRow(A,r,m):
    """multiply all elements of row r of array A by value m"""
    for col in range(len(A[r])):
        A[r][col] = (A[r][col])*m

def addRowSIntoRowD(A,rs,rd):
    """adds each element of row rs of array A into row rd of array A"""
    for col in range(len(A[rd])):
        A[rd][col] += A[rs][col]

def addMofRowSIntoRowD(A,m,rs,rd):
    """adds each element of row rs multiplied by m into row rd of array A"""
    for col in range(len(A[rd])):
        A[rd][col] += (A[rs][col])*m

def solve(A):
    """returns array of 0's with a diagonal of 1's, solving array A"""
    r = len(A)
    c = len(A[0])
    if r+1 != c:
        print 'Error! Wrong number of rows and columns'
        return
    else:
        for col in range(len(A)):
            l = col

            for row in range(len(A)):
                if row == col:
                    multRow(A,row,(1.0/(A[row][col])))
                else:
                    c = -1.0*(A[row][col]) / (A[l][col])
                    addMofRowSIntoRowD(A,c,l,row)

