# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can
# flip at most k 0's.


def longestSubarray(nums):
    longest = prev = curr = 0

    for bit in nums:
        if bit:
            curr += 1
            longest = max(longest, prev + curr)
        else:
            prev, curr = curr, 0

    return longest - (longest == len(nums))


