import asyncio
from datetime import datetime
from random import randint

# async def slow_operation():
#     await asyncio.sleep(1)
#     return 'Future is done'
#
#
# def got_result(future):
#     print(future.result())
#     loop.stop()
#
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(slow_operation())
# task.add_done_callback(got_result)
# loop.run_forever()


async def slow_routine():
    await asyncio.sleep(3)
    return datetime.now()

# print(datetime.now())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*[
#     slow_routine()
#     for x in range(3)
# ]))
# print(datetime.now(), ' ')


async def gen_list():
    await asyncio.sleep(1)
    list1 = [
        randint(1, 10)
        for x in range(5)
    ]
    print(list1)
    return list1


async def sqrt_coro():
    result = await gen_list()
    print([
        pow(x, 1/2)
        for x in result
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(sqrt_coro())
