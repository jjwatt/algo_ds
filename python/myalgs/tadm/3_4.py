#!/usr/bin/env python3
# *** 3-4
# Design a stack /S/ that supports /S.push(x)/, /S.pop()/ and
# /S.findmin()/, which returns the minimum element of /S/. All
# operations should run in constant time.

import pytest
import random


class MinStack:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.mins: list[int] = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> int:
        if not self.data:
            raise IndexError("pop from empty MinStack")
        val = self.data.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        return val

    def findmin(self) -> int:
        if not self.mins:
            raise IndexError("findmin from empty MinStack")
        return self.mins[-1]


def test_single_element() -> None:
    stack = MinStack()
    stack.push(42)

    assert stack.findmin() == 42
    assert stack.pop() == 42


def test_decreasing_and_increasing_pushes() -> None:
    stack = MinStack()

    # Decreasing: every push updates the minimum.
    stack.push(5)
    assert stack.findmin() == 5
    stack.push(3)
    assert stack.findmin() == 3
    stack.push(1)
    assert stack.findmin() == 1

    # Increasing: minimum should remain 1.
    stack.push(2)
    assert stack.findmin() == 1
    stack.push(4)
    assert stack.findmin() == 1

    # Unwind and verify minimum restores accurately
    assert stack.pop() == 4
    assert stack.findmin() == 1
    assert stack.pop() == 2
    assert stack.findmin() == 1
    assert stack.pop() == 1
    assert stack.findmin() == 3
    assert stack.pop() == 3
    assert stack.findmin() == 5


def test_randomized_against_oracle() -> None:
    rng = random.Random(42)
    stack = MinStack()
    oracle: list[int] = []

    for _ in range(1_000):
        if not oracle or rng.random() < 0.6:
            val = rng.randint(-50, 50)
            stack.push(val)
            oracle.append(val)
        else:
            assert stack.pop() == oracle.pop()

        if oracle:
            assert stack.findmin() == min(oracle)
