

# Operazioni
# is_empty(self) -> bool
# size(self) -> int
# push(self, dato) -> void
# pop(self) -> bool
# top(self) -> int


class Stack:

    def __init__(self):
        self.size = 0
        self.top = None
        self.internal_stack = []

    def is_empty(self):
        return self.size == 0

    def the_size(self):
        return (len(self.internal_stack))

    def push(self, dato):
        self.size += 1
        self.top = dato
        self.internal_stack.append(dato)

    def pop(self):
        if self.size <= 0:
            return False
        else:
            self.size -=1
            if self.size-1 >=0:            
                self.top = self.internal_stack[self.size-1]
            else:
                self.top = 0
            self.internal_stack.pop()
            return True

    def the_top(self):
        if self.top == None:
            return 0
        else:
            return self.top