#!/usr/bin/env python3
# hackerrank.com/challenges/pangrams
import string


def pangram(s: str) -> bool:
    for letter in string.ascii_letters:
        if letter.lower() not in s.lower():
            return False
    return True


if __name__ == "__main__":
    input = "The quick brown fox jumps over the lazy dog"
    pangram_p = pangram(input)
    output = "pangram" if pangram_p else "not pangram"
    print(f"{output=}")
    if not pangram_p:
        raise RuntimeError("Programming error: Misidentified pangram")

    input = "Not a pangram"
    pangram_p = pangram(input)
    output = "pangram" if pangram_p else "not pangram"
    print(f"{output=}")
    if pangram_p:
        raise RuntimeError("Programming error: Misidentified pangram")
