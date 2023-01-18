from .node import Node

# Operazioni:
# append(self, dato) -> void
# remove(self, dato) -> str
# search(self, dato) -> bool
class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, info):
        if self.head == None :
            self.head = Node(info)
        else :
            new_nodo = Node(info)
            current = self.head
            while current.next_nodo != None:
                current = current.next_nodo
            current.next_nodo = new_nodo

    def remove(self, to_be_deleted):
        current_node = self.head

        if current_node != None:
            if current_node.info == to_be_deleted:
                self.head = current_node.next_nodo
                return

        while current_node != None :
            if current_node.info == to_be_deleted:
                break
            prev = current_node
            current_node = current_node.next_nodo
        if current_node == None:
            return

        prev.next_nodo = current_node.next_nodo
        current_node = None


    def stringher(self):
        current_node = self.head
        string = ""
        if current_node == None:
            string = "LINKED LIST VUOTA!"
        else:
            while current_node != None:
                string += current_node.info+" -> "
                current_node = current_node.next_nodo        
        return string

    def search(self, find):
        current_node = self.head
        if current_node == None:
            return False
        else:
            while current_node != None:
                if current_node.info == find:
                    return True
                else:
                    current_node = current_node.next_nodo