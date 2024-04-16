# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
# of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.

nums = [1, 7, 3, 6, 5, 6]


def pivotIndex(nums):
    left, right = 0, sum(nums[1:])
    if left == right:
        return 0
    for i in range(1, len(nums)):
        left += nums[i - 1]
        right -= nums[i]
        if left == right:
            return i
    return -1

print(pivotIndex(nums))
