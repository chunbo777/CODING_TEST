class Stack:
    def __init__(self):
        self.items = []
    def pop(self, item):
        try:
            self.items.pop(item)
        except:
            print("stack is empty")
        return self.items

    def push(self, item):
        self.items.append(item)
        return self.items

    def top(self):
        return self.items[-1]

    def len(self):
        return len(self.items)

stack = Stack()
stack.push(3)
