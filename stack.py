from Stack.stack import Stack

stack_test = Stack()
print(stack_test.the_size())
print(stack_test.the_top())
print(stack_test.is_empty())

stack_test.push(5)
print(stack_test.the_size())
print(stack_test.the_top())

stack_test.push(3)
print(stack_test.the_size())
print(stack_test.the_top())

stack_test.push(1)
print(stack_test.the_size())
print(stack_test.the_top())

print(stack_test.is_empty())

print(stack_test.pop())
print(stack_test.the_size())
print(stack_test.the_top())

print(stack_test.pop())
print(stack_test.the_size())
print(stack_test.the_top())
print(stack_test.pop())
print(stack_test.the_size())
print(stack_test.the_top())
print(stack_test.pop())
print(stack_test.is_empty())
