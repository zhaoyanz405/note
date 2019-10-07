#!/bin/python
"""
author: yan.zhao
contact: zhaoyanz405@gmail.com
date: 2019/10/7 9:15
"""


class Node:
    def __init__(self, data, next_point=None):
        """

        :param data:
        :param next_point:
        """
        self.data = data
        self.next = next_point


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head

    # 不可以，因为调用next后，本质上这个链表的长度变短了
    # def next(self):
    #     if self.head.next:
    #         self.head = self.head.next
    #     else:
    #         raise StopIteration

    def append(self, node: Node):
        if not self.head:
            self.head = node
            return

        # 否则遍历，append到队尾
        latest = self.head
        while latest.next:
            latest = latest.next
        latest.next = node

    def insert(self, anchor, node: Node):
        latest = self.head
        if latest is anchor:
            latest.next, node.next = node, latest.next

        while latest.next:
            latest = latest.next
            if latest is anchor:
                latest.next, node.next = node, latest.next

    def show(self):
        latest = self.head
        while latest:
            print(latest.data)
            latest = latest.next


node1 = Node('1')
node2 = Node('2')
node3 = Node('3')

sl = SingleLinkedList(head=node1)
sl.append(node2)
sl.append(node3)
sl.insert(node1, Node('4'))
sl.show()
