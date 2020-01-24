#!/usr/bin/env python3

#  ファイル...モジュール
#  ディレクトリ...パッケージ

#  これは直接ファイル（モジュール）をimoprtしている
#  なので__init__.pyの参照は起こらない
#  import example.a

#  __init__.pyがないと
#  AttributeError: module 'example' has no attribute 'a'
import example #  example/__init__.pyを参照する

def main():
    #  example.a.fib(10)
    a.fib(10)

if __name__ == '__main__':
    main()
