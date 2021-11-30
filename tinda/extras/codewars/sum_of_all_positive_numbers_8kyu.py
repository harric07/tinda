# 8 kyu
# sum of all positive integers in an array
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# defualt: return 0


def positive_sum(arr):
    return sum([i for i in arr if i > 0]) if arr else 0

