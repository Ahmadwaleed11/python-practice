import time
import asyncio

async def function1():
    await asyncio.sleep(2)
    print("hello")

async def function2():
    await asyncio.sleep(2)
    print("hello")

async def function3():
   await asyncio.sleep(2)
   print("hello")

async def main():
 L=await asyncio.gather(
        function1(),
        function2(),
        function3(),
        
)
 print(L) 
asyncio.run(main())

