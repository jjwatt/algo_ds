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

    def member_fast(self, x: T) -> bool: ...

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
        """Standard 2d comparison lookup."""
        if x < self.val:
            return self.left.member(x)
        elif self.val < x:
            return self.right.member(x)
        else:
            return True

    def member_fast(self, x: T) -> bool:
        """Exercise 2.2: at most d + 1 comparisons via candidate tracking."""
        return _member_candidate(self, x, candidate=None)

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

    def member_fast(self, x: T) -> bool:
        return False

    def insert(self, x: T) -> Set[T]:
        return Tree(left=self, val=x, right=self)

    def __repr__(self) -> str:
        return "Empty"


def _member_candidate[T: Ordered](tree: Set[T], x: T, candidate: T | None) -> bool:
    match tree:
        case Empty():
            # Leaf reached: exact equality check with the last candidate seen.
            return candidate is not None and not (candidate < x)
        case Tree(left=l, val=v, right=r):
            if x < v:
                # x < v, so candidate remains unchanged.
                return _member_candidate(l, x, candidate)
            else:
                # v <= x, so 'v' becomes the newest potential candidate.
                return _member_candidate(r, x, candidate=v)
        case _:
            raise RuntimeError("Invalid Set")


def empty_set[T: Ordered]() -> Set[T]:
    return Empty[T]()


def insert[T: Ordered](x: T, s: Set[T]) -> Set[T]:
    return s.insert(x)


def member[T: Ordered](x: T, s: Set[T]) -> bool:
    return s.member(x)


def member_fast[T: Ordered](x: T, s: Set[T]) -> bool:
    return s.member_fast(x)


def to_sorted_list[T: Ordered](s: Set[T]) -> list[T]:
    """In-order traversal yielding sorted list."""
    if isinstance(s, Tree):
        return to_sorted_list(s.left) + [s.val] + to_sorted_list(s.right)
    return []
