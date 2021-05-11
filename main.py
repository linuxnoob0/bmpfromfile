'''
Dont mind the weird names first program uploaded to github

Free to use just include creater me

Was a fun project inspired by that thing in linux where you can play any file as a sound

'''



import binascii
import random
import os

bitmapHEADER = "424dfac800000000000076000000280000004801000039010000010004000000000084c80000741200007412000000000000000000000000000000008000008000000080800080000000800080008080000080808000c0c0c0000000ff0000ff000000ffff00ff000000ff00ff00ffff0000ffffff00"

def makeFile(filein):


    with open(f'.//{filein}', 'rb') as lyw:
        content3 = lyw.read()
    content3 = str(binascii.hexlify(content3)).strip("\n").format()


    full = bitmapHEADER + content3[2:]
    full = binascii.unhexlify(full[0:len(full)-1])

    outF = open(f"{filein}.bmp", "wb")
    outF.write(full)
    outF.close()


def genhex():
    stringed = str(hex(random.randint(0, 255)))
    stringed = stringed[2:]
    return stringed[0]

arr = os.listdir()
print(arr)
abc = len(arr)-1

while (abc != 0):
    makeFile(arr[abc])
    abc -= 1



