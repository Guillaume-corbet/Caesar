#!/usr/bin/python3
import os
import sys

hexaToBinTable = {
    '0': b"0000",'1': b"0001",'2': b"0010",'3': b"0011",'4': b"0100",'5': b"0101",'6': b"0110",'7': b"0111",'8': b"1000",'9': b"1001",'A': b"1010",'B': b"1011",'C': b"1100",'D': b"1101",'E': b"1110",'F': b"1111"
}

binToHexa = {
    "0000": b'0', "0001": b'1', "0010": b'2', "0011": b'3', "0100": b'4', "0101": b'5', "0110": b'6', "0111": b'7', "1000": b'8', "1001": b'9', "1010": b'A', "1011": b'B', "1100": b'C', "1101": b'D', "1110": b'E', "1111": b'F'
}

def readFile(path):
    if not os.path.isfile(path):
        print("File does not exist.", file=sys.stderr)
        return None
    with open(path, 'r') as file:
        cnt = file.read()
        if not cnt:
            print("File is empty.", file=sys.stderr)
            return None
        return cnt

def isHexa(string):
    for letter in string:
        if letter not in "0123456789ABCDEF":
            return False
    return True

# Converts an hex strings into binary
def hexToBin(string):
    global hexaToBinTable
    hexaBytes = string.encode('utf-8')
    rawBin = bytes()

    for byte in hexaBytes:
        rawBin += hexaToBinTable[chr(byte)]
    return rawBin

# Converts a binary strings into hex
def binaryToHex(string):
    global binToHexa
    rawHex = bytes()

    splitBin = [string[i:i+4] for i in range(0, len(string), 4)]
    for byte in splitBin:
        tmp = ""
        for i in byte:
            tmp += chr(i + 48)
        rawHex += binToHexa[tmp]
    return rawHex

def byte_xor(string1, string2):
    return bytes([a ^ b for a, b in zip(string1, string2)])

def fixed_xor(string1, string2):
    global hexaToBinTable
    string1 = hexToBin(string1)
    string2 = hexToBin(string2)
    res = bytes()

    res = byte_xor(string1, string2)
    res = binaryToHex(res)
    return (res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wong arguments.", file=sys.stderr)
        exit(84)
    cnt = readFile(sys.argv[1])
    if not cnt:
        exit(84)
    cnt = cnt.upper()
    tab = cnt.split('\n')
    if len(tab) != 2 and (len(tab) != 3 or len(tab[2]) != 0):
        print("More or less than two strings in input.", file=sys.stderr)
        exit(84)
    if not isHexa(tab[0]) or len(tab[0]) % 2 != 0 or len(tab[0]) == 0:
        print("First string is not in hexadecimal format.", file=sys.stderr)
        exit(84)
    if not isHexa(tab[1]) or len(tab[1]) % 2 != 0 or len(tab[1]) == 0:
        print("Second string is not in hexadecimal format.", file=sys.stderr)
        exit(84)
    if len(tab[0]) != len(tab[1]):
        print("string haven't the same lenght.", file=sys.stderr)
        exit(84)
    res = fixed_xor(tab[0], tab[1])
    print(res.decode("utf-8"))
    exit(0)