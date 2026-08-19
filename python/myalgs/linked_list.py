"""Strictly-typed linked list implementation."""
from collections.abc import Iterator, Sequence
from typing import Self, overload


class Node[T]:
    data: T
    next: Self | None

    def __init__(self, data: T, next_node: Self | None = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList[T](Sequence[T]):
    head: Node[T] | None
    _size: int

    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        """Returns the total number of elements in O(1) time."""
        return self._size

    def push_front(self, data: T) -> None:
        """Prepends an element to the beginning of the list."""
        self.head = Node(data, next_node=self.head)
        self._size += 1

    def append(self, data: T) -> None:
        """Appends an element to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node
        self._size += 1

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> "LinkedList[T]": ...

    def __getitem__(self, index: int | slice) -> T | "LinkedList[T]":
        # Handle slices.
        if isinstance(index, slice):
            sublist: LinkedList[T] = LinkedList()
            for i in range(*index.indices(self._size)):
                sublist.append(self[i])
            return sublist
        # Handle integer indexing.
        if isinstance(index, int):
            actual_idx = index if index >= 0 else index + self._size
            if not 0 <= actual_idx < self._size:
                raise IndexError("LinkedList index out of range")

            curr = self.head
            for _ in range(actual_idx):
                # Type narrowing guard.
                assert curr is not None
                curr = curr.next
            assert curr is not None
            return curr.data
        raise TypeError(f"Invalid argument type: {type(index).__name__}")
    
    def __iter__(self) -> Iterator[T]:
        """Allows iteration over elements (yields T), satisfying Iterable[T]."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def display(self) -> None:
        print(" -> ".join(str(item) for item in self))


if __name__ == "__main__":
    nums: LinkedList[int] = LinkedList()
    for n in (10, 20, 30, 40, 50):
        nums.append(n)

    # Collection protocol support.
    print(f"Length: {len(nums)}")
    print(f"30 in list? {30 in nums}")

    # Sequence protocol support (overload indexing).
    first_item: int = nums[0]
    last_item: int = nums[-1]
    print(f"Indices: {first_item=}, {last_item=}")

    # Slicing support.
    sliced: LinkedList[int] = nums[1:4]
    print(f"Slice [1:4]: {list(sliced)}")

    # Search and count mixins.
    print(f"Index of 40: {nums.index(40)}")
    print(f"Count of 20: {nums.count(20)}")

