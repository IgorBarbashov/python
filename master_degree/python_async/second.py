import asyncio
import time


async def print_name(name, t=15):
    cnt = 0

    while True:
        print(f"{name} - {cnt}")
        cnt += 1

        if cnt > t:
            break

        await asyncio.sleep(.1)


async def waiter():
    while True:
        print("!!! waiter")
        # time.sleep(1) - синхронный sleep заблокирует поток выполнения программы
        await asyncio.sleep(.5)


async def runner():
    # запуск функций в EventLoop с помощью создания задач
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(print_name("first"))
        task2 = tg.create_task(print_name("second"))
        task3 = tg.create_task(waiter())

if __name__ == "__main__":
    asyncio.run(runner())
