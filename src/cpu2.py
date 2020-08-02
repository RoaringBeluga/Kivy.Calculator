class CalcCPU2:

    stack = []
    opcode = ''
    display = 0.0
    opcount = 0
    incount = 0

    def calc(self, key):
        if key not in ['+', '-', '*', '/', '=', '']:
            print("No opcode recognized")
            return
        self.push(self.display)
        if(len(self.stack) == 2) or (key == '='):
            print("Performing:\t", self.opcode, " on:")
            print("\t", self.stack)
            self.perform()
        self.opcode = key

    def perform(self):
        print("Trying to execute:\t", self.opcode)
        print("Operation #", self.opcount)
        print("Inputs processed: ", self.incount)
        if   self.opcode == '+':
            self.add()
            self.opcode = ''
        elif self.opcode == '-':
            self.sub()
            self.opcode = ''
        elif self.opcode == '*':
            self.mul()
            self.opcode = ''
        elif self.opcode == '/':
            self.div()
            self.opcode = ''
        elif self.opcode == '=':
            if len(self.stack) < 2:
                self.push(0)
                self.perform()
            else:
                self.opcode = ''
                self.perform()
        else:
            print("Strange operation: '" + self.opcode + "'")
        print("Result:\t", self.display)
        print("\tOperations:\t", self.opcount, "\n\tInputs:\t", self.incount)

    def input(self, num):
        self.display = num
        self.incount+=1
        print("Input: ", num)

    def push(self, value):
        self.stack.append(value)
        print("Stack: ")
        print(self.stack)


    def add(self):
        op_1 = self.stack.pop()
        op_2 = self.stack.pop()
        result = op_1 + op_2
        self.display = result
        self.stack.append(result)
        self.opcount+=1

    def sub(self):
        op_1 = self.stack.pop()
        op_2 = self.stack.pop()
        result = op_2 - op_1
        self.display = result
        self.stack.append(result)
        self.opcount+=1

    def mul(self):
        op_1 = self.stack.pop()
        op_2 = self.stack.pop()
        result = op_1 * op_2
        self.display = result
        self.stack.append(result)
        self.opcount+=1

    def div(self):
        op_1 = self.stack.pop()
        if op_1 == 0:
            print("DIVISION BY ZERO!")
            self.stack = []
            self.opcode = ''
            self.display = 'ERROR: DIVISION BY ZERO!'
            return
        op_2 = self.stack.pop()
        result = op_2 / op_1
        self.display = result
        self.stack.append(result)
        self.opcount+=1

if __name__ == '__main__':
    cpu = CalcCPU2()

    cpu.input(1.0)
    cpu.calc('+')
    cpu.input(1.0)
    cpu.calc('-')
    cpu.input(4.0)
    cpu.calc('+')
    cpu.input(4.0)
    cpu.calc('*')
    cpu.input(2.0)
    cpu.calc('=')
