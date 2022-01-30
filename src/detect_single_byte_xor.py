#!/usr/bin/python3
import os
import sys

hexaToBinTable = {
    '0': "0000",'1': "0001",'2': "0010",'3': "0011",'4': "0100",'5': "0101",'6': "0110",'7': "0111",'8': "1000",'9': "1001",'A': "1010",'B': "1011",'C': "1100",'D': "1101",'E': "1110",'F': "1111"
}

binToHexa = {
    "0000": b'0', "0001": b'1', "0010": b'2', "0011": b'3', "0100": b'4', "0101": b'5', "0110": b'6', "0111": b'7', "1000": b'8', "1001": b'9', "1010": b'A', "1011": b'B', "1100": b'C', "1101": b'D', "1110": b'E', "1111": b'F'
}

character_frequencies = {
        'A': .08167, 'B': .01492, 'C': .02782, 'D': .04253,
        'E': .12702, 'F': .02228, 'G': .02015, 'H': .06094,
        'I': .06094, 'J': .00153, 'K': .00772, 'L': .04025,
        'M': .02406, 'N': .06749, 'O': .07507, 'P': .01929,
        'Q': .00095, 'R': .05987, 'S': .06327, 'T': .09056,
        'U': .02758, 'V': .00978, 'W': .02360, 'X': .00150,
        'Y': .01974, 'Z': .00074, ' ': .13000
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
    return (rawHex)

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def hexaToString(input):
    input = input.decode("utf-8")
    string = ""
    for i in range(0, len(input), 2):
        string = string + chr(int("0x" + input[i] + input[i + 1], 16))
    return (string)

def getScore(tmp):
    global character_frequencies
    score = 0
    tmp = hexaToString(binaryToHex(tmp))
    tmp = tmp.upper()
    for i in range(0, len(tmp)):
        if tmp[i] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ :,.!?;\n":
            return (1000000)
        for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            score += abs((tmp.count(let) / len(tmp) * 100) - (character_frequencies[let] * 100))
    return (score)

def detect_single_byte_xor(cnt):
    best_key = 0
    binCnt = bytes()
    for hexChar in cnt:
        binCnt += hexaToBinTable[hexChar].encode('utf-8')
    binsize = len(binCnt)
    for key in range(0, 256):
        byteKey = bytes()
        tmp = bytes()
        encoded_key = format(key, '#08b')[2:]
        encoded_key = '0' * (8 - len(encoded_key)) + encoded_key
        size = len(encoded_key)
        while (size + len(encoded_key) < binsize):
            encoded_key += encoded_key
        for char in encoded_key:
            if len(encoded_key) >= binsize:
                break
            encoded_key += char
        for char in encoded_key:
            byteKey += char.encode('utf-8')
        tmp = bytes([a ^ b for a, b in zip(binCnt, byteKey)])
        score = getScore(tmp)
        if (key == 0):
            best_key = key
            best_score = score
        if score < best_score:
            best_score = score
            best_key = key
    return (hex(best_key), best_score)

if __name__ == "__main__":
    savedScore = 1000000
    line_count = 0
    if len(sys.argv) != 2:
        print("Wong arguments.", file=sys.stderr)
        exit(84)
    cnt = readFile(sys.argv[1])
    if not cnt:
        exit(84)
    cnt = cnt.upper()
    tab = cnt.split('\n')
    cnt = ""
    for elm in tab:
        if not isHexa(elm) or len(elm) % 2 != 0 or len(elm) == 0:
            print("String is not in hexadecimal format.", file=sys.stderr)
            exit(84)
        res, score = detect_single_byte_xor(elm)
        if score < savedScore:
            savedScore = score
            res = res.replace("0x", "")
            cnt = str(line_count) + " " + res
        line_count += 1
    print(cnt)
    exit(0)