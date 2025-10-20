#https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int | None) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def __len__(self):
        return len(self.queue)

    def empty(self) -> bool:
        return len(self.queue) == 0

#solution using 1 queue
class MyStack:
    def __init__(self):
        self.queue = MyQueue()
        self.queue.push(None)

    def push(self, x: int) -> None:
        self._scroll_forward()
        self.queue.push(x)

    def _is_forward(self):
        return self.queue.peek() is None

    def _scroll(self):
        if self._is_forward():
            self._scroll_backwards()

    def _scroll_forward(self):
        while not self._is_forward():
            self.queue.push(self.queue.pop())

    def _scroll_backwards(self):
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self) -> int:
        self._scroll()
        return self.queue.pop()

    def top(self) -> int:
        self._scroll()
        return self.queue.peek()

    def empty(self) -> bool:
        return len(self.queue) == 1

#solution using 2 queues
class MyStack2:

    def __init__(self):
        self._in = MyQueue()
        self._out = MyQueue()

    def push(self, x: int) -> None:
        self._in.push(x)

    def _balance(self):
        if self._in.empty():
            if self._out.empty():
                raise IndexError("Stack is empty")
            self._in, self._out = self._out, self._in
        while len(self._in) > 1:
            self._out.push(self._in.pop())

    def pop(self) -> int:
        self._balance()
        return self._in.pop()

    def top(self) -> int:
        self._balance()
        return self._in.peek()

    def empty(self) -> bool:
        return self._in.empty() and self._out.empty()
