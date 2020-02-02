from collections import Counter


def find_uniq(arr):
    return list(Counter(arr).keys())[list(Counter(arr).values()).index(1)]

print (find_uniq([0, 0, 0.55, 0, 0]))

