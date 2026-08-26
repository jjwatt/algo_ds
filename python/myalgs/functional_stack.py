from __future__ import annotations

from typing import Protocol, runtime_checkable
from dataclasses import dataclass

class EmptyStackError(Exception):
    pass

@runtime_checkable
class Stack[T](Protocol):
    @property
    def is_empty(self) -> bool: ...

    def head(self) -> T: ...

    def tail(self) -> Stack[T]: ...


@dataclass(frozen=True, slots=True)
class Cons[T]:
    head_val: T
    tail_stack: Stack[T]

    @property
    def is_empty(self) -> bool:
        return False

    def head(self) -> T:
        return self.head_val

    def tail(self) -> Stack[T]:
        return self.tail_stack


@dataclass(frozen=True, slots=True)
class Nil[T]:
    @property
    def is_empty(self) -> bool:
        return True

    def head(self) -> T:
        raise EmptyStackError("Nil has no head")

    def tail(self) -> Stack[T]:
        raise EmptyStackError("Nil has no tail")


def cons[T](x: T, stack: Stack[T]) -> Stack[T]:
    return Cons(head_val=x, tail_stack=stack)


def to_list[T](stack: Stack[T]) -> list[T]:
    res: list[T] = []
    curr = stack
    while not curr.is_empty:
        res.append(curr.head())
        curr = curr.tail()
    return res


@dataclass(frozen=True, slots=True)
class TupleStack[T]:
    _data: tuple[T, ...] = ()

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def head(self) -> T:
        if not self._data:
            raise EmptyStackError("Cannot take the head of an empty TupleStack")
        return self._data[0]

    def tail(self) -> TupleStack[T]:
        if not self._data:
            raise EmptyStackError("Cannot take the tail of an emtpy TupleStack")
        return TupleStack(self._data[1:])

    def __repr__(self) -> str:
        return f"TupleStack{self._data}"

