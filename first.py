import asyncio
import random


async def my_coroutine(i):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f"coroutine{i} after {process_time} seconds    ")


async def main():
    tasks = []
    for i in range(100):
        tasks.append(asyncio.ensure_future(my_coroutine(i)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    loop.close()

