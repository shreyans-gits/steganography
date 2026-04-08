import cv2
from randimage import get_random_image, show_array
import numpy as np

def error42069():
    print("Invalid command. Rerun the program.")

def enc(code):
    return '{0:08b}'.format(ord(code))

def encfromfile(fn:str):
    f = open(fn, "r")
    k = f.read()
    f.close()
    return k 


def encode():
    cmd = input("File/Direct: ")
    if cmd == "F":
        msg = encfromfile(input("Filename: "))
    elif cmd == "D":
        msg = input("Message: ")
    else:
        error42069()
        quit()

    l = len(msg)
    binary = []
    for charac in msg:
        binary.append(enc(charac))

    img = (get_random_image((284, 540)) * 255).astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    n = 0
    r = 0
    for k in range(0, l):
        j = 0
        for i in binary[k][0:3]:
            if int(i) == 0:
                if img[r][n][j] % 2 == 1:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            if int(i) == 1:
                if img[r][n][j] % 2 == 0:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            j+=1

        n += 1

        j = 0
        for i in binary[k][3:6]:
            if int(i) == 0:
                if img[r][n][j] % 2 == 1:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            if int(i) == 1:
                if img[r][n][j] % 2 == 0:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            j+=1

        n+=1

        j = 0
        for i in binary[k][6:8]:
            if int(i) == 0:
                if img[r][n][j] % 2 == 1:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            if int(i) == 1:
                if img[r][n][j] % 2 == 0:
                    img[r][n][j] = (img[r][n][j] & 0xFE) | int(i)
            j+=1
        
        
        if k < l-1:
            if img[r][n][2] % 2 == 1:
                img[r][n][2] += 1
        elif k == l-1:
            if img[r][n][2] % 2 == 0:
                img[r][n][2] += 1

        n+=1

        if n == 540:
            n = 0
            r += 1

    cv2.imwrite("output.png", img)

def decode(filename:str):
    img = cv2.imread(filename)
    main = []
    k = 0
    r = 0
    while True:
        temp = ""
        for i in img[r][k]:
            if i % 2 == 0:
                temp += "0"
            else:
                temp += '1'
        k+=1
        for i in img[r][k]:
            if i % 2 == 0:
                temp += "0"
            else:
                temp += '1'
        k += 1
        for i in img[r][k][0:2]:
            if i % 2 == 0:
                temp += "0"
            else:
                temp += '1'
        main.append(temp)
        if img[r][k][2] % 2 == 1:
            break
        k+=1
        if k == 540:
            k = 0
            r += 1

    output = ""
    for c in main:
        output += chr(int(c, 2))

    return output
