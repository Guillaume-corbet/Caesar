#!/usr/bin/python3
import os
import sys

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

def repeating_key_xor(key, cnt):
    i = 0
    tmp = bytes()
    for elm in cnt:
        tmp += bytes([int(elm, 16) ^ int(key[i], 16)])
        if i >= len(key) - 1:
            i = 0
        else:
            i += 1
    tmp = tmp.hex().upper()
    for i in range(0, int(len(tmp) / 2), 1):
        tmp = tmp[:i] + tmp[i+1:]
    return (tmp)

def getKey(key):
    return (int(key, 16))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wong arguments.", file=sys.stderr)
        exit(84)
    cnt = readFile(sys.argv[1])
    if not cnt:
        exit(84)
    cnt = cnt.upper()
    tab = cnt.split('\n', 1)
    if not isHexa(tab[0]) or len(tab[0]) % 2 != 0 or len(tab[0]) == 0:
        print("Key is not in hexadecimal format.", file=sys.stderr)
        exit(84)
    if not isHexa(tab[1]) or len(tab[1]) % 2 != 0 or len(tab[1]) == 0:
        print("Message is not in hexadecimal format.", file=sys.stderr)
        exit(84)
    res = repeating_key_xor(tab[0], tab[1])
    print(res)
    exit(0)