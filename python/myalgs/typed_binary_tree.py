from typing import Protocol, Self


class BinaryNode[T](Protocol):
    value: T
    left: Self | None
    right: Self | None


class MyIntNode:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: MyIntNode | None = None
        self.right: MyIntNode | None = None


def tree_sum(node: BinaryNode[int] | None) -> int:
    if node is None:
        return 0
    return node.value + tree_sum(node.left) + tree_sum(node.right)

