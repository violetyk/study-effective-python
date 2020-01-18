#!/usr/bin/env python

#  https://rinatz.github.io/python-book/ch02-02-functions/

#  関数の間は2行開ける
#  デフォルト引数は最後
#  デフォルト引数の=左右はスペースを空けない
#  キーワード引数は順不同でOK
#  return しなかった場合はNoneが返る

def f1(x, y=20):
    print(f'The value of x is {x}')
    print(f'The value of y is {y}\n')


#  引数に*をつけるとタプルとして受け取れる
#  引数に**をつけると辞書として受け取れる
#  引き数名は自由だけど慣習的に*args, **kwargsが使われる
def f2(a, *args, **kwargs):
    print(f'The value of x is {a}')
    print(f'The value of x is {args}')
    print(f'The value of y is {kwargs}\n')

    #  The value of x is 10
    #  The value of x is (20, 30)
    #  The value of y is {'hoge': 40, 'fuga': 50}


# f3(*args)でアンパックされる
# f3(*kwargs)でdictの各要素をキーワード引数として渡せる
def f3(x, y, z):
    print(f'The value of x is {x}')
    print(f'The value of x is {y}')
    print(f'The value of y is {z}\n')


#  型ヒント
def f4(x: int, y: int):
    #  文字列にかけ算すると繰り返された
    #  The value of x * y is 三十三十三十三十三十三十三十三十三十三十
    print(f'The value of x * y is {x * y}')

    return x * y

#  空の実装にしておきたい場合はpass
def f5():
    pass


def main():
    f1(10)
    f1(10, 30)
    f1(y=10, x=30)

    f2(10, 20, 30, hoge=40, fuga=50)

    args = (0, 1, 2)
    f3(*args)

    kwargs = { 'y': 1, 'x': 0, 'z': 2}
    f3(**kwargs)

    f4(10, 30)
    f4(10, '三十') #実行時、エラーにはらなかった
    v = f4(3, 4)
    print(v)
    print(f'The value of v is {v}')

    f5()


if __name__ == '__main__':
    main()
