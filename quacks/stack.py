class Stack:

    def __init__(self, depth=1):
        self._data = []
        self._depth = depth

    def push(self, value):
        if len(self._data) < self._depth:
            self._data.insert(0, value)
        elif self._depth == 0:
            self._data.insert(0, value)
        else:
            raise IndexError('Stack overflow')

    def pop(self):
        if len(self._data) > 0:
            return self._data.pop(0)
        else:
            raise IndexError('The stack is empty')

    @property
    def full(self):
        if self._depth == 0:
            return False
        return True if len(self._data) == self._depth else False

    @property
    def empty(self):
        return len(self._data) == 0

    @property
    def top(self):
        if len(self._data) < 1:
            return None
        return self._data[0]

    @top.setter
    def top(self, value):
        if self.empty:
            self._data.insert(0, value)
        else:
            self._data[0] = value
