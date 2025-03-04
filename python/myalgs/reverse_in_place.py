def reverse_in_place(col):
    start = 0
    end = len(col) - 1
    while start < end:
        col[start], col[end] = col[end], col[start]
        start += 1
        end -= 1
