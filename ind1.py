#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    Aliter = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    f = open('d:\\text.txt', 'r')
    for line in f:
        w = line.split(' ')
        for elem in w:
            if elem[0] in Aliter:
                print(elem)
    f.close()
