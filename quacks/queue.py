class Queue:

    def __init__(self, length=1, blocking=True):
        if length is not int or len < 1:
            raise ValueError('Length must be int and not less than 1')
        self._data = []
        self._max_len = length
        self._blocking = blocking

    @property
    def max_length(self):
        return self._max_len

    @max_length.setter
    def set_max_length(self, length):
        if length is not int or len < 1:
            raise ValueError('Length must be int and not less than 1')
        else:
            self._max_len = length

    def push(self, value):
        if len(self._data) < self._max_len:
            self._data.append(value)
        elif not self._blocking:
            self._data.pop()
            self._data.append(value)
        else:
            raise IndexError('Queue is full.')

    def pop(self):
        if len(self._data) > 0:
            return self._data.pop()
        else:
            raise IndexError('Queue is empty.')