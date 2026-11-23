#!/usr/bin/env python3
# *** 3-4
# Design a stack /S/ that supports /S.push(x)/, /S.pop()/ and
# /S.findmin()/, which returns the minimum element of /S/. All
# operations should run in constant time.

import pytest
import random
from typing import Protocol, Self


class SupportsLe(Protocol):
    def __le__(self, other: Self, /) -> bool: ...


class MinStack[T: SupportsLe]:
    def __init__(self) -> None:
        self.data: list[T] = []
        self.mins: list[T] = []

    def push(self, x: T) -> None:
        self.data.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> T:
        if not self.data:
            raise IndexError("pop from empty MinStack")
        val = self.data.pop()
        if val <= self.mins[-1]:
            self.mins.pop()
        return val

    def findmin(self) -> T:
        if not self.mins:
            raise IndexError("findmin from empty MinStack")
        return self.mins[-1]


def test_generic_strings() -> None:
    stack = MinStack[str]()
    stack.push("pear")
    stack.push("apple")
    stack.push("banana")

    assert stack.findmin() == "apple"
    assert stack.pop() == "banana"
    assert stack.findmin() == "apple"
    assert stack.pop() == "apple"
    assert stack.findmin() == "pear"


def test_generic_ints() -> None:
    stack = MinStack[int]()
    stack.push(5)
    assert stack.findmin() == 5
    stack.push(3)
    assert stack.findmin() == 3
    stack.push(1)
    assert stack.findmin() == 1

    stack.push(2)
    assert stack.findmin() == 1
    stack.push(4)
    assert stack.findmin() == 1
