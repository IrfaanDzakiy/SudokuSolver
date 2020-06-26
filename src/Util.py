import os, fnmatch
from SudokuSolver import *

def showArr(arr):
    res = "= = = = = = = = = = = = = = = = = = =\n"   
    for i in range(9):
        res += '| '
        for j in range(8):
            res += str(arr[i][j]) + ' - '
        res += str(arr[i][8]) + ' |'
        res += '\n'
    res += "= = = = = = = = = = = = = = = = = = =\n"    
    return res

def checkArr(arr):
    for i in range(9):
        for j in range(9):
            if (not checkCellSafety(arr, i, j, arr[i][j])):
                print (i, j)
                return False
    return True

def printTestList(inp):
    res = []
    listOfFiles = os.listdir('../test/.')
    print("")
    if (inp == '1'):
        pattern = "*.txt"
    elif (inp == '2'):
        pattern = "*.png"

    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            res.append(entry)
            print (entry)

    print("")
    return res
    
def printHeader():
    print("SELAMAT DATANG DI BAMBANG SUDOKU SOLVER\n")

def printFiveCoordinates(arr):
    res = ''
    for i in range(9):
        for j in range(9):
            if (arr[i][j] == 5):
                res += "(" + str(i+1) + ", " + str(j+1) + ")\n"
    return res

