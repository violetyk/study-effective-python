#!/usr/bin/env python3

#  リスト内包表記
#  comprehension、ここでは「理解」ではなく「含む」の意味

def main():
    x = [i * 2 for i in range(50)]
    print(x)

    #  辞書からタプルのリストにするときによく使われるらしい
    x = {'a': 10, 'b': 20, 'c': 30}
    y = [(key, value) for key, value in x.items()]
    print(y) #  ('a', 10), ('b', 20), ('c', 30)]

    #  ifを後ろにつけられる
    x = [i for i in range(10) if i % 2 == 0]
    print(x)

    #  forも後ろにつけられる
    a = [(x,y) for x in range(3) for y in range(x, 3)]
    print (a) # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

    #  リストではなくセット（集合）にするとジェネレータになる
    #  https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09
    #  ジェネレータはイテレータの一種であり、1要素を取り出そうとする度に処理を行い、
    #  要素をジェネレートするタイプのもの。Pythonではyield文を使った実装を指すことが多いと思われる
    g = ((x,y) for x in range(3) for y in range(x, 3))
    print(g) # <generator object main.<locals>.<genexpr> at 0x103a7c050>
    print(type(g)) # <class 'generator'>
    print(list(g)) # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


if __name__ == '__main__':
    main()
