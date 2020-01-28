#!/usr/bin/env python3

import asyncio
import random

async def coro():
    return 1


async def call_web_api(url):
    #  Web APIの処理をここではスリープで代用
    print(f'send a request: {url}')
    # ここまで来ると処理が中断されて2番目のコルーチンが動き始める
    #  sleep()で処理が中断される理由はI/O処理待ちだから
    # 3番目のコルーチンがここまできて中断荒れたら、レスポンスが返ってくるまで待機される
    await asyncio.sleep(random.random())
    # レスポンスが返ってきて再開可能になったコルーチンから順次処理再開
    print(f'got a response: {url}')
    return url

async def async_download(url):
    # awaitを使ってコルーチンを呼び出す
    response = await call_web_api(url) 
    return response


async def main():

    #  gather()は複数のコルーチンを受け取るとそれぞれの実行をスケジューリングしてくれる
    #  渡した順番に実行されて返ってくる
    task = asyncio.gather(
        async_download('https://twitter.com'),
        async_download('https://facebook.com'),
        async_download('https://instagram.com'),
    )
    return await task


if __name__ == '__main__':
    #  coro()
    #  asyncio.run(coro())

    #  result = asyncio.run(async_download('https://twitter.com'))
    result = asyncio.run(main())
