# Implement a stack that supports push and pop operations using standard enqueue and dequeue operations of the queue.

from collections import deque


class Stack:
    def __init__(self,size):
        self.size=size
        self.liste=deque ("")

    def push(self,item):
        self.liste.append (item)

    def pop(self):
        self.liste.pop ()

    def show(self):
        print (self.liste)


stack =Stack (5)

stack.push ("A")
stack.show ()
stack.push ("B")
stack.show ()
stack.push ("C")
stack.show ()
stack.push ("D")
stack.show ()
stack.push ("E")
stack.show ()

stack.pop ()
stack.show ()
stack.pop ()
stack.show ()
stack.pop ()
stack.show ()
stack.pop ()
stack.show ()
stack.pop ()
stack.show ()
