def main():
    #  破壊的処理
    org_list = [3, 1, 4, 5, 2]
    org_list.sort()
    print(org_list)

    #  非破壊的処理
    org_list = [3, 1, 4, 5, 2]
    new_list = sorted(org_list)
    print(org_list)
    print(new_list)


    #  keyで並び順返すように指定する
    l = ['Banana', 'Alice', 'Apple', 'Bob']
    l_order = ['Alice', 'Bob', 'Apple', 'Banana']
    print(l)
    print(sorted(l, key=l_order.index))


    d = {
        'Banana': 40,
        'Alice': 30,
        'Apple' : 20,
        'Bob': 10,
    }
    print(d)
    #  辞書のキーでソート
    print(sorted(d.items(), key=lambda x: x[0]))
    #  辞書の値でソート
    print(sorted(d.items(), key=lambda x: x[1]))
    #  辞書のキー指定順でソート
    d_order = ['Alice', 'Bob', 'Apple', 'Banana']
    sorted_d = sorted(d.items(), key=lambda x: d_order.index(x[0]))
    print(sorted_d)

if __name__ == '__main__':
    main()
