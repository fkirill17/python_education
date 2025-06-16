import asyncio


async def hello():
    for i in range(3):
        await asyncio.sleep(1)
        print('Hello')


async def world():
    for i in range(5):
        await asyncio.sleep(2)
        print('World')


async def main():
    await asyncio.gather(hello(), world())


if __name__ == '__main__':
    asyncio.run(main())