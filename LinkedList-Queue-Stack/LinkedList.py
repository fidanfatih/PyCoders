from __future__ import annotations
from typing import Tuple


class ListNode:
    def __init__(self, data, next: ListNode = None, prev: ListNode = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__size = 0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        """
        - returns `True` if list is empty
        - returns `False` if list is not empty
        """
        return self.size() == 0

    def add(self, value):
        self.add_last(value)

    # edge case - empty list
    def add_last(self, value) -> None:
        if self.is_empty():
            # node = ListNode(data=value)
            # self.head = node
            # self.tail = node
            self.head = self.tail = ListNode(data=value)
        else:
            # node olustur
            node = ListNode(value, prev=self.tail)
            # kuyrugun next i yap
            self.tail.next = node
            # node un prev ini eski kuyruk yap
            # node.prev = self.tail
            # node u kuyruk yap
            self.tail = node
        self.__size += 1

    # edge case - empty list
    def add_first(self, value) -> None:
        if self.is_empty():
            # node = ListNode(data=value)
            # self.head = node
            # self.tail = node
            self.head = self.tail = ListNode(data=value)
        else:
            node = ListNode(data=value)
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.__size += 1

    def add_after(self, after_value, value):
        if self.is_empty():
            raise RuntimeError("Empty List: can not add after")
        for node in self:
            if node.data == after_value:
                # edge case: last element -> tail
                if node is self.tail:
                    return self.add_last(value)
                new_node = ListNode(value, prev=node, next=node.next)
                # new_node.next = node.next
                # new_node.prev = node
                node.next = new_node
                new_node.next.prev = new_node
                return
        raise RuntimeError(f"{after_value} is not in the list!")

    def add_before(self, before_value, value):
        if self.is_empty():
            raise RuntimeError("Empty List: can not add after")
        for node in self:
            if node.data == before_value:
                if node is self.head:
                    return self.add_first(value)
                new_node = ListNode(value, prev=node.prev, next=node)
                node.prev.next = new_node
                node.prev = new_node
                return
        raise RuntimeError(f"{before_value} is not in the list!")

    def find_value(self, value) -> Tuple[ListNode | None, int]:
        """
        Makes a linear search starting from the `head` of the list.

        - If `null` or (`None`) is provided as argument to be searched,
        raises a `RuntimeError`

        - If the value is not in the list returns `(None, -1)`

        - If found, `first element` is the `node` and the `second` is the `index` itself.
        """
        if value is None:
            raise RuntimeError("can not find null value")

        if self.is_empty():
            return None, -1

        index = 0
        for node in self:
            if node.data == value:
                return node, index
            index += 1

        return None, -1

    def update(self, old_value, new_value):
        node, index = self.find_value(old_value)
        if index == -1:
            raise RuntimeError(f"Value: {old_value} not found in the list!")
        node.data = new_value

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list: can not remove first")
        temp = self.head.data

        self.head = self.head.next
        self.__size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None

        return temp

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty list: can not remove last")
        temp = self.tail.data

        self.tail = self.tail.prev
        self.__size -= 1

        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None

        return temp

    def remove_node(self, node: ListNode):
        """use with caution: `node` can not be `None`"""
        if node is self.head:
            return self.remove_first()
        if node is self.tail:
            return self.remove_last()

        temp = node.data
        node.next.prev = node.prev
        node.prev.next = node.next

        node.next = None
        node.prev = None
        node = None
        self.__size -= 1

        return temp

    def remove_at(self, index: int):
        if index < 0 or index >= self.size():
            raise RuntimeError(f"index: {index} is out of list bounds!")

        node = None
        if index < self.size() / 2:
            node = self.head
            for _ in range(0, index):
                node = node.next
        else:
            node = self.tail
            for _ in range(index, self.size() - 1):
                node = node.prev

        return self.remove_node(node)

    def remove_value(self, value) -> bool:
        node, index = self.find_value(value)
        if index != -1:
            self.remove_node(node)
            return True
        return False

    def index_of(self, value) -> int:
        node, index = self.find_value(value)
        return index

    def contains(self, value) -> bool:
        node, index = self.find_value(value)
        return index != -1

    def peek_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list: can not peek first")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise RuntimeError("Empty list: can not peek last")
        return self.tail.data

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        # [35, 15, 25]
        elements = []
        for node in self:
            elements.append(str(node.data))
        return "[ " + " <--> ".join(elements) + " ]"
        # return elements


x = LinkedList()

x.add_last(15)  # 15
x.add_last(25)  # 15 -> 25
x.add_first(35)  # 35 -> 15 -> 25
x.add_after(15, 50)  # 35 -> 15 -> 50 -> 25
x.add_before(15, 90)  # 35 -> 90 -> 15 -> 50 -> 25
x.update(15, 0)

# for i in x:
#     print(i)

print(x)
