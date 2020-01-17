#!/usr/bin/env python

#  https://rinatz.github.io/python-book/ch02-01-variables/

def main():
    #  x = 10
    x = 5 / 2  # 除算。整数に対しての/はPython2だと商(=2)、Python3だと除算(=2.5)になる
    y = 5 // 2 # 商
    print(x)
    print(y)


    #  bool
    t = True
    f = False
    #  t = true # Name Error
    #  f = false # Name Error
    print(t)
    print(f)


    #  string
    x = 'hello, world'
    y = '日本語'
    print(x)
    print(y)

    x = 10
    s1 = f'The value of x is {x}'
    s2 = f'The value of x * x is {x * x}'
    print(s1)
    print(s2)

    s3 = 'The value of x is {}'.format(20)
    s4 = 'The value of name is {name}'.format(name = 'Taro')
    print(s3)
    print(s4)

    b1 = b'0xDEADBEEF'
    print(b1)


    #  list 
    l1 = [0, 1, 2, 3, 4]
    l2 = [10, 3.14, 'hello, world!']
    l3 = [
        'hoge',
        'fuga',
        'wef',
    ]
    print(l1)
    print(l2)
    print(l3)


    l1.append(5)
    l1.append(l2)
    print(l1) #[0, 1, 2, 3, 4, 5, [10, 3.14, 'hello, world!']]
    print(l1[0])
    print(l1[6])
    print(l1[6][2])
    print(l1[-2])

    # tuple 要素変更ができないので必要ない場合はlistより安全
    t1 = (0, 1, 2, 3, 4)
    # tupleはカッコがなくてもOK
    t2 = 10, 3.14, 'hello, world'
    # 空のタプル
    t3 = ()
    print(t1)
    print(t2)
    print(t3)


    #  アンパック代入 listでもtupleでもできる
    x = (10, 3.14, 'hello, world')
    a, b, c = x
    print(a, b, c)
    x = [0, 1, 2, 3, 4]
    # ValueError: too many values to unpack (expected 3)
    #  a, b, c = x
    a, b, *c = x
    # cは[2, 3, 4]になる
    print(a, b, c)


    # dict
    x = {
        'name': 'Taro',
        'age': 30,
    }
    print(x)
    print(x['name'])
    #  AttributeError: 'dict' object has no attribute 'name'
    #  print(x.name)
    print(type(x)) #<class 'dict'>


    # set(集合)
    s = {1, 2, 3, 4, 1, 2, 3} 
    print(s)
    print(type(s)) #<class 'set'>

    # set型は順序を持たない
    s = {1.23, '百', (0, 1, 2), '百'}
    print(s) # {(0, 1, 2), 1.23, '百'}]

    # set型は更新可能なオブジェクトは登録できない
    #  TypeError: unhashable type: 'list'
    #  s = {[0, 1, 2]}
    #  TypeError: unhashable type: 'dict'
    #  s = {{'name': 'Taro'}}

    #  set型は型が違っても等価であれば重複と見なす
    s = {100, 100.0}
    print(s)


    #  空のdictは{}で作り、空のset型はコンストラクタで作る
    a = {}
    print(type(a)) # <class 'dict'>
    b = set()
    print(type(b)) # <class 'set'>


    #  frozenset型はイミュータブルなset型
    s = {1, 2, 3, 4, 1, 2, 3} 
    fs = frozenset(s)
    print(fs) #frozenset({1, 2, 3, 4})
    print(type(fs)) #class 'frozenset'>

    # listへの変換
    l = list(fs)
    print(l, type(l)) # [1, 2, 3, 4] <class 'list'>

    # tupleへの変換
    t = tuple(fs)
    print(t, type(t)) # (1, 2, 3, 4) <class 'tuple'>


    #  集合内包表記（リスト内包表記や辞書内奥表記もある）
    #  内包表記(comprehension)
    print(range(5)) # range(0, 5)
    s = {i**2 for i in range(5)}
    print(s) # {0, 1, 4, 9, 16}

    #  集合の要素数
    s = {1, 2, 3, 4, 1, 2, 3}
    print(len(s)) # 4

    #  集合に要素を追加
    s = {1, 2, 3, 4, 1, 2, 3}
    s.add(4)
    s.add(5)
    s.add(5)
    print(s) # {1, 2, 3, 4, 5}


    #  集合から要素を削除
    #  discard()は要素がなくてもエラーにならない
    #  remove()は要素がないとエラー
    #  pop()は要素を返し削除するがどの値かは選択できない
    #  clear()で全て消す
    s = {1, 2, 3, 4, 1, 2, 3}
    s.discard(3)
    print(s) # {1, 2, 4}
    s.remove(2)
    print(s) # {1, 4}
    #  s.remove(2) # KeyError: 2

    v = s.pop()
    print(v, s) # 1 {4}
    v = s.pop()
    print(v, s) # 4 set()
    #  v = s.pop() # KeyError: 'pop from an empty set'

    s = {1, 2, 3, 4, 1, 2, 3}
    s.clear()
    print(s)

    #  和集合 | または union()
    s1 = {0, 1, 2}
    s2 = {1, 2, 3}
    s3 = {2, 3, 4}

    print(s1 | s2) # {0, 1, 2, 3}
    print(s1.union(s2)) # {0, 1, 2, 3}
    print(s1 | s2 | s3) # {0, 1, 2, 3, 4}
    print(s1.union(s2, s3)) # {0, 1, 2, 3, 4}
    # リストやタプル引数に指定できる
    print(s1.union(s2, s3, [ 5, 6, 5, 7, 5])) # {0, 1, 2, 3, 4, 5, 6, 7}

    # 積集合 & または intersection()
    print(s1 & s2)
    print(s1.intersection(s2))
    print(s1 & s2 & s3)
    print(s1.intersection(s2, s3)) #{2}
    print(s1.intersection(s2, s3, [2, 3, 4])) #{2}

    # 差集合 - または difference()
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(a - b) # {1, 2}
    print(a.difference(b)) # {1, 2}
    print(b - a) # {4, 5}
    print(b.difference(a)) # {4, 5}


    #  対象差集合（どっちか一方にだけ含まれる。論理演算の排他的論理和XOR）
    #  ^ または symmetric_difference()
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(a ^ b) #{1, 2, 4, 5}
    print(a.symmetric_difference(b)) #{1, 2, 4, 5}


    #  部分集合か判定 <= または issubset()
    #  真部分集合か判定するには <
    s1 = {0, 1}
    s2 = {0, 1, 2}
    print(s1 <= s2) # True
    print(s1.issubset(s2)) # True
    print(s2.issubset(s1)) # False
    print(s1 <= s1) # True
    print(s1 < s1) # False

    #  上位集合か判定 >= または isupperset()
    #  新上位集合上か判定するには >
    print(s2 >= s1) # True
    print(s2.issuperset(s1)) # True
    print(s1 >= s1) # True
    print(s1 > s1) # False

    # 互いに素か判定 isdisjoint()
    s1 = {0, 1}
    s2 = {1, 2}
    s3 = {2, 3}
    print(s1.isdisjoint(s2)) # False
    print(s1.isdisjoint(s3)) # True


    #  Pythonのnull的なヤツ
    x = None
    print(x) # None


    # 定数はないけど大文字で書いておくルール
    PI = 3.14

if __name__ == '__main__':
    main()
