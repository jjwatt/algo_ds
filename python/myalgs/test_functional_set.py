from dataclasses import dataclass
from typing import Self

import pytest

from functional_set import (Empty, Set, Tree, empty_set, insert, member,
                            member_fast, to_sorted_list)


def test_empty_set_properties() -> None:
    s: Set[int] = empty_set()
    assert s.is_empty is True
    assert member(10, s) is False
    assert to_sorted_list(s) == []
    assert isinstance(s, Set)


def test_insert_and_membership() -> None:
    s: Set[int] = empty_set()
    s1 = insert(5, s)
    s2 = insert(3, s1)
    s3 = insert(7, s2)
    s4 = insert(1, s3)

    assert member(5, s4) is True
    assert member(3, s4) is True
    assert member(7, s4) is True
    assert member(1, s4) is True
    assert member(99, s4) is False
    assert to_sorted_list(s4) == [1, 3, 5, 7]


def test_functional_immutability() -> None:
    s0: Set[int] = empty_set()
    s1 = insert(10, s0)
    s2 = insert(20, s1)
    s3 = insert(5, s1)

    # s1 doesn't change.
    assert to_sorted_list(s1) == [10]
    assert to_sorted_list(s2) == [10, 20]
    assert to_sorted_list(s3) == [5, 10]


def test_duplicate_insertion_returns_same_node() -> None:
    s: Set[int] = insert(10, empty_set())
    s_dup = insert(10, s)

    # No unnecessary copies on duplicate insert.
    assert s_dup is s


def test_structural_sharing() -> None:
    # Build base:          10
    #                     /  \
    #                    5   15
    base: Set[int] = insert(15, insert(5, insert(10, empty_set())))
    assert isinstance(base, Tree)

    # Inserting 20 only copies the root and right subtree,
    # while the left subtree (5) is shared.
    extended = insert(20, base)
    assert isinstance(extended, Tree)

    assert extended.left is base.left
    assert extended.right is not base.right


def test_string_ordering() -> None:
    words: Set[str] = empty_set()
    for word in ["banana", "apple", "cherry", "date"]:
        words = insert(word, words)

    assert to_sorted_list(words) == ["apple", "banana", "cherry", "date"]
    assert member("apple", words) is True
    assert member("fig", words) is False


@dataclass(slots=True)
class CountedInt:
    value: int
    comparisons: int = 0

    def __lt__(self, other: Self, /) -> bool:
        self.comparisons += 1
        other.comparisons += 1
        return self.value < other.value

    
def test_member_fast_correctness() -> None:
    s: Set[int] = empty_set()
    elements = [50, 20, 70, 10, 30, 60, 80]
    for x in elements:
        s = insert(x, s)

    for x in elements:
        assert member_fast(x, s) is True

    assert member_fast(5, s) is False


def test_member_fast_comparison_bound() -> None:
    # Build a balanced BST of depth 3.
    #              40
    #           /      \
    #         20        60
    #        /  \      /  \
    #       10  30    50   70
    nums = [40, 20, 60, 10, 30, 50, 70]
    s: Set[CountedInt] = empty_set()
    for num in nums:
        s = insert(CountedInt(num), s)

    # Reset counter on target key.
    # Leaf node at depth 2.
    target = CountedInt(10)
    assert member_fast(target, s) is True

    # Depth is 2, number of nodes visited is 3, plus 1 at Empty.
    # Total comparisons for target must be <= d + 1 + 1 (4 comparisons).
    assert target.comparisons <= 4
