#https://leetcode.com/problems/implement-queue-using-stacks/description/
class MyQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def _scroll(self):
        while self._in:
            self._out.append(self._in.pop())

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        if not self._out:
            self._scroll()
        return self._out.pop()

    def peek(self) -> int:
        if not self._out:
            self._scroll()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out