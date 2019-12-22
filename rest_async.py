import asyncio
import json
import time

import aiohttp


async def worker(name, n, session):
    print(f"worker {name}")
    url = f"http://qrng.anu.edu.au/API/jsonI.php?length={n}&type=uint16"
    response = await session.request(method="GET", url=url)
    value = await response.text()
    value = json.loads(value)
    return value["data"]


async def main():
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(
            *(worker(f"w-{i}", n, session) for i, n in enumerate(range(2, 10)))
        )
        print(f"response is {sums}")


if __name__ == "__main__":
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed:0.2f} seconds")
