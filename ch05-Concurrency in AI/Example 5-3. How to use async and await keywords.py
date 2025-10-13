import asyncio

async def main():
    print("Before sleeping")
    await asyncio.sleep(3) # Simulate a blocking I/O operation
    print("After sleeping for 3 seconds")

asyncio.run(main())