from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Self, runtime_checkable


@runtime_checkable
class Ordered(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...


@runtime_checkable
class Set[T: Ordered](Protocol):
    @property
    def is_empty(self) -> bool: ...

    def member(self, x: T) -> bool: ...

    def insert(self, x: T) -> Set[T]: ...


@dataclass(frozen=True, slots=True)
class Tree[T: Ordered]:
    left: Set[T]
    val: T
    right: Set[T]

    @property
    def is_empty(self) -> bool:
        return False

    def member(self, x: T) -> bool:
        if x < self.val:
            return self.left.member(x)
        elif self.val < x:
            return self.right.member(x)
        else:
            return True

    def insert(self, x: T) -> Set[T]:
        if x < self.val:
            return Tree(left=self.left.insert(x), val=self.val, right=self.right)
        elif self.val < x:
            return Tree(left=self.left, val=self.val, right=self.right.insert(x))
        else:
            return self

    def __repr__(self) -> str:
        return f"Tree({self.left!r}, {self.val!r}, {self.right!r})"


@dataclass(frozen=True, slots=True)
class Empty[T: Ordered]:
    @property
    def is_empty(self) -> bool:
        return True

    def member(self, x: T) -> bool:
        return False

    def insert(self, x: T) -> Set[T]:
        return Tree(left=self, val=x, right=self)

    def __repr__(self) -> str:
        return "Empty"


def empty_set[T: Ordered]() -> Set[T]:
    return Empty[T]()


def insert[T: Ordered](x: T, s: Set[T]) -> Set[T]:
    return s.insert(x)


def member[T: Ordered](x: T, s: Set[T]) -> bool:
    return s.member(x)

def to_sorted_list[T: Ordered](s: Set[T]) -> list[T]:
    """In-order traversal yielding sorted list."""
    if isinstance(s, Tree):
        return to_sorted_list(s.left) + [s.val] + to_sorted_list(s.right)
    return []
