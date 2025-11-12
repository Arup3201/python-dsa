class CustomPriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, i):
        p = (i-1)//2
        if p<0 or p>=self.size:
            return -1
        return p
    
    def left_child(self, i):
        left = 2*i+1
        if left<0 or left>=self.size:
            return -1
        return left
        
    def right_child(self, i):
        right = 2*i+2
        if right<0 or right>=self.size:
            return -1
        return right
        
    def is_lesser(self, a, b):
        return a[1]<b[1]
    
    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        
        smallest = i
        if left!=-1 and self.is_lesser(self.heap[left], self.heap[smallest]):
            smallest = left
        if right!=-1 and self.is_lesser(self.heap[right], self.heap[smallest]):
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)
    
    def push(self, x):
        self.heap.append(x)
        self.size += 1
        
        i = self.size-1
        while i>0:
            p = self.parent(i)
            if p==-1:
                break
            
            if self.is_lesser(self.heap[i], self.heap[p]):
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            
            i = p
        
    def pop(self):
        m = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap = self.heap[:self.size-1]
        self.size-=1
        self.heapify(0)
        return m
    
def test_custom_pq_push():
    test_cases = [
        {
            "arr": [[0, 5], [1, 2], [2, 4], [3, 1]], 
            "output": [[3, 1], [1, 2], [2, 4], [0, 5]]
        }
    ]

    for tc in test_cases:
        pq = CustomPriorityQueue()
        for elm in tc["arr"]:
            pq.push(elm)
        assert pq.heap == tc["output"], tc["arr"]

def test_custom_pq_pop():
    test_cases = [
        {
            "arr": [[0, 5], [1, 2], [2, 4], [3, 1]], 
            "popped": [3, 1],
            "output": [[1, 2], [0, 5], [2, 4]]
        }
    ]
    for tc in test_cases:
        pq = CustomPriorityQueue()
        for elm in tc["arr"]:
            pq.push(elm)
        elm = pq.pop()
        assert elm == tc["popped"]
        assert pq.heap == tc["output"], tc["arr"]