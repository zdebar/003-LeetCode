# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.

from collections import Counter


def maxOperations2(nums, k):
    sum_numbers = Counter(nums)
    count = 0
    for key, value in sum_numbers.items():
        if key == (k - key):
            count += (value // 2) * 2
        else:
            count += min(value, sum_numbers.get(k - key, 0))

    return int(count / 2)


def maxOperations3(nums, k):
    helper = dict()
    count = 0
    for i in nums:
        if helper.get(k - i, 0) > 0:
            count += 1
            helper[k - i] -= 1
        else:
            helper[i] = helper.get(i, 0) + 1
    return count


def maxOperations(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            count += 1
            left += 1
            right -= 1
        elif total < k:
            left += 1
        else:
            right -= 1

    return count


nums = [3, 1, 3, 4, 3]
k = 6
print(maxOperations(nums, k))
