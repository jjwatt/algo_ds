# Given the head of a linked list, rotate the list to the right by k places.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    # Edge cases.
    if not head or not head.next or k == 0:
        return head

    # Compute the length of the list and locate the tail node.
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    # Normalize k.
    k = k % n
    if k == 0:
        return head

    # Connect tail to head to form a circular list.
    tail.next = head

    # Advance to the new tail: (n - k - 1) steps from head.
    steps_to_new_tail = n - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        assert new_tail.next is not None
        new_tail = new_tail.next

    # Set the new head and break the ring.
    new_head = new_tail.next
    new_tail.next = None

    return new_head
