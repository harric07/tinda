# BINARY SEARCH
# Divide and conquer, kind of
import random
import time

def default_search(list, target):
    # example list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binary_search(list, target, low=None, high=None):
    # we need a sorder list here!
    # example list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if list[mid] == target:
        return mid
    elif list[mid] > target:
        return binary_search(list, target, low, mid - 1)
    else:
        return binary_search(list, target, mid + 1, high)


if __name__ == "__main__":
    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # target = 7
    # print(default_search(list, target))
    # print(binary_search(list, target))
    length = 10000
    sorter_list = set()
    while len(sorter_list) < length:
        sorter_list.add(random.randint(-3*length, 3*length))
    sorter_list = sorted(list(sorter_list))
    start_time = time.time()
    for i in sorter_list:
        default_search(sorter_list, i)
    end_time = time.time()
    x = end_time - start_time
    print(f"default search too '{end_time - start_time/length}' seconds.")
    start_time = time.time()
    for i in sorter_list:
        binary_search(sorter_list, i)
    end_time = time.time()
    y = end_time - start_time
    print(f"Binary search too '{end_time - start_time/length}' seconds.")
    print(f"Binary search is '{x/y}' times faster than default search.")
    print(f"Binary search is '{y/x}' times slower than default search.")
    print(f"The difference is '{x-y}' seconds.")
    print(f"The difference is '{(x-y)/x}' percent.")













