

# Operazioni
# is_empty(self) -> bool
# size(self) -> int
# enqueue(self, dato) -> void
# dequeue(self) -> bool
# head(self) -> int 
# tail(self) -> int

class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.internal_queue = []

    def is_empty(self):
        return self.size == 0

    def the_size(self):
        return(len(self.internal_queue))

    def enqueue(self, dato):
        if not self.head:
            self.head = dato
        self.tail = dato
        self.size += 1
        self.internal_queue.append(dato)
        return 

    def dequeue(self):
        if self.size <=0:
            return False
        else:
            self.size -= 1
            self.internal_queue.pop(0)
            if self.internal_queue:
                self.head = self.internal_queue[0]
            else:
                self.head = -1              
            return True

    def the_head(self):
        head = self.head if self.head else -1
        return head
    
    def the_tail(self):
        tail = self.tail if self.tail else -1
        return tail

