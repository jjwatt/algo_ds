# Given an array of integers temperatures represents the daily
# temperatures, return an array answer such that answer[i] is the number
# of days you have to wait after the ith day to get a warmer
# temperature. If there is no future day for which this is possible,
# keep answer[i] == 0 instead.


# The Pattern: Next Greater Element => Monotonic Stack


def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n
    # Stores indices of unresolved days.
    stack = []

    for i, temp in enumerate(temperatures):
        # Resolve all colder days currently waiting on the stack.
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            ans[prev_day] = i - prev_day
        stack.append(i)
    return ans


def main():
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    output = daily_temperatures(temperatures)
    print(f"{output=}")


if __name__ == "__main__":
    main()
