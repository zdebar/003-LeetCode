# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any
# answer with a calculation error less than 10-5 will be accepted.


nums = [1, 12, -5, -6, 50, 3]
k = 4


# def findMaxAverage(nums, k):
#     max_avg = sum(nums[:k]) / k
#     for i in range(1,len(nums)-k+1):
#         max_avg = max(sum(nums[i:i+k])/k, max_avg)
#     return max_avg

def findMaxAverage(nums, k):
    slide_sum = sum(nums[:k])
    max_sum = slide_sum
    for i in range(1, len(nums) - k + 1):
        slide_sum = slide_sum + nums[i + k - 1] - nums[i - 1]
        max_sum = max(slide_sum, max_sum)
    return float(max_sum / k)

print(findMaxAverage(nums, k))
