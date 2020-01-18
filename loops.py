#!/usr/bin/env python3

def main():
    #  リスト
    values = [0, 1, 2]
    for value in values:
        print(f'The value is {value}')

    #  タプル
    values = (0, 1, 2)
    for value in values:
        print(f'The value is {value}')

    #  辞書はそのままだとキーがループされる
    items = {'a': 1, 'b': 2, 'c': 3}
    for key in items:
        print(f'The key is {key}')

    #  辞書でバリューを取るとき
    for value in items.values():
        print(f'The value is {value}')

    #  foreach的なのをするときはitems()
    for key, value in items.items():
        print(f'The pair of key and value is ({key}, {value})')

    #  python3ではxrangeなくなってxrangeがrangeになった
    print(type(range(10))) # <class 'range'>
    print(list(range(0, 10, 2))) #[0, 2, 4, 6, 8]
    print(0 in range(0, 10, 2)) # True
    print(10 in range(0, 10, 2)) # False

    for value in range(0, 10, 2):
        print(f'The value is {value}')

    x = [10, 20, 30, 40, 50]
    index = 0

    while index < 5:
        print(f'The value is {x[index]}')
        index += 1

    #  無限ループ
    #  while True:
        #  print('.', end='')



if __name__ == '__main__':
    main()
