"""Strictly-typed linked list implementation."""
from collections.abc import Iterable, Iterator, MutableSequence
from typing import Self, cast, overload


class Node[T]:
    data: T
    next: Self | None

    def __init__(self, data: T, next_node: Self | None = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList[T](MutableSequence[T]):
    head: Node[T] | None
    _size: int

    def __init__(self, iterable: Iterable[T] | None = None) -> None:
        self.head = None
        self._size = 0
        if iterable is not None:
            self.extend(iterable)

    def __len__(self) -> int:
        """Returns the total number of elements in O(1) time."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allows iteration over elements (yields T), satisfying Iterable[T]."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def _get_node(self, index: int) -> Node[T]:
        """Helper to locate a node at a normalized index."""
        actual_idx = index if 0 <= index else index + self._size
        if not 0 <= actual_idx < self._size:
            raise IndexError("LinkedList index out of range")

        curr = self.head
        for _ in range(actual_idx):
            assert curr is not None
            curr = curr.next
        assert curr is not None
        return curr

    def insert(self, index: int, value: T) -> None:
        """Inserts an element at the specified index."""
        if index < 0:
            index += self._size
        if index <= 0:
            self.head = Node(value, next_node=self.head)
        elif self._size <= index:
            prev = self._get_node(self._size - 1)
            prev.next = Node(value)
        else:
            prev = self._get_node(index - 1)
            prev.next = Node(value, next_node=prev.next)
        self._size += 1

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
            return self._get_node(index).data

    @overload
    def __setitem__(self, index: int, value: T) -> None: ...

    @overload
    def __setitem__(self, index: slice, value: Iterable[T]) -> None: ...

    def __setitem__(self, index: int | slice, value: T | Iterable[T]) -> None:
        if isinstance(index, int):
            self._get_node(index).data = cast(T, value)
            return
        if isinstance(index, slice):
            target_indices = list(range(*index.indices(self._size)))
            values = list(cast(Iterable[T], value))

            if index.step is not None and index.step != 1:
                if len(target_indices) != len(values):
                    raise ValueError(
                        f"attempt to assign sequence of size {len(values)} "
                        f"to extended slice of size {len(target_indices)}"
                    )
                for idx, val in zip(target_indices, values):
                    self._get_node(idx).data = val
            else:
                # Contiguous slice replacement.
                for idx in reversed(target_indices):
                    del self[idx]
                    insert_idx = target_indices[0] if target_indices else self._size
                for val in reversed(values):
                    self.insert(insert_idx, val)
            return


    @overload
    def __delitem__(self, index: int) -> None: ...

    @overload
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index: int | slice) -> None:
        if isinstance(index, int):
            actual_idx = index if 0 <= index else index + self._size
            if not 0 <= actual_idx < self._size:
                raise IndexError("LinkedList assignment out of range")
            if actual_idx == 0:
                assert self.head is not None
                self.head = self.head.next
            else:
                prev = self._get_node(actual_idx - 1)
                assert prev.next is not None
                prev.next = prev.next.next
            self._size -= 1
            return
        if isinstance(index, slice):
            # Deleting in reverse order ensures earlier indices remain valid.
            for idx in reversed(range(*index.indices(self._size))):
                del self[idx]
            return

    def __repr__(self) -> str:
        return f"LinkedList([{', '.join(repr(x) for x in self)}])"


if __name__ == "__main__":
    # Initialize from iterable.
    ll = LinkedList([10, 20, 30, 40, 50])

    # Standard mutation & Indexing.
    ll[1] = 99
    ll.insert(0, 5)
    print(ll)

    # Deletion
    del ll[2]
    print(ll)

    # Mixin methods from MutableSequence.
    popped = ll.pop()
    print(popped)
    ll.append(60)
    ll.extend([70, 80])
    ll.remove(30)
    ll.reverse()
    print(f"After mixins: {ll}")

    # Slice assignment & slicing
    ll[1:3] = [700, 600]
    print(f"After slice set: {ll}")

