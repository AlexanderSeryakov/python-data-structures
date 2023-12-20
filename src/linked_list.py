from typing import Optional


class LinkedListIterator:
    def __init__(self, obj: "LinkedList") -> None:
        self.__current_node = obj.head

    def __iter__(self) -> "LinkedListIterator":
        return self

    def __next__(self) -> "Node":
        if self.__current_node is None:
            raise StopIteration
        node_to_return = self.__current_node
        self.__current_node = node_to_return.next
        return node_to_return


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, node: Node) -> Node:
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        return node

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)
