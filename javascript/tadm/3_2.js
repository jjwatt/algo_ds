#!/usr/bin/env node
//  Give an algorithm that takes a string $S$ consisting of opening and
//  closing parentheses, say `)()(())()()))())))(`, and finds the length
//  of the longest balanced parenthesis in $S$, which is 12 in the example
//  above. (Hint: The solution is not necessarily a contiguous run of
//  parenthesis from $S$).

import process from "node:process";
import { fileURLToPath } from "node:url";

/**
 * Counts the longest balanced subsequence of parenthesis in a string.
 *
 * @param {string} s
 * @returns {number}
 */
export function longestBalancedSubsequenceLen(s) {
    let openCount = 0;
    let matchedPairs = 0;

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === "(") {
            openCount += 1;
        } else if (ch === ")") {
            if (openCount > 0) {
                matchedPairs += 1;
                openCount -= 1;
            }
        }
    }
    return matchedPairs * 2;
}

/**
 * Counts the longest balanced subsequence of parenthesis in a string with a stack.
 *
 * @param {string} s
 * @returns {number}
 */
export function longestBalancedSubsequenceLenStack(s) {
    const stack = [];
    let matchedPairs = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === "(") {
            stack.push(i);
        } else if (ch === ")") {
            if (stack.length !== 0) {
                stack.pop();
                matchedPairs += 2;
            }
        }
    }
    return matchedPairs;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
    const tests = [
        {
            input: ")()(())()()))())))(",
            want: 12,
        },
    ];
    for (const { input, want } of tests) {
        const got = longestBalancedSubsequenceLenStack(input);
        if (got === want) {
            console.log(`Successfully counted ${want} parentheses`);
        } else {
            console.error(`Failed to count ${want} parentheses, got ${got}`);
            process.exit(1);
        }
    }
}
