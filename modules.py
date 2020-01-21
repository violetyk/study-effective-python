#!/usr/bin/env python3

#  https://rinatz.github.io/python-book/ch04-01-modules/

#  fib.pyを取り込む
#  import(モジュール名)
import fib

#  from (モジュール名) import (関数名)
from fib import myfunc

#  from (モジュール名) import (関数名), (関数名)...
#  from fib import fib, myfunc

#  from (モジュール名) import *


def main():
    fib.fib(10)
    #  fib.myfunc
    myfunc()
    #  wef.fib(10)

#  __name__にはモジュール名が入っている
#  print(__name__) #  __main__
#  つまり、自分がインポートされてないときだけmain()を呼び出す
if __name__ == '__main__':
    main()
