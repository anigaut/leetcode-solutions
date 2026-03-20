class MyCircularQueue:

    def __init__(self, k: int):
        self.elements = []
        self.size = k
        self.valid_elements = 0
        self.first = 0

    def enQueue(self, value: int) -> bool:
        if self.valid_elements < self.size:
            self.elements.append(value)
            self.valid_elements += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.valid_elements == 0:
            return False
        self.valid_elements -= 1
        self.elements[self.first] = -1
        self.first += 1
        return True

    def Front(self) -> int:
        if self.valid_elements == 0:
            return -1
        return self.elements[self.first]

    def Rear(self) -> int:
        if self.valid_elements == 0:
            return -1
        return self.elements[len(self.elements) - 1]

    def isEmpty(self) -> bool:
        if self.valid_elements == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.valid_elements == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
