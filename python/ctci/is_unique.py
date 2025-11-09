
def is_unique_chars(string: str) -> bool:
    char_set = []
    for i, c in enumerate(string):
        val = string[i]
        if val in char_set:
            return False
        char_set.append(c)
    return True

if __name__ == "__main__":
    string = "hello"
    res = is_unique_chars(string)
    print(f"{res=}")
