"""Strictly-typed linked list implementation."""
from collections.abc import Iterator
from typing import Self


class Node[T]:
    data: T
    next: Self | None

    def __init__(self, data: T, next_node: Self | None = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList[T]:
    head: Node[T] | None

    def __init__(self) -> None:
        self.head = None

    def append(self, data: T) -> None:
        """Appends an element to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def push_front(self, data: T) -> None:
        """Prepends an element to the beginning of the list."""
        self.head = Node(data, next_node=self.head)


    def __iter__(self) -> Iterator[T]:
        """Allows iteration over elements (yields T), satisfying Iterable[T]."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def display(self) -> None:
        print(" -> ".join(str(item) for item in self))


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    mylist.push_front(40)
    mylist.display()
