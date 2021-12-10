class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.key)
    
    def preorder(self):
        if self != None:
            print(self.key)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()


"""이진탐색트리:
    각 노드의 왼쪽 서브트리의 key값은 본 노드의 key값보다 작거나 같아야하고, 
            오른쪽 서브트리의 key값은 본 노드의 key값보다 커야한다 """

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
        
    def find_loc(self, key): #특정 key값의 로케이션을 찾는 것. 만약에 해당 노드가 있다면 그 노드의 key값을 리턴, 만약에 해당 노드가 없다면 그 노드가 삽입돼야할 곳의 부모노드를 리턴 
        if self.size == 0:
            return None
        P = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                P = v 
                v = v.right #v를 더 큰 값으로 업데이트
            else: #v.key > key
                P = v
                v = v.left    
        return P # 없을 경우에 부모노드를 리턴
    
    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v #부모노드 리턴 되는 게 아닌가요?

    def insert(self, key):
        p = self.find_loc(key)
        if  p == None or p.key != key:
            v = Node(key)
            if p == None: #bsr가 empty 인 것, insert될 키를 root로 만들어야 하는 상황
                self.root = v
            else : 
                v.parent =  p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print("중복임")
    
    def deleteByMerging(self, x):
        """ c = X 자리를 대체할 노드
            m = L에서 가장 큰 노드"""

        a = self.left
        b = self.right
        if a != None:
            c = a
            m = a
            while m.right:
                m = m.right
            if b != None:
                b.parent = m
                m.right = b
        else: #a==None
            c = b
            if self.parent != None:
                if c:
                    c.parent = self.parent
                    if self.parent.key < c.key:
                        self.parent.right = c
                    else:
                        self.parent.left = c
            else:
                self.parent = None
        self.size -= 1


T = BST()
T.insert(15)
T.insert(3)
T.insert(4)
T.insert(10)
T.insert(11)