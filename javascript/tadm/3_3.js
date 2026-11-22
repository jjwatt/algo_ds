#!/usr/bin/env node
// *** 3-3
// Give an algorithm to reverse the direction of a given singly linked
// list. In other words, after the reversal all pointers should now point
// backwards. Your algorithm should take linear time.

/**
 * Represents a node in a singly linked list.
 */
export class ListNode {
    /**
     * @param {number} [val=0]
     * @param {ListNode | null} [next=null]
     */
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

/**
 * Reverse a singly linked list recursively.
 * Time Complexity: O(n)
 * Space Complexity: O(n) due to the recursion call stack.
 *
 * @param {ListNode | null} head
 * @returns {ListNode | null}
 */
export function reverseListRecursive(head) {
    if (head === null || head.next === null) {
        return head;
    }

    const newHead = reverseListRecursive(head.next);
    head.next.next = head;
    head.next = null;

    return newHead;
}

/**
 * Reverse singly linked list iteratively.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 *
 * @param {ListNode | null} head
 * @returns {ListNode | null}
 */
export function reverseListIterative(head) {
    let prev = null;
    let curr = head;

    while (curr !== null) {
        const nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }

    return prev;
}
