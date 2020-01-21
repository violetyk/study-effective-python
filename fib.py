#!/usr/bin/env python3


#  print(__name__) # fib

#  フィボナッチ数列（前の2つを加えると次の数になる）
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end= ' ')
        a, b = b, a + b

    #  print()

def myfunc():
    print('myfunc!')
