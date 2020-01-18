#!/usr/bin/env python3

#  if elif else 
#  switchはない
def f1(number):
    if number % 4 == 0:
        print('number is divisible by 4')
    elif number % 3 == 0:
        print('number is divisible by 3')
    elif number % 2 == 0:
        print('number is divisible by 2')
    elif number is None:
        print('number is None')
    else:
        print('number is not divisible by 4, 3, or 2')


def f2(*args):
    for v in args:
        #  ifに直接渡して真偽値判定
        if v:
            print('{v} is True'.format(v=v))
        else:
            print('{v} is False'.format(v=v))
        #  0 is False
        #  0.0 is False
        #  is False
        #  b'' is False
        #  [] is False
        #  () is False
        #  {} is False
        #  set() is False
        #  None is False

#  and, orが使える
#  and使わなくても変数の範囲のチェックができる
def f3(x):
    if x >= 0 and x < 10:
        print(f'{x} is in [0, 10)')
    if 0 <= x < 10: # x >= 0 and x < 10 と同じ
        print(f'{x} is in [0, 10)')


#  in でリスト、タプル、集合内で含まれるかどうか調べる
 # in 文字列だと含まれるかどうか
def f4(data, x):
    if x in data:
        print(f'{data} contains {x}')
    else:
        print(f'{data} not contains {x}')


#  in 辞書だとキーがあるかどうか
def f5(data, key):
    if key in data:
        print(f'{data} contains the value of key {key}')
    else:
        print(f'{data} not contains the value of key {key}')


#  is 同じインスタンスかどうか
#  None のようなシングルトンと比較をする場合は、常にisかis notを使うべきです。絶対に等値演算子を使わないでください。
def f6(x, y):
    if x is y:
        print('x is y == True')
        return
    else:
        print('x is y == False')

    if x == y:
        print('x == y == True')



def main():
    f1(2)
    f1(5)

    f2(0, 0.0, '', b'', [], (), {}, set(), None)

    f3(0)
    f3(1)
    f3(9)
    f3(10)

    f4([0, 1, 2, 3], 2)
    f4([0, 1, 2, 3], 4)
    f4((0, 1, 2), 2)
    f4((0, 1, 2), 3)
    f4({'a', 'b', 'c', 'b'}, 'c')
    f4({'a', 'b', 'c', 'b'}, 'd')
    f4('abcde', 'c') # abcde contains c
    f4('abcde', 'z') # abcde not contains z
    f4('abcde', 'bcd') #abcde contains bcd

    f5({'x': 0, 'y': 1, 'z': 2}, 'x')

    x = [0, 1, 2]
    y = x
    z = x
    f6(y, z)
    x = [0, 1, 2]
    y = [0, 1, 2]
    f6(x, y) # xとyは等値だが別のインスタンス

if __name__ == '__main__':
    main()
    
