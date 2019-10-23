#! /usr/bin/python

"""
@author: yan.zhao
@contact: yan.zhao@idiaoyan.com
@time: 2019/10/23 9:50
"""


def func():
    """
    普通函数
    :return:
    """
    return 1


def generator():
    """
    生成器函数
    :return:
    """
    for i in range(10):
        yield i


# after python version >= 3.5
async def async_function():
    """
    异步函数
    :return:
    """
    async for i in async_generator():
        if i == 9:
            return i


async def async_generator():
    """
    异步生成器
    :return:
    """
    for i in range(10):
        yield i


# print(type(func))
# print(type(generator()))
# print(type(async_function()))
# print(type(async_generator()))
try:
    async_function().send(None)
except StopIteration as e:
    print(e.value)
