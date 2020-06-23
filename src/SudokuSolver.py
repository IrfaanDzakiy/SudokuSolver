def findEmptyCell(arr):
    cell = [-1,-1]
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                cell[0] = i
                cell[1] = j
                return cell
    return cell

def isAnyEmptyCell(arr):
    cell = findEmptyCell(arr)
    if (cell == [-1,-1]):
        return False
    return True

def checkRow(arr, row, num):
    for j in range(9):
        if (arr[row][j] == num):
            return True
    return False

def checkCol(arr, col, num):
    for i in range(9):
        if (arr[i][col] == num):
            return True
    return False

def checkBox(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if ( arr[row+i][col+j] == num):
                return True
    return False

def checkCellSafety(arr, row, col, num):
    isRow = checkRow(arr, row, num)
    isCol = checkCol(arr, col, num)
    isBox = checkBox(arr, row - row % 3, col - col % 3, num)

    return not isRow and not isCol and not isBox

def solve(arr):
    if (not isAnyEmptyCell(arr)):
        return True

    empRow = findEmptyCell(arr)[0]
    empCol = findEmptyCell(arr)[1]

    for num in range(1, 10):
        if (checkCellSafety(arr, empRow, empCol, num)):
            arr[empRow][empCol] = num

            if (solve(arr)):
                return True

            arr[empRow][empCol] = 0
    
    return False


