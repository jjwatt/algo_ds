#!/usr/bin/env python3
# *** 3-3
# Give an algorithm to reverse the direction of a given singly linked
# list. In other words, after the reversal all pointers should now point
# backwards. Your algorithm should take linear time.

from typing import Self


class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev: ListNode | None = None
    curr: ListNode | None = head

    while curr is not None:
        # Cache remainder of list.
        next_node = curr.next
        # Reverse the pointer.
        curr.next = prev
        # Advance prev to current node.
        prev = curr
        # Advance curr to next node.
        curr = next_node

    return prev
