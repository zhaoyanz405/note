#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author: Zhao Yan
# @datetime: 8/31/18 10:36 AM
import time, random
from queue import Queue
from threading import Thread

class Producer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print('%s is producing %d to the queue!' % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.randint(0, 5))

        print('%s finished!' % self.getName())



class Consumer(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        print(self.data.empty())
        for i in range(5):
            value = self.data.get()
            print("%s is consuming. %d in the queue is consumed." % (self.getName(), value))
        print(self.data.empty())



if __name__ == '__main__':
    queue = Queue(100000)
    producer = Producer('Producer', queue)
    consumer = Consumer('Consumer', queue)

    producer.start()
    consumer.start()

    producer.join()
    Producer('Produce2', queue).start()
    consumer.join()
    print("all finished")
