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
  await function1()
  await function2()
  await function3()
#  L=await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
        
# )
#  print(L) 
asyncio.run(main())

