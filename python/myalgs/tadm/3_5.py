#!/usr/bin/env python3
# *** 3-5
# We have seen how dynamic arrays enable arrays to grow while still
# achieving constant time amortized performance. This problem concerns
# extending dynamic arrays to let them both grow and shrink on demand.

# (a) Consider an underflow strategy that cuts the array size in half
# whenever the array falls below half full. Give an example sequence of
# insertions and deletions where this strategy gives a bad amortized
# cost.

# (b) Then give a better underflow strategy than that suggested above,
# one that achieves constant amortized cost per deletion.

import ctypes
from typing import Any

import pytest


class DynamicArray[T]:
    def __init__(self) -> None:
        self.n: int = 0
        self.capacity: int = 1
        self.data: ctypes.Array[Any] = self.make_array(self.capacity)

    def __len__(self) -> int:
        return self.n

    def append(self, item: T) -> None:
        if self.n == self.capacity:
            # Double capacity when we run out.
            self.resize(2 * self.capacity)
        self.data[self.n] = item
        self.n += 1

    def pop(self) -> T:
        if self.n == 0:
            raise IndexError("pop from empty DynamicArray")
        item: T = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1

        # Shrink only when load drops to <= 25%, keeping capacity >= 1.
        if self.capacity > 1 and self.n <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return item

    def resize(self, new_cap: int) -> None:
        new_data = self.make_array(new_cap)
        for i in range(self.n):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_cap

    @staticmethod
    def make_array(cap: int) -> ctypes.Array[Any]:
        return (cap * ctypes.py_object)()


def test_doubling_on_overflow() -> None:
    arr = DynamicArray[int]()
    assert len(arr) == 0
    assert arr.capacity == 1

    # 1st item fits in initial capacity 1.
    arr.append(10)
    assert len(arr) == 1
    assert arr.capacity == 1

    # 2nd item overflows -> capacity doubles to 2
    arr.append(20)
    assert len(arr) == 2
    assert arr.capacity == 2

    # 3rd item overflows -> capacity doubles to 4
    arr.append(30)
    assert len(arr) == 3
    assert arr.capacity == 4

    # 4th item fits -> capacity stays 4
    arr.append(40)
    assert len(arr) == 4
    assert arr.capacity == 4

    # 5th item overflows -> capacity doubles to 8
    arr.append(50)
    assert len(arr) == 5
    assert arr.capacity == 8


def test_quarter_full_shrinking_threshold() -> None:
    arr = DynamicArray[int]()
    # Fill to capacity 8 (5 elements triggers cap=8; add 3 more to reach 8/8).
    for i in range(8):
        arr.append(i)
    assert len(arr) == 8
    assert arr.capacity == 8

    # Pop down to 3/8 -> must not shrink yet.
    for _ in range(5):
        arr.pop()
    assert len(arr) == 3
    assert arr.capacity == 8

    # Pop 1 more -> drops to 2/8 (25% full) -> shrinks capacity to 4 (50%).
    assert arr.pop() == 2
    assert len(arr) == 2
    assert arr.capacity == 4

    # Pop 1 more -> drops to 1/4 (25% full) -> shrinks capacity to 2 (50%).
    assert arr.pop() == 1
    assert len(arr) == 1
    assert arr.capacity == 2

    # Pop last item -> drops to 0/2 -> shrinks capacity to floor of 1.
    assert arr.pop() == 0
    assert len(arr) == 0
    assert arr.capacity == 1


def test_no_thrashing_at_half_capacity_boundary() -> None:
    """Verify alternating append/pop across the 50% boundary triggers zero resizes."""
    arr = DynamicArray[int]()
    # Grow capacity to 16 by inserting 9 elements
    for i in range(9):
        arr.append(i)
    assert len(arr) == 9
    assert arr.capacity == 16

    # Pop once so array sits right at 8/16 (50% full—the old naive threshold)
    arr.pop()
    assert len(arr) == 8
    assert arr.capacity == 16

    # Alternate append and pop around n=8; capacity must remain locked at 16
    for _ in range(50):
        arr.append(99)
        assert arr.capacity == 16
        assert arr.pop() == 99
        assert arr.capacity == 16


def test_data_integrity_across_grow_and_shrink_cycles() -> None:
    arr = DynamicArray[str]()
    items = [f"item-{i}" for i in range(65)]
    for item in items:
        arr.append(item)

    assert len(arr) == 65
    assert arr.capacity == 128

    # Drain completely and confirm LIFO order survives every reallocation.
    popped = [arr.pop() for _ in range(65)]
    assert popped == list(reversed(items))
    assert len(arr) == 0
    assert arr.capacity == 1


def test_pop_empty_raises() -> None:
    arr = DynamicArray[int]()
    with pytest.raises(IndexError):
        arr.pop()

    arr.append(1)
    arr.pop()

    with pytest.raises(IndexError):
        arr.pop()
