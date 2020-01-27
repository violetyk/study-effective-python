#!/usr/bin/env python3

import sys
from concurrent.futures import (
    ThreadPoolExecutor,
    Future,
    as_completed,
    wait
)

from hashlib import md5
from pathlib import Path
from urllib import request

import time
import threading

urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://instagram.com',
]

def f(val):
    return val


def download(url):
    req = request.Request(url)
    #  ファイル名に/等が含まれないようにする
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './tmp/' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
    return url, file_path

def main():
    #  print(sys.version)
    #  スレッドベースの非同期実行
    future = ThreadPoolExecutor().submit(f, 'wef')
    is_feature = isinstance(future, Future)
    print(is_feature)

    result = future.result()
    print(result)

    is_running = future.running()
    print(is_running)

    is_done = future.done()
    print(is_done)

    is_cancelled = future.cancelled()
    print(is_cancelled)

    #  print(download(urls[0]))
    get_sequentials()
    get_multi_thread()

    counter = Counter()
    threads = 2
    with ThreadPoolExecutor() as e:
        #  2つのスレッドを用意し、それぞれcount_upを呼び出す
        futures = [e.submit(count_up, counter) for _ in range(threads)]
        done, not_done = wait(futures)
        print(done, not_done)

    print(f'{counter.count} != 2000000')


    counter2 = ThreadSafeCounter()
    threads = 2
    with ThreadPoolExecutor() as e:
        #  2つのスレッドを用意し、それぞれcount_upを呼び出す
        futures = [e.submit(count_up, counter2) for _ in range(threads)]
        done, not_done = wait(futures)
        print(done, not_done)

    print(f'{counter2.count} == 2000000')


#  実行時間を計るデコレータ
def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper


#  逐次実行
@elapsed_time
def get_sequentials():
    for url in urls:
        print(download(url))

# マルチスレッドで並行化
@elapsed_time
def get_multi_thread():
    #  max_workersのデフォルトはコア数x5
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in urls]
        for future in as_completed(futures):
            #  完了したものから取得できる
            print(future.result())


#  スレッドセーフになっていない実装
class Counter(object):

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


class ThreadSafeCounter(object):
    #  ロックを用意する
    lock = threading.Lock()
    def __init__(self):
        self.count = 0

    def increment(self):
        #  ロックを獲得して処理が終わったら速やかにロックを解放する
        #  解放漏れを防ぐためにもLockオブジェクトはwithと一緒に使う
        with self.lock:
            #  排他制御したい一連の処理をこのブロック内に書く
            self.count = self.count + 1


def count_up(counter):
    for _ in range(1000000):
        counter.increment()


if __name__ == '__main__':
    main()
