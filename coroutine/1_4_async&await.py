'''
Description: asyncio:python3.4之后的版本
Author: zhengchengzhong
Date: 2021-01-24 14:35:52
'''
import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [asyncio.ensure_future(func1()), asyncio.ensure_future(func2())]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


