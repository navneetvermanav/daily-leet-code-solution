class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.rear, self.front = 0, 0
        self.arr = [None] * self.k

    def inc(self, i: int) -> int:
        return 0 if i >= self.k-1 else i + 1

    def dec(self, i: int) -> int:
        return self.k-1 if i == 0 else i - 1

    def enQueue(self, value: int) -> bool:
        if self.arr[self.rear] == None:
            self.arr[self.rear] = value
            self.rear = self.inc(self.rear)
            return True
        return False

    def deQueue(self) -> bool:
        if self.arr[self.front] == None: return False
        self.arr[self.front] = None
        self.front = self.inc(self.front)
        return True

    def Front(self) -> int:
        if self.arr[self.front] == None: return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.arr[self.dec(self.rear)] == None: return -1
        return self.arr[self.dec(self.rear)]

    def isEmpty(self) -> bool:
        if self.arr[self.front] is None and self.arr[self.rear] is None: return True
        return False

    def isFull(self) -> bool:
        if self.arr[self.front] and self.arr[self.rear]: return True
        return False