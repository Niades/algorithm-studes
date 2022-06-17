# Date: 18-06-22

import math

def find(haystack, needle):
    left, right = 0, len(haystack)
    middle = math.ceil(right - left - 1)
    while (left <= right):
        middle_value = haystack[middle]
        if middle_value == needle:
            return needle
        elif middle_value < needle:
            right = middle - 1
        elif middle_value > needle:
            left = middle + 1
        middle = math.ceil(right - left)
    return left

def main():
    assert find([1, 2, 3, 4], 1), 1
    assert find([1, 5, 6, 12, 13, 45, 63, 99, 101, 30000, 350000000], 101)
    print("All tests passed")

if __name__ == "__main__":
    main()
