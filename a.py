#!/usr/bin/python

# Fibonacci
#
# 1 1 2 3 5 8 13 21 34 55 
if __name__ == '__main__':
    a = 1
    b = 1 
    print(a)
    print(b)
    #for i in range(10):
    for i in range(10**9):
        a = a + b
        b = a + b
        print(a)
        print(b)
