from __future__ import annotations
from typing import Tuple


class ListNode:
    def __init__(self,data,next: ListNode = None) -> None:
        self.data=data
        self.next=next
        # self.prev = prev

    def __repr__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.__size=0

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        """
        - returns `True` if list is empty
        - returns `False` if list is not empty
        """
        return self.size () == 0

    def add(self,value):
        self.add_last (value)

    # edge case - empty list
    def add_last(self,value) -> None:
        if self.is_empty ():
            # node = ListNode(data=value)
            # self.head = node
            # self.tail = node
            self.head=self.tail=ListNode (data = value)
        else:
            # node olustur
            node=ListNode (value)
            # kuyrugun next i yap
            self.tail.next=node
            # node un prev ini eski kuyruk yap
            # node.prev = self.tail
            # node u kuyruk yap
            self.tail=node
        self.__size+=1

    # edge case - empty list
    def add_first(self,value) -> None:
        if self.is_empty ():
            # node = ListNode(data=value)
            # self.head = node
            # self.tail = node
            self.head=self.tail=ListNode (data = value)
        else:
            node=ListNode (data = value)
            node.next=self.head
            self.head=node
        self.__size+=1

    def add_after(self,after_value,value):
        if self.is_empty ():
            raise RuntimeError ("Empty List: can not add after")
        for node in self:
            if node.data == after_value:
                # edge case: last element -> tail
                if node is self.tail:
                    return self.add_last (value)
                new_node=ListNode (value,next = node.next)
                # new_node.next = node.next
                # new_node.prev = node
                node.next=new_node
                return
        raise RuntimeError (f"{after_value} is not in the list!")

    def add_before(self,before_value,value):
        if self.is_empty ():
            raise RuntimeError ("Empty List: can not add after")
        for node in self:
            if node.data == before_value:
                if node is self.head:
                    return self.add_first (value)
                new_node=ListNode (value,next = node)
                # node.prev.next = new_node
                # node.prev = new_node
                return
        raise RuntimeError (f"{before_value} is not in the list!")

    def find_value(self,value) -> Tuple[ListNode | None,int]:

        if value is None:
            raise RuntimeError ("can not find null value")

        if self.is_empty ():
            return None,-1

        index=0
        for node in self:
            if node.data == value:
                return node,index
            index+=1

        return None,-1

    def update(self,old_value,new_value):
        node,index=self.find_value (old_value)
        if index == -1:
            raise RuntimeError (f"Value: {old_value} not found in the list!")
        node.data=new_value

    def remove_first(self):
        if self.is_empty ():
            raise RuntimeError ("Empty list: can not remove first")
        temp=self.head.data

        self.head=self.head.next
        self.__size-=1

        if self.is_empty ():
            self.tail=None
        # else:
        #     self.head.prev = None

        return temp

    def remove_last(self):
        if self.is_empty ():
            raise RuntimeError ("Empty list: can not remove last")
        temp=self.head

        # self.tail = self.tail.prev
        self.__size-=1
        while self.head.next is not None:
            temp=temp.next
        temp.next=None

        return temp

    def index_of(self,value) -> int:
        node,index=self.find_value (value)
        return index

    def contains(self,value) -> bool:
        node,index=self.find_value (value)
        return index != -1

    def peek_first(self):
        if self.is_empty ():
            raise RuntimeError ("Empty list: can not peek first")
        return self.head.data

    def peek_last(self):
        if self.is_empty ():
            raise RuntimeError ("Empty list: can not peek last")
        return self.tail.data

    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next

    def __repr__(self) -> str:
        # [35, 15, 25]
        elements=[]
        for node in self:
            elements.append (str (node.data))
        return "[ "+" <--> ".join (elements)+" ]"
