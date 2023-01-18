from LinkedList.node import Node
from LinkedList.linkedList import LinkedList

nodo_test = Node('5')
print(nodo_test.info)

linked_list_test = LinkedList()
print(linked_list_test.stringher())
linked_list_test.append('5')
print(linked_list_test.stringher())
linked_list_test.append('7')
print(linked_list_test.stringher())
linked_list_test.append('3')
print(linked_list_test.stringher())

print(linked_list_test.search('a'))
print(linked_list_test.search(''))
print(linked_list_test.search('5'))
print(linked_list_test.search('3'))
print(linked_list_test.search('7'))
print(linked_list_test.search('71'))

linked_list_test.remove('9')
print(linked_list_test.stringher())
linked_list_test.remove('3')
print(linked_list_test.stringher())
linked_list_test.remove('5')
print(linked_list_test.stringher())
linked_list_test.remove('7')
print(linked_list_test.stringher())
linked_list_test.remove('0')
# print(linked_list_test.stringher())
