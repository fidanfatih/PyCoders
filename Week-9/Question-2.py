# Implement a queue using a single linked list. (Hint: Enqueuing happens at the tail of the list, and the dequeuing of items happens at the head of the list.)

from singlelinkedlist import LinkedList


class Queue:
    def __init__(self) -> None:
        self.__list=LinkedList ()

    def size(self):
        return self.__list.size ()

    def is_empty(self):
        return self.__list.is_empty ()

    def enqueue(self,value):
        self.__list.add (value)

    def dequeue(self):
        return self.__list.remove_first ()

    def peek(self):
        return self.__list.peek_first ()


queue=Queue ()
queue.enqueue ('A')
queue.enqueue ('B')
queue.enqueue ('C')
queue.enqueue ('D')

print (f'"{queue.dequeue ()}" is first item. It is removed.')
print (f'"{queue.peek ()}" is new first item.')
print (f'Size of list is {queue.size ()}')
print(f'"True" if the list is empty, "False" if not: {queue.is_empty ()}')
