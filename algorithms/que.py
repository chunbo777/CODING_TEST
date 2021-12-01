from collections import deque


class Que:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
        return self.queue
    def dequeue(self):
        try:
            self.queue.popleft()
        except:
            print("queue is Empty")
        return self.queue
que = Que()
que.enqueue(3)
que.dequeue()
que.dequeue()    

