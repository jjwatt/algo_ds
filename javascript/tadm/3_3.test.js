import assert from "node:assert/strict";
import { describe, it } from "node:test";
import { ListNode, reverseListIterative, reverseListRecursive } from "./3_3.js";

/**
 * Helper: Builds a linked list from an array of values.
 * @param {number[]} values
 * @returns {ListNode | null}
 */
function fromArray(values) {
    let head = null;
    for (let i = values.length - 1; i >= 0; i--) {
        head = new ListNode(values[i], head);
    }
    return head;
}

/**
 * Helper: Converts a linked list back into an array of values.
 * @param {ListNode | null} head
 * @returns {number[]}
 */
function toArray(head) {
    const result = [];
    let curr = head;
    while (curr !== null) {
        result.push(curr.val);
        curr = curr.next;
    }
    return result;
}

// Run the exact same test cases against both implementations.
const implementations = [
    { name: "reverseListRecursive", fn: reverseListRecursive },
    { name: "reverseListIterative", fn: reverseListIterative },
];

for (const { name, fn } of implementations) {
    describe(name, () => {
        it("returns null for an empty list", () => {
            assert.equal(fn(null), null);
        });

        it("returns the same node for a single-element list", () => {
            const node = new ListNode(42);
            const reversed = fn(node);
            assert.equal(reversed, node);
            assert.deepEqual(toArray(reversed), [42]);
        });

        it("reverses a two-element list", () => {
            const list = fromArray([1, 2]);
            const reversed = fn(list);
            assert.deepEqual(toArray(reversed), [2, 1]);
        });

        it("reverses a multi-element list and updates all pointers", () => {
            const list = fromArray([1, 2, 3, 4, 5]);
            const reversed = fn(list);
            assert.deepEqual(toArray(reversed), [5, 4, 3, 2, 1]);
        });
    });
}
