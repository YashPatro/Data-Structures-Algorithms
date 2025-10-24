#24/10/25

class Queu:
    def __init__(self,queue,max):
        self.front = 0
        self.rear = 0
        self.queue = queue
        self.max = max
        self.available = max
    def enqueue(self,item):
        if self.available  == 0:
            print('queue overflow')
        else:
            #self.queue.insert(self.rear,item)
            self.queue[self.rear] = item
            self.rear += 1
            self.available -= 1
    def dequeue(self):
        if self.available  == self.max:
            print('queue underflow')
        else:
            #self.queue.insert(self.rear,item)
            self.queue[self.rear] = None
            self.front += 1
            self.available += 1
    def peak(self):
        print(self.queue[self.front])
    def getRear(self):
        print(self.queue[self.rear])
    def displayQ(self):
        print(self.queue)

q1 = []

queue1 = Queu(q1,5)
queue1.enqueue(10)