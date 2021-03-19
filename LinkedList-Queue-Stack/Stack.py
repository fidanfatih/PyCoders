# LIFO -> Last In First Out
from LinkedList import LinkedList


class Stack:
    def __init__(self) -> None:
        self.__list = LinkedList()

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.__list.is_empty()

    def push(self, value):
        self.__list.add_first(value)

    def pop(self):
        return self.__list.remove_first()

    def peek(self):
        return self.__list.peek_first()
