#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 9:15
"""


class Node:
    def __init__(self, data, next_point):
        """

        :param data:
        :param next_point:
        """
        self.data = data
        self.next = next_point


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def next(self):
        if self.head.next:
            self.head = self.head.next
        else:
            raise StopIteration


node3 = Node('3', None)
node2 = Node('2', node3)
node1 = Node('1', node2)

sl = SingleLinkedList()
sl.head = node1

while True:
    try:
        print(sl.head.data)
        sl.next()
    except StopIteration:
        print('end')
        break
