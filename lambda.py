#!/usr/bin/env python3

def main():
    a = [1, 2, 3, 4, 5]
    #  map はジェネレターオブジェクトを返す
    #  ジェネレータをlist()に渡すとリストに変換してくれる
    print(map(lambda x: x * x, a))
    print(list(map(lambda x: x * x, a)))
    pass

if __name__ == '__main__':
    main()
