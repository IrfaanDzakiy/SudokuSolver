from ReaderWriter import *
from Util import *
from SudokuSolver import *

printHeader()
playing = True
while (playing):
    content = ''
    print(\
        "Mau ngesolve sudoku dari format apa ni :\n"\
        "1. Text\n"\
        "2. PNG"
        )
    format = input("Masukan nomor dari format yang diinginkan (1/2) : ")
    while (format != '1' and format != '2'):
        format = input("Masukan nomor dari format yang diinginkan (1/2) : ")

    fileList = printTestList(format)

    fileName = input("Masukan nama file sudoku yang ingin dipecahkan : ")
    while(fileName not in fileList):
        fileName = input("Masukan nama file sudoku yang ingin dipecahkan : ")
    
    content += fileName + '\n'

    if (format == '1'):
        arr = textToGrid('../test/' + fileName)
    else:
        arr = pngToGrid('../test/' + fileName)

    content += "Before : \n\n"
    content += showArr(arr) + '\n'

    content += "After : \n\n"
    if (not solve(arr)):
        content += "Unsolvable\n"
    
    content += showArr(arr) + '\n'
    
    content += "Koordinat area bernomor 5 : \n"
    content += printFiveCoordinates(arr)

    print(content)

    print("Solusi akan disimpan kedalam file solution_" + fileName.split('.')[0] + ".txt")
    gridToText(fileName.split('.')[0], content)

    cont = input("Coba lagi ? (Y/N) : ")
    if (cont == "N"):
        print("Terima kasih sudah mencoba BAMBANG SUDOKU SOLVER !!!!!")
        playing = False
    
    