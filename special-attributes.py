#!/usr/bin/env python


import math

class Point:
    #  __doc__ docstring。トリプルクォーテーションでくくられた改行含む文字列。サブクラスに継承はされない。
    """この文字列は
    1つの文字列として
    扱われます。"""

    #  __init__() コンストラクタ
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


    #  __getattribute__() クラスのメンバやメソッドを参照できる。
    #  __getattribute__のフォールバック
    def __getattr__(self, item):
        print(item)
        return 'Member not found'

    #  __getitem__はクラスのインスタンスに対して辞書のindexでアクセスした場合
    def __getitem__(self, item):
        print(f'__getitem__({item}) is called')
        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y


def main():
    point = Point(10, 20)
    print(point.__doc__)

    print(point.x)
    #  print(point.__getattribute__('x')) とおなじ
    print(point.distance())
    #  print(point.__getattribute__('distance')()) とおなじ

    print(point.x2)
    #  point.__getattribute__('x2')のフォールバックで__getattr__('x2') が呼ばれる


    #  point.__getitem__('x')が呼ばれる
    print(point['x'])
    print(point['y'])

    point.x = 30

if __name__ == '__main__':
    main()
    
