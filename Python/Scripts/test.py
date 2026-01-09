import asyncio

# async def fetch(id, ttime):
#     print(f"Fetching data for process {id}")
#     await asyncio.sleep(ttime)
#     print(f"Data Fetched for process {id}")
#     return {"Data" : id}

# async def main():
#     print("Started main() function")
#     data1 = await fetch(1,3)
#     data2 = await fetch(2,3)
#     print(f"{data1}\n{data2}")
#     return

# asyncio.run(main())
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

func = count_up_to(5)