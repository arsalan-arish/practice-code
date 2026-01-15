# from contextlib import contextmanager, asynccontextmanager
# import time
# import asyncio
# import os
# import inspect

# async def main():
#     pass

# x = main()
# print(dir(x))

# # Filter to see only your custom methods (ignoring dunders)
# methods = [m for m in dir(x) if not m.startswith('__')]
# print(methods)

# methods = inspect.getmembers(x, predicate=inspect.ismethod)
# for name, func in methods:
#     print(f"Method Name: {name}")

#! ---------------------------------- Context Manager --------------------------------------------------------
# #* Synchronous Context Manager

# @contextmanager
# def myManager1(n: int):  # The arguments specified here take place of the __init__ section
#     # The code of __enter__ section
#     value = n**2
#     try:
#         # This contains only the return statement of the __enter__ section
#         yield value
#     except Exception as e:
#         pass # Equivalent to "return True" in __exit__
#     finally:
#         # This contatins the code of the __exit__ section, although exception handling is done by above block
#         print("Closing...")
# # TODO If I don't want to manipulate exceptions and propagate them automatically
# def myManager1(n: int):
#     # The code for the __enter__ section
#     value = n**2
#     yield value # yield instead of return
#     # The code for the __exit__ section
#     print("Closing...")

# #! Equivalent manual implementation
# class myManager2:
#     def __init__(self, n: int):
#         self.n = n
#     def __enter__(self):
#         value = self.n**2
#         return value
#     def __exit__(self, type, value, traceback):
#         print("Closing...")
#         return True

# # Testing
# x = 5
# with myManager1(x) as sq1:
#     print(f"The value is {sq}")
#     raise # This error does not affect
# with myManager2(x) as sq1:
#     print(f"The value is {sq}")
#     raise # This error does not affect


# #* Asynchronous Context Mangager

# @asynccontextmanager
# def myManager3(n: int):
#     pass

# #! Equal manual implementation 
# class myManager4:
#     def __init__(self, n):
#         self.n = n
#     def __aenter__(self):
#         pass
#     async def __aexit__(self, type, value, traceback):
#         pass 

# # Testing
# x = 5
# with myManager3(x) as sq2:
#     pass
# with myManager4(x) as sq2:
#     pass


#! -------------------------------- Decorators -------------------------------------------------------
# TODO - Create a timer function decorator that stores the time a function takes to execute in __time__

# def timer(f):
#     def decorator(*args):
#         start = time.perf_counter()
#         print(f"Function {f.__name__} took {round(time.perf_counter() - start, 3)} seconds to execute.")
    
#     return decorator


# @timer
# def func(n, x):
#     for _ in range(n):
#         print("Hello!")
    
# @timer
# def func1(n: int):
#     lst = []
#     for i in range(n):
#         lst.append(i)
#     print(lst[-1])
#     return

# help(range)

# #! -------------------------------- Iterator -------------------------------------------------------
# # TODO - Create an iterator class object based on the python iterator protocol

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __iter__(self):
#         self.i = 1
#         self.attrs = list(self.__dict__.items())
#         return self
#     def __next__(self):
#         if self.i <= len(self.attrs):
#             ans = self.attrs[(self.i)-1]
#             self.i += 1
#             return ans
#         else:
#             raise StopIteration



# x = Human("Tom", 10)

# for attr in x:
#     print(attr)
