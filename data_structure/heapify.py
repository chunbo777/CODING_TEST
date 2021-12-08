# class Heap:
#     def __init__(self, heap):
#         self.heap = heap
#         self.

def makeheap(list):
    n = len(list)
    for k in range(n-1, -1, -1):
        heapify_down(list, k,n)

def heapify_down(list, k, n):
    while list[k].child() != None 



def child():
    