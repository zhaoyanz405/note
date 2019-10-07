#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 11:14
"""
import threading


class OptimismLock:
    def __init__(self, data):
        """
        :param data: 要加锁的数据
        """
        self.lock = threading.RLock()
        self.data = data
        self.version = 0

    def acquire(self):
        self.lock.acquire()
        data, ver = self.data, self.version
        self.lock.release()
        return data, ver

    def update(self, up_data, version):
        self.lock.acquire()
        if version != self.version:
            self.lock.release()
            return False

        self.data = up_data
        self.version += 1
        self.lock.release()
        return True
