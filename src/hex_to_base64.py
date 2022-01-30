#!/usr/bin/python3
import os
import sys

hexaToBinTable = {
    '0': b"0000",'1': b"0001",'2': b"0010",'3': b"0011",'4': b"0100",'5': b"0101",'6': b"0110",'7': b"0111",'8': b"1000",'9': b"1001",'A': b"1010",'B': b"1011",'C': b"1100",'D': b"1101",'E': b"1110",'F': b"1111"
}

base64Table = {
    "000000": b'A', "000001": b'B', "000010": b'C', "000011": b'D', "000100": b'E', "000101": b'F', "000110": b'G', "000111": b'H', "001000": b'I', "001001": b'J', "001010": b'K', "001011": b'L', "001100": b'M', "001101": b'N', "001110": b'O', "001111": b'P', "010000": b'Q', "010001": b'R', "010010": b'S', "010011": b'T', "010100": b'U', "010101": b'V', "010110": b'W', "010111": b'X', "011000": b'Y', "011001": b'Z', "011010": b'a', "011011": b'b', "011100": b'c', "011101": b'd', "011110": b'e', "011111": b'f', "100000": b'g', "100001": b'h', "100010": b'i', "100011": b'j', "100100": b'k', "100101": b'l', "100110": b'm', "100111": b'n', "101000": b'o', "101001": b'p', "101010": b'q', "101011": b'r', "101100": b's', "101101": b't', "101110": b'u', "101111": b'v', "110000": b'w', "110001": b'x', "110010": b'y', "110011": b'z', "110100": b'0', "110101": b'1', "110110": b'2', "110111": b'3', "111000": b'4', "111001": b'5', "111010": b'6', "111011": b'7', "111100": b'8', "111101": b'9', "111110": b'+', "111111": b'/'
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


def hexToBase64(cnt):
    global hexaToBinTable
    global base64Table
    hexaBytes = cnt.encode('utf-8')
    rawBin = bytes()
    res = bytes()

    for byte in hexaBytes:
        rawBin += hexaToBinTable[chr(byte)]
    splitBin = [rawBin[i:i+6] for i in range(0, len(rawBin), 6)]
    for i in range(0, 6 - len(splitBin[len(splitBin) - 1])):
        splitBin[len(splitBin) - 1] += b'0'
    for elm in splitBin:
        res += base64Table[elm.decode("utf-8")]
    if len(res) % 4 != 0:
        for i in range(0, 4 - len(res) % 4):
            res += b'='
    return (res)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wong arguments.", file=sys.stderr)
        exit(84)
    cnt = readFile(sys.argv[1])
    if not cnt:
        exit(84)
    cnt = cnt.upper()
    cnt = cnt.replace('\n', '')
    if not isHexa(cnt) or len(cnt) % 2 != 0 or len(cnt) == 0:
        print("String is not in hexadecimal format.", file=sys.stderr)
        exit(84)
    res = hexToBase64(cnt)
    print(res.decode("utf-8"))
    exit(0)