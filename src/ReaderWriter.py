import pytesseract as tess
from PIL import Image

def pngToGrid(path):
    tess.pytesseract.tesseract_cmd = r'C:\Users\IRFAAN DZAKIY\AppData\Local\Tesseract-OCR\tesseract.exe'

    img = Image.open(path)
    width, height = img.size
    arr = [[0 for i in range(9)] for i in range(9)]

    img = img.crop((1, 1, width - 1, height - 1))

    for i in range(9):
        for j in range(9):
            left = 32 * j + 4
            top = 32 * i + 2.5
            right = left + 32 - 9
            bottom = top + 32 - 7

            img1 = img.crop((left, top, right, bottom))
            text = tess.image_to_string(img1, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            
            if (text == ''):
                arr[i][j] = 0
            else:
                arr[i][j] = int(text)  

    return arr 

def textToGrid(path):
    arr = []
    with open(path, 'r') as f:
        for row in f:
            arr.append(row.split())
    for i in range(9):
        for j in range(9):
            if (arr[i][j] == '#'):
                arr[i][j] = 0
            else:
                arr[i][j] = int(arr[i][j])
    return arr

def gridToText(filename, content):
    fileLoc = "../test/solution_" + filename + '.txt'
    f = open(fileLoc, 'w')
    f.write(content)
    f.close()