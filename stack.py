
class stack:
    def __init__(self):
        self.data= []

    def stackismax(self):
        if len(self.data)  == 5:
            return 'stack is full'
        else:
            return f'stack has {5- len(self.data)} space in it'

    def push(self,element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return 'overflow'

    def pop(self):
        if len(self.data) == 0:
            return 'underflow'
        else:
            self.data.pop()


stack = stack()

print(stack.pop())
stack.push(12)
print(stack.stackismax())
stack.push(24)
stack.push(16)
stack.push(18)
stack.push(19)
stack.push(15)
print(stack.data)
print(stack.stackismax())