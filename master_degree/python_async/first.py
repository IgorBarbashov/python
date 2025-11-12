import asyncio
import random


async def func(s):
    r = random.random()
    await asyncio.sleep(s)
    return r


async def value(s):
    v = await func(s)
    print(v)


async def count(c, t):
    cnt = 0
    result = 0

    while True:
        print(result)
        result += c
        cnt += 1

        if cnt > t:
            break

        await asyncio.sleep(.1)

    await asyncio.sleep(.5)
    print("end count")


async def main():
    # запуск нескольких функций в EventLoop
    await asyncio.gather(
        value(1),
        count(1, 22),
        value(2),
        value(3)
    )

if __name__ == "__main__":
    asyncio.run(main())
