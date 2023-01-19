from Queue.queue import Queue

queue_test = Queue()
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())

queue_test.enqueue(5)
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())

queue_test.enqueue(3)
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())

print('dequeue')

queue_test.dequeue()
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())

queue_test.dequeue()
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())

queue_test.dequeue()
print(queue_test.the_head())
print(queue_test.the_tail())
print(queue_test.the_size())
print(queue_test.is_empty())
