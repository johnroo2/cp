class MinStack:
    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.arr = self.arr + [val]
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:-1]
        self.minStack = self.minStack[:-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
