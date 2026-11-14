#!/usr/bin/env node
// *** 3-1
// A common problem for compilers and text editors is determining whether
// parentheses in a string are balanced and properly nested. For
// example, the string =((())())()= contains properly nested pairs of
// parentheses, while the strings =)()(= and =())= do not. Give an
// algorithm that returns true if a string contains properly nested and
// balanced parentheses, and false if otherwise. For full credit,
// identify the position of the first offending parenthesis if the string
// is not properly nested and balanced.

import process from "node:process";
import { fileURLToPath } from "node:url";

/**
 * Checks whether parentheses in a string are balanced and properly nested.
 *
 * @param {string} s
 * @returns {{ balanced: boolean, offendingIndex: number | null }}
 */
export function checkBalancedParentheses(s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (ch === "(") {
      stack.push(i);
    } else if (ch === ")") {
      if (stack.length === 0) {
        return { balanced: false, offendingIndex: i };
      }
      stack.pop();
    }
  }

  if (stack.length > 0) {
    // If there are still items in the stack, there are unclosed parens.
    // First offending open paren is the earliest in the stack.
    return { balanced: false, offendingIndex: stack[0] };
  }

  return { balanced: true, offendingIndex: null };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const tests = [
    {
      input: "((())())()",
      want: { balanced: true, offendingIndex: null },
    },
    {
      input: ")()(",
      want: { balanced: false, offendingIndex: 0 },
    },
    {
      input: "())",
      want: { balanced: false, offendingIndex: 2 },
    },
    {
      input: "((())",
      want: { balanced: false, offendingIndex: 0 },
    },
  ];

  for (const { input, want } of tests) {
    const got = checkBalancedParentheses(input);
    const label = want.balanced ? "passing" : "failing";

    if (
      got.balanced === want.balanced &&
      got.offendingIndex === want.offendingIndex
    ) {
      console.log(`Successfully marked parens ${label}`);
    } else {
      console.error(
        `Programming Error: Algorithm failed to mark parens ${label}`,
      );
      process.exit(1);
    }
  }
}
