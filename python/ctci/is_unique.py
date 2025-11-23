from collections.abc import Iterable

def is_unique_chars(string: str) -> bool:
    char_set = []
    for i, val in enumerate(string):
        if val in char_set:
            return False
        char_set.append(val)
    return True

def is_unique_iter(it: Iterable) -> bool:
    it_set = set()
    for item in it:
        if item in it_set:
            return False
        it_set.add(item)
    return True

if __name__ == "__main__":
    string = "hello"
    res = is_unique_chars(string)
    print(f"{res=}")
