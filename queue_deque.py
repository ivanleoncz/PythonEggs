#!/usr/bin/python3
''' Demonstrating the usage of collections.deque data type.'''

from collections import deque

queue = deque(["d","e","f"])
print("\nQueue:",queue)

queue.append("g")
queue.append("h")
queue.append("i")
print("\nQueue (new items -> right):  ",queue)

queue.pop()
print("Queue (less items -> right): ",queue)

queue.appendleft("c")
queue.appendleft("b")
queue.appendleft("a")
print("\nQueue (new items -> left):   ",queue)

queue.popleft()
print("Queue (less items -> left):  ",queue)

