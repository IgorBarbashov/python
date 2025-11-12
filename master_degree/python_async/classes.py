import asyncio


class NeiroGetway:

    # стандартный __init__() не может быть корутиной и должен возвращать None
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    async def init(cls, host, port):
        self = cls(host, port)

        con = await self.async_con()

    async def async_con(self):
        print("connection ....")
        await asyncio.sleep(1)

    async def close(self):
        print("colosing ....")
        await asyncio.sleep(1)

    # метод нужен чтобы мы могли использовать класс как контекстный менеджер
    # вызывается при создании менеджера
    async def __aenter__(self):
        print("Init")
        await NeiroGetway.init(self.host, self.port)
        return self

    # метод нужен чтобы мы могли использовать класс как контекстный менеджер
    # этот метод высвобождает ресурсы
    async def __aexit__(self, a, b, c):
        await self.close()

    async def send(self):
        print("sending")
        await asyncio.sleep(1)


async def main():
    async with NeiroGetway("192.168.1.1", 984) as connection:
        task1 = asyncio.create_task(connection.send())


if __name__ == "__main__":
    asyncio.run(main())
