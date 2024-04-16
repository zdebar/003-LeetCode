# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or
# false otherwise.


def uniqueOccurrences(arr):
    occur = {}
    for i in arr:
        occur[i] = occur.get(i, 0) + 1
    values = [value for value in occur.values()]
    return len(values) == len(set(values))


arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(uniqueOccurrences(arr))
