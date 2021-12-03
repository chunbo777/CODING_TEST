class Node():
    def __init__(self, key=None):
        self.key=key
        self.next = None
        
    def __str__(self):
        return str(self.key)

    
    
class LL(Node):    
    def __init__(self, key = None):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def push_front(self, key =None):
        node = Node(key)
        node.next = self.head
        self.head = node
        self.size += 1  

    def push_back(self, key = None):
        node = Node(key)
        if len(self) == 0 :
            self.head  = node 
        else:
            tail = self.head
            while tail.next != None:
                tail =  tail.next
            tail.next = node
        self.size += 1

    def pop_front(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key
    def pop_back(self):
        if len(self) == 0:
            return None
        else:
            tail = self.head
            prev = None
            while tail.next != None:
                prev = tail
                tail =  tail.next
            x = tail
            prev.next = tail.next
            key = x.key
            self.size -= 1
            del x
            return key

    def search(self, key):
        start = self.head
        while start != None:
            start=start.next
            if start.key == key:
                return start

class LL_2():
    def __init__(self):
    
        self.head = dummy
            


Node(3)
ll = LL()
ll.push_front(3)
ll.push_front(5)
ll.push_front(7)
ll.push_back(3)
ll.push_back(7)
ll.search(3)
print(ll.size)

# ll= LL()
# ll(7)
# ll(3)
# ll(2)
# ll(1)


             
        