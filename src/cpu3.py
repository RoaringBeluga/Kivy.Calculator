from dataclasses import dataclass

from quacks.stack import Stack


@dataclass
class Opcodes:
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'


class CalcCPU3:

    def __init__(self):
        self._stack = Stack(depth=2)
        self._opcode = ''

    @property
    def display(self):
        data = self._stack.top
        return self._stack.top

    @display.setter
    def display(self, value):
        if self._stack.top:
            self._stack.top = value
        else:
            self._stack.push(value)

"""
if op = operation:
    if stack.empty:
        do_nothing()
        break
    if stack.full
    
"""