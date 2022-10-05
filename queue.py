
class queue:
    def __init__(self):
        self.data =[]

    def queueisfull(self):
        if len(self.data) == 5:
            return 'Queue is full'
        else:
            return f'Queue has {5-len(self.data)} space'

    def enqueue(self,element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return 'overflow'

    def dequeue(self):
        if len(self.data) == 0:
            return 'underflow'
        else:
            self.data.pop(0)


queue = queue()

print(queue.dequeue())
queue.enqueue(12)
print(queue.queueisfull())
queue.enqueue(25)
queue.enqueue(16)
queue.enqueue(19)
queue.enqueue(17)
print(queue.data)
queue.dequeue()
print(queue.data)