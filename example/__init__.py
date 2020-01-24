# import exampleでexample.a.fib()できるようにする
# 相対インポート
from . import a

#  ModuleNotFoundError: No module named 'a'
#  import a


#  Python はモジュールを探しに行くときに次の順序でモジュールを検索する
#  1. ビルトインモジュール（Python に最初から組み込まれたモジュール）
#  2. python コマンドに渡したファイルのあるディレクトリ直下
